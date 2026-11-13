#!/usr/bin/env python3
"""Builds the launch-day "it's out, your key works" email queue.

  python3 launch_queue.py --contacts EXPORT_DIR --out queue.json [--plan plan.json]
                          [--wishlists 10,000] [--discount] [--per-hour 40]

EXPORT_DIR holds one JSON file per contact, exported from the outreach tracker.
Nothing is sent from here: the queue is a file Claude reads when it sends.

Who is in it: everyone who was emailed a Steam key and has not passed, bounced
or been put on hold. Order: people who replied or covered the game first, then
by reach. Day 1 is launch day (replied/covered, everyone at 10K and up, and all
press), day 2 is the rest, so the account stays well under Gmail's 500-a-day
limit.

The plan file is private and lives in the outreach tracker's database, not in
this repo (collection "launch", document "plan"). It holds:
  greets    {contact id: name to greet}
  skip      [contact ids to leave out]
  reach     {contact id: audience size} for big channels whose notes carry no
            number, so they are not sorted in with the small ones
  wishlists the figure for "wishlisted over N times": Steamworks' lifetime
            wishlist additions, rounded down, as Trevor gave it
  personal  {contact id: {greet, body, subject?, thread?, to?}} hand-written
            notes for people who replied or covered. In a body, {KEY} is the
            contact's key, {STORE} the store link, and {DISC} the launch
            discount sentence (empty unless --discount is given).
A replied/covered contact with no personal note is reported and left out.

Keys end up in the queue file, which is why it is written outside the repo.
"""
import argparse, glob, json, os, re

STORE = "https://store.steampowered.com/app/5195200/?utm_source=creator&utm_medium=email&utm_campaign=launch&utm_content=engagement"
SKIP = {
    "y9-ardjunatv",        # declined, key revoked
    "y7-floydsonson", "y7-skoottie", "y7-trentomento",  # cut as bad fits
    "potatomcwhiskey",     # gets his own note with an early key
}
EMAIL_RE = re.compile(r"^[^@\s,]+@[^@\s,]+\.[^@\s,]+$")


def reach(notes):
    """Biggest audience number in the first part of the notes (subs, followers or views)."""
    head, best = (notes or "")[:220], 0
    for num, unit in re.findall(r"([\d.]+)\s*([KM])\b", head):
        try:
            best = max(best, float(num) * (1e6 if unit == "M" else 1e3))
        except ValueError:
            pass
    for num in re.findall(r"\b\d{1,3}(?:,\d{3})+\b", head):  # written out, as in "781,221 followers"
        best = max(best, float(num.replace(",", "")))
    return int(best)


def first_name(c):
    if c.get("kind") in ("press", "feature"):
        m = re.search(r" - ([A-Z][a-z]+)\b", c.get("name") or "")  # "Outlet - First Last (Role)"
        return m.group(1) if m else "there"
    n = re.split(r"\s[-(|]", c.get("name") or "")[0]
    n = re.sub(r"\s*\(.*$", "", n).strip()
    return n or "there"


def body(greet, key, early, day, wishlists, discount):
    opener = "Engagement is out on Steam today." if day == 1 else "Engagement is out now on Steam. It launched yesterday."
    keyline = (f"Your key from my earlier email already unlocks the full game: {key}" if early
               else f"Your key from my earlier email unlocks the full game now: {key}")
    facts = "You can play it solo or in co-op with friends."
    if wishlists:
        facts += f" It has been wishlisted over {wishlists} times" + (", and it's 20% off for launch week." if discount else ".")
    elif discount:
        facts += " It's 20% off for launch week."
    return "\n".join([
        f"Hi {greet},", "",
        opener, "",
        keyline, "",
        "A quick reminder of what it is: you command one capital ship against a swarm that grows every minute, "
        "bolting salvaged guns onto the hull and raising a fleet of escorts around it. " + facts, "",
        f"Steam page: {STORE}", "",
        "If you cover it, I'd love to see it, and I'm around all day if you need anything.", "",
        "Thanks,", "Trevor", "TrevorGames", "blizzxx2@gmail.com",
    ])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--contacts", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--plan")
    ap.add_argument("--wishlists", help="overrides the plan's wishlists value")
    ap.add_argument("--discount", action="store_true")
    ap.add_argument("--per-hour", type=int, default=40)
    a = ap.parse_args()
    plan = json.load(open(a.plan)) if a.plan else {}
    plan = plan.get("data", plan)
    greets, personal, skip = plan.get("greets", {}), plan.get("personal", {}), SKIP | set(plan.get("skip", []))
    disc = " It's 20% off for launch week." if a.discount else ""
    wishlists = a.wishlists if a.wishlists is not None else plan.get("wishlists", "")

    rows, problems = [], []
    for f in glob.glob(os.path.join(a.contacts, "*.json")):
        cid = os.path.basename(f)[:-5]
        c = json.load(open(f))
        c = c.get("data", c)
        key = (c.get("earlyKey") or c.get("key") or "").strip()
        if not key or not c.get("sentAt") or cid in skip or c.get("hold"):
            continue
        if c.get("status") in ("passed", "bounced", "todo") or c.get("game") not in (None, "", "engagement"):
            continue
        emails = [e.strip() for e in (c.get("email") or "").split(",") if e.strip()]
        if not emails or not all(EMAIL_RE.match(e) for e in emails):
            problems.append((cid, c.get("email")))
            continue
        warm = c.get("status") in ("replied", "covered")
        r = plan.get("reach", {}).get(cid) or reach(c.get("notes"))
        if c.get("kind") == "press" and r < 10_000:
            r = 99_999  # press goes out on launch day, right after the biggest channels
        tier = 0 if warm else 1 if r >= 100_000 else 2 if r >= 10_000 else 3
        rows.append({"id": cid, "name": c.get("name"), "to": emails[:1], "cc": emails[1:], "tier": tier, "reach": r,
                     "status": c.get("status"), "key": key, "early": bool(c.get("earlyKey")) or cid == "tw-digitaubrey",
                     "greet": greets.get(cid) or first_name(c)})

    missing = [r["id"] for r in rows if r["tier"] == 0 and r["id"] not in personal]
    rows = [r for r in rows if r["id"] not in missing]
    seen, out = set(), []
    for r in sorted(rows, key=lambda r: (r["tier"], -r["reach"], r["id"])):
        if r["to"][0].lower() in seen:  # one email per address
            continue
        seen.add(r["to"][0].lower())
        out.append(r)

    n = {1: 0, 2: 0}
    for r in out:
        r["day"] = 1 if r["tier"] <= 2 else 2
        r["batch"] = n[r["day"]] // a.per_hour + 1
        n[r["day"]] += 1
        if r["tier"] == 0:
            n_ = personal[r["id"]]
            r.update(personal=True, greet=n_.get("greet", r["greet"]), subject=n_.get("subject") or "Engagement is out today on Steam")
            if n_.get("to"):
                r["to"], r["cc"] = [n_["to"]], []
            if n_.get("thread"):
                r["thread"] = n_["thread"]
            r["body"] = f"Hi {r['greet']},\n\n" + n_["body"].replace("{KEY}", r["key"]).replace("{STORE}", STORE).replace("{DISC}", disc)
            assert "{" not in r["body"] and "\u2014" not in r["body"] and "\u2013" not in r["body"], r["id"]
            continue
        r["subject"] = "Engagement is out today on Steam (your key inside)" if r["day"] == 1 else "Engagement is out now on Steam (your key inside)"
        r["body"] = body(r["greet"], r["key"], r["early"], r["day"], wishlists, a.discount)
        assert "\u2014" not in r["body"] and "\u2013" not in r["body"]

    json.dump(out, open(a.out, "w"), indent=1, ensure_ascii=False)
    print(f"queue: {len(out)} people | launch day {n[1]} in {-(-n[1] // a.per_hour)} hourly batches | day after {n[2]} in {-(-n[2] // a.per_hour)}")
    for t, label in ((0, "replied or covered (personal notes)"), (1, "100K and up"), (2, "10K to 100K"), (3, "under 10K or unknown")):
        print(f"  tier {t}: {sum(1 for r in out if r['tier'] == t):4}  {label}")
    if problems:
        print("skipped, bad address:", problems)
    if missing:
        print("LEFT OUT, replied or covered but no personal note in the plan:", missing)


if __name__ == "__main__":
    main()
