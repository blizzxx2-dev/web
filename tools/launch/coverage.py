#!/usr/bin/env python3
"""Coverage radar: find videos about the game, and keep view counts current.

  python3 coverage.py --known known.json --contacts CONTACTS_DIR --out coverage.csv

Three passes, all against public YouTube pages:
  1. Refresh title, date and views for every item already in known.json.
  2. Open the Videos tab of every contacted creator (contacts exported from the
     outreach tracker as one JSON file per contact) and flag any upload whose
     title names the game. Roundup videos that only mention it inside the video
     or its description are not caught: YouTube puts video pages behind a bot
     check, and this tool does not try to get around that.
  3. Search YouTube for recent uploads that name the game.

New finds are printed and added to known.json with "new": true. They stay out
of the CSV until someone has looked at them and removed that flag, because
"Engagement" is a common word and a title match can be about something else.
"""
import argparse, concurrent.futures as cf, csv, datetime as dt, glob, html, json, os, re, subprocess

GAME = "Engagement"
APPID = "5195200"
TITLE_RE = re.compile(r"\bengagement\b", re.I)
# "Engagement" is a common word, so a search hit also has to sound like a game video.
CONTEXT_RE = re.compile(r"rogue|survivor|bullet.?(heaven|hell)|capital ship|battleship|space|fleet|demo|gameplay|first look|steam|indie game|auto.?battler|trevor", re.I)
OWN = {"trevor games", "engagement - space roguelite"}  # the developer's own channels are not coverage
SEARCHES = ["engagement capital ship", "engagement roguelite", "engagement trevorgames", "engagement bullet heaven", "engagement space survivors gameplay"]


def get(url):
    return subprocess.run(["curl", "-sL", "-m", "25", "-A", "Mozilla/5.0", "-H", "Accept-Language: en-US", url], capture_output=True, text=True).stdout


def initial_data(page):
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", page, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except Exception:
        return None


def walk(o):
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from walk(v)
    elif isinstance(o, list):
        for v in o:
            yield from walk(v)


def channel_videos(link):
    """[(video id, title, age text, views text)] for a channel's newest uploads."""
    m = re.search(r"youtube\.com/(@[^/?\s]+|channel/[^/?\s]+|c/[^/?\s]+|user/[^/?\s]+)", link or "")
    if not m:
        return []
    d = initial_data(get(f"https://www.youtube.com/{m.group(1)}/videos"))
    out = []
    for o in walk(d) if d else []:
        if "contentId" in o and "metadata" in o:
            md = o["metadata"].get("lockupMetadataViewModel", {})
            title = md.get("title", {}).get("content")
            meta = re.findall(r'"content": "([^"]+)"', json.dumps(md.get("metadata", {})))
            if title:
                out.append((o["contentId"], title, meta[-1] if meta else "", meta[-2] if len(meta) > 1 else ""))
        elif "videoId" in o and isinstance(o.get("title"), dict) and "publishedTimeText" in o:
            t = o["title"]
            out.append((o["videoId"], (t.get("runs") or [{}])[0].get("text") or t.get("simpleText") or "", o["publishedTimeText"].get("simpleText", ""),
                        o.get("viewCountText", {}).get("simpleText", "")))
    return out[:30]


def count(text):
    """'1.1K views' -> 1100"""
    m = re.match(r"([\d.,]+)\s*([KMB]?)", (text or "").replace(",", ""))
    if not m or not m.group(1):
        return ""
    return int(float(m.group(1)) * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)])


def age_to_date(age, today):
    """'6d ago', '4w ago', '2 days ago' -> an ISO date (to the day at best)."""
    m = re.match(r"(?:Streamed\s+)?(\d+)\s*(minutes?|min|hours?|h|days?|d|weeks?|w|months?|mo|years?|y)\b", age or "")
    if not m:
        return ""
    unit = m.group(2)
    per = 0 if unit[0] in "h" or unit.startswith("min") else 1 if unit[0] == "d" else 7 if unit[0] == "w" else 30 if unit.startswith("mo") else 365
    return (today - dt.timedelta(days=int(m.group(1)) * per)).isoformat()


_chan = {}


def video(vid):
    """Title and channel from YouTube's oEmbed endpoint, views and age from the channel's own Videos tab."""
    try:
        o = json.loads(get(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"))
    except Exception:
        return {"id": vid, "title": "", "channel": "", "views": "", "date": ""}
    url = o.get("author_url", "")
    if url not in _chan:
        _chan[url] = channel_videos(url)
    row = next((v for v in _chan[url] if v[0] == vid), None)
    return {"id": vid, "title": o.get("title", ""), "channel": o.get("author_name", ""),
            "views": count(row[3]) if row else "", "date": age_to_date(row[2], dt.date.today()) if row else ""}


def scan_contact(c):
    return [(vid, "title", c) for vid, title, age, views in channel_videos(c.get("link")) if TITLE_RE.search(title)]


def search():
    found = []
    for q in SEARCHES:
        d = initial_data(get("https://www.youtube.com/results?search_query=" + q.replace(" ", "+") + "&sp=EgIIBA%253D%253D"))  # uploaded this month
        for o in walk(d) if d else []:
            v = o.get("videoRenderer")
            title = v["title"]["runs"][0]["text"] if v else ""
            if v and TITLE_RE.search(title) and CONTEXT_RE.search(title):
                ch = v.get("ownerText", {}).get("runs", [{}])[0].get("text", "")
                if ch.lower() not in OWN:
                    found.append(v["videoId"])
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--known", required=True)
    ap.add_argument("--contacts")
    ap.add_argument("--out", required=True)
    ap.add_argument("--skip-scan", action="store_true")
    a = ap.parse_args()
    known = json.load(open(a.known))
    ids = {k["id"] for k in known if k.get("id")}
    new = []
    if a.contacts and not a.skip_scan:
        contacts = []
        for f in glob.glob(os.path.join(a.contacts, "*.json")):
            d = json.load(open(f))
            d = d.get("data", d)
            if d.get("sentAt") and "youtube.com" in (d.get("link") or "") and (d.get("game") in (None, "", "engagement")):
                contacts.append(d)
        print("scanning", len(contacts), "contacted channels")
        with cf.ThreadPoolExecutor(8) as ex:
            for hits in ex.map(scan_contact, contacts):
                for vid, where, c in hits:
                    if vid not in ids:
                        ids.add(vid)
                        new.append({"id": vid, "kind": "video", "found": where, "contact": c.get("name")})
    if not a.skip_scan:
        for vid in search():
            if vid not in ids:
                ids.add(vid)
                new.append({"id": vid, "kind": "video", "found": "search"})
    for n in new:
        n["new"] = True
        known.append(n)
    for k in known:
        if k.get("id"):
            v = video(k["id"])
            if v["channel"].lower() in OWN:
                k["own"] = True
                continue
            k.update(outlet=k.get("outlet") or v["channel"], title=k.get("title_en") or v["title"] or k.get("title", ""), views=v["views"] or k.get("views", ""),
                     date=k.get("date") or v["date"], url=f"https://youtu.be/{k['id']}")
    known = [k for k in known if not k.get("own")]
    json.dump(known, open(a.known, "w"), indent=1, ensure_ascii=False)
    with open(a.out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "outlet", "title", "kind", "views", "url"])
        for k in sorted((k for k in known if not k.get("new")), key=lambda k: k.get("date", ""), reverse=True):
            w.writerow([k.get("date", ""), k.get("outlet", ""), html.unescape(k.get("title", "")), k.get("kind", ""), k.get("views", ""), k.get("url", "")])
    print("coverage items:", len([k for k in known if not k.get("new")]), "| new this run, waiting for a look:", len(new))
    for n in new:
        print("  NEW:", n.get("outlet"), "|", n.get("title"), "|", n.get("url"), "| found in", n.get("found"), "| contact:", n.get("contact"))


if __name__ == "__main__":
    main()
