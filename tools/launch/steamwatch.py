#!/usr/bin/env python3
"""steamwatch: one-run snapshot of where a Steam game stands.

Before release it reads the Popular Upcoming lists (overall and per tag), who is
ahead, when each of them releases, and where the game should land once the
earlier releases leave. After release it reads New & Trending and Top Sellers
per tag plus the review count. Every run appends one line to a history file and
prints what changed since the previous run and since about a day ago.

Usage:
  python3 steamwatch.py --out DIR            # snapshot, print report
  python3 steamwatch.py --out DIR --quiet    # snapshot only

Files written in DIR:
  history.jsonl   one compact line per run (the time series)
  latest.json     the full latest snapshot (who is ahead, projections)

Only public Steam store pages are read. No login, no keys.
"""
import argparse, datetime as dt, html, json, os, re, subprocess, sys, time

APP = "5195200"
NAME = "Engagement"
LAUNCH = dt.date(2026, 11, 12)
TAGS = [  # (key, label, Steam tag id) in the order Trevor cares about
    ("bullet_heaven", "Bullet Heaven", 723991),
    ("flight", "Flight", 15045),
    ("space", "Space", 1755),
    ("local_coop", "Local Co-Op", 3841),
    ("action_roguelike", "Action Roguelike", 42804),
    ("coop", "Co-op", 1685),
    ("roguelike", "Roguelike", 1716),
    ("overall", "Overall", None),
]
SEARCH = "https://store.steampowered.com/search/results/?query&start={start}&count=100&filter={flt}&infinite=1&cc=us&l=english{tag}"
MONTHS = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}


def fetch(url, tries=3, cookie=None):
    for i in range(tries):
        r = subprocess.run(["curl", "-s", "-L", "-m", "30", "-H", "Accept-Language: en-US"] + (["-b", cookie] if cookie else []) + [url], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout
        time.sleep(1.5 * (i + 1))
    return ""


def rows_of(results_html):
    out = []
    for blk in results_html.split("<a href=")[1:]:
        a = re.search(r'data-ds-appid="(\d+)"', blk)
        if not a:
            continue
        t = re.search(r'class="title">([^<]+)<', blk)
        r = re.search(r"search_released[^>]*>\s*([^<]*?)\s*<", blk)
        out.append({"app": a.group(1), "name": html.unescape(t.group(1)) if t else "", "rel": r.group(1) if r else ""})
    return out


def rel_date(s):
    """'Nov 12, 2026' -> date. Vague strings ('November 2026', '2026', 'Coming soon') -> None."""
    m = re.match(r"^([A-Z][a-z]{2}) (\d{1,2}), (\d{4})$", s or "")
    if not m or m.group(1) not in MONTHS:
        return None
    return dt.date(int(m.group(3)), MONTHS[m.group(1)], int(m.group(2)))


def walk(flt, tag, stop_app=None, max_n=1500):
    """Rows of a search list up to and including stop_app. Returns (rows, rank or None, total)."""
    stop_app = stop_app or APP
    rows, total = [], None
    for start in range(0, max_n, 100):
        raw = fetch(SEARCH.format(start=start, flt=flt, tag=f"&tags={tag}" if tag else ""))
        try:
            d = json.loads(raw)
        except Exception:
            break
        total = d.get("total_count", total)
        page = rows_of(d.get("results_html", ""))
        if not page:
            break
        for r in page:
            rows.append(r)
            if r["app"] == stop_app:
                return rows, len(rows), total
        if total is not None and len(rows) >= total:
            break
    return rows, None, total


_fol = {}


def followers(app):
    if app not in _fol:
        x = fetch(f"https://steamcommunity.com/games/{app}/memberslistxml/?xml=1", tries=2)
        m = re.search(r"<memberCount>(\d+)", x)
        _fol[app] = int(m.group(1)) if m else None
    return _fol[app]


def front_page():
    """Position of the app in the store front page tabs (top 30 upcoming, new releases), or None."""
    h = fetch("https://store.steampowered.com/?cc=us&l=english")
    out = {}
    for key, tab in (("popular_upcoming_tab", "tab_upcoming_content"), ("new_releases_tab", "tab_newreleases_content")):
        i = h.find(f'id="{tab}"')
        if i < 0:
            out[key] = None
            continue
        j = h.find('class="home_tab_content"', i + 10)
        ids = re.findall(r'data-ds-appid="(\d+)"', h[i : j if j > 0 else i + 200000])
        out[key] = ids.index(APP) + 1 if APP in ids else None
        out[key + "_size"] = len(ids)
    return out


def app_state():
    d = {}
    try:
        j = json.loads(fetch(f"https://store.steampowered.com/api/appdetails?appids={APP}&cc=us&filters=basic,price_overview,release_date"))[APP]["data"]
        d["coming_soon"] = j.get("release_date", {}).get("coming_soon")
        d["release"] = j.get("release_date", {}).get("date")
        p = j.get("price_overview") or {}
        d["price"] = p.get("final", 0) / 100 if p else None
        d["discount"] = p.get("discount_percent") if p else None
    except Exception:
        d["coming_soon"] = None
    # Review count and label come from the store page itself (the reviews API returns nothing from here).
    page = fetch(f"https://store.steampowered.com/app/{APP}/?cc=us&l=english", cookie="birthtime=0; wants_mature_content=1")
    m = re.search(r'itemprop="reviewCount" content="(\d+)"', page) or re.search(r"not_enough_reviews\">\s*([\d,]+) user reviews?", page)
    d["reviews"] = int(m.group(1).replace(",", "")) if m else (0 if "No user reviews" in page else None)
    m = re.search(r'game_review_summary [a-z_ ]*"(?: itemprop="description")?>([^<]+)<', page)
    d["review_desc"] = m.group(1).strip() if m else None
    m = re.search(r"(\d+)% of the [\d,]+ user reviews", page)
    d["positive_pct"] = int(m.group(1)) if m else None
    return d


def snapshot():
    now = dt.datetime.now(dt.timezone.utc)
    st = app_state()
    released = st.get("coming_soon") is False
    snap = {"t": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "ms": int(now.timestamp() * 1000), "phase": "released" if released else "upcoming",
            "followers": followers(APP), "app": st, "lists": {}}
    snap.update(front_page())
    for key, label, tag in TAGS:
        entry = {"label": label}
        if not released:
            rows, rank, total = walk("popularcomingsoon", tag)
            entry.update(rank=rank, total=total)
            if rank:
                ahead = rows[:-1]
                for r in ahead:
                    d = rel_date(r["rel"])
                    r["leaves"] = bool(d and d < LAUNCH)  # releases before us, so it drops off the upcoming list first
                stay = [r for r in ahead if not r["leaves"]]
                entry["ahead"] = len(ahead)
                entry["leaving"] = len(ahead) - len(stay)
                entry["projected"] = len(stay) + 1
                if key != "overall":
                    for r in stay[:8]:
                        r["followers"] = followers(r["app"])
                    entry["ahead_list"] = [{k: r.get(k) for k in ("app", "name", "rel", "leaves", "followers")} for r in ahead[:25]]
                entry["stay_list"] = [{k: r.get(k) for k in ("app", "name", "rel", "followers")} for r in stay[:12]]
        else:
            for flt, name in (("popularnew", "trending"), ("topsellers", "sellers")):
                rows, rank, total = walk(flt, tag, max_n=300)
                entry[name] = rank
                entry[name + "_total"] = total
        snap["lists"][key] = entry
    if not released:
        # how exclusive New & Trending is for our best tag, as a launch-day benchmark
        rows, _, total = walk("popularnew", 723991, stop_app="-", max_n=100)
        snap["bh_trending_now"] = [{"name": r["name"], "rel": r["rel"]} for r in rows[:8]]
    return snap


def compact(s):
    c = {"t": s["t"], "ms": s["ms"], "phase": s["phase"], "followers": s.get("followers"),
         "upcoming_tab": s.get("popular_upcoming_tab"), "new_tab": s.get("new_releases_tab"),
         "reviews": s["app"].get("reviews")}
    for k, e in s["lists"].items():
        if s["phase"] == "upcoming":
            c[k] = e.get("rank")
            c[k + "_proj"] = e.get("projected")
        else:
            c[k + "_trend"] = e.get("trending")
            c[k + "_sell"] = e.get("sellers")
    return c


def load_history(path):
    out = []
    if os.path.exists(path):
        for line in open(path):
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except Exception:
                    pass
    return out


def arrow(new, old):
    if new is None or old is None:
        return ""
    if new == old:
        return "  ="
    return f" {'+' if old > new else '-'}{abs(old - new)}"  # + means moved up (smaller rank number)


def report(s, hist):
    prev = hist[-1] if hist else None
    day = None
    for h in hist:
        if s["ms"] - h["ms"] >= 20 * 3600 * 1000:
            day = h  # latest snapshot that is at least ~a day old
    when = dt.datetime.strptime(s["t"], "%Y-%m-%dT%H:%M:%SZ")
    print(f"{NAME} on Steam, {when:%b %d %H:%M} UTC, {'RELEASED' if s['phase']=='released' else 'upcoming'}")
    f = s.get("followers")
    print(f"followers {f}" + (f" ({arrow(-f, -prev['followers']).strip()} since last run)" if prev and prev.get("followers") and f else ""))
    if s["phase"] == "upcoming":
        print(f"{'list':18}{'now':>5}{'vs last':>9}{'vs ~24h':>9}{'by launch eve':>15}  stays ahead")
        for key, label, _ in TAGS:
            e = s["lists"][key]
            stays = ", ".join(r["name"] for r in e.get("stay_list", [])[:4]) if key != "overall" else ""
            print(f"{label:18}{str(e.get('rank') or '-'):>5}{arrow(e.get('rank'), prev.get(key) if prev else None):>9}{arrow(e.get('rank'), day.get(key) if day else None):>9}{('#' + str(e['projected'])) if e.get('projected') else '-':>15}  {stays}")
        pu = s.get("popular_upcoming_tab")
        print(f"front page Popular Upcoming tab (top {s.get('popular_upcoming_tab_size')}): {'#' + str(pu) if pu else 'not on it'}")
        print("Bullet Heaven New & Trending right now:", "; ".join(f"{r['name']} ({r['rel']})" for r in s.get("bh_trending_now", [])))
    else:
        a = s["app"]
        print(f"reviews {a.get('reviews')} ({a.get('review_desc')}, {a.get('positive_pct')}% positive), price ${a.get('price')} ({a.get('discount')}% off)")
        nt = s.get("new_releases_tab")
        print(f"front page New Releases tab: {'#' + str(nt) if nt else 'not on it'}")
        print(f"{'list':18}{'New & Trending':>16}{'Top Sellers':>13}")
        for key, label, _ in TAGS:
            e = s["lists"][key]
            print(f"{label:18}{str(e.get('trending') or '-'):>16}{str(e.get('sellers') or '-'):>13}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--app", help="check another app id (for testing the after-release view on a game that is already out)")
    a = ap.parse_args()
    if a.app:
        global APP, NAME
        APP, NAME = a.app, "app " + a.app
    os.makedirs(a.out, exist_ok=True)
    hp = os.path.join(a.out, "history.jsonl")
    hist = load_history(hp)
    s = snapshot()
    if not any(e.get("rank") or e.get("trending") or e.get("sellers") for e in s["lists"].values()) and s.get("followers") is None:
        sys.exit("Steam returned nothing usable; history left untouched.")
    with open(hp, "a") as fh:
        fh.write(json.dumps(compact(s)) + "\n")
    json.dump(s, open(os.path.join(a.out, "latest.json"), "w"), indent=1)
    if not a.quiet:
        report(s, hist)


if __name__ == "__main__":
    main()
