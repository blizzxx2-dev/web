#!/usr/bin/env python3
"""Builds the follow-up queue for people who got the launch email and stayed quiet.

  python3 followup_queue.py --queue queue.json --contacts EXPORT_DIR --threads threads.json
                            --out followup.json [--plan plan.json] [--replied replied.json]
                            [--per-hour 40]

  queue.json    the launch queue from launch_queue.py (who was written to, with which key)
  EXPORT_DIR    a fresh export of the tracker's contacts, one JSON file per contact
  threads.json  {address: Gmail thread id of the launch email}, so the follow-up
                lands under it as a reply
  replied.json  [addresses that have written back since launch], from a Gmail search
  plan.json     the private launch plan; its "skip" and "reach" entries are used

Left out: people who got a hand-written launch note (they replied or covered
before launch), anyone the tracker now shows as replied, covered, passed,
bounced or on hold, anyone whose launch email did not go out or has no thread,
and every address in replied.json. Order: biggest audience first, press right
after the 100K channels.

Nothing is sent from here. The output holds keys, so it is written outside the
repo. It is {"subject", "body", "rows"}: Claude fills {GREET}, {KEY} and
{REVIEWS} in the body for each row when it sends. {REVIEWS} is the review line
as Steam shows it at send time, for example "87% of its Steam reviews are
positive" or "its Steam reviews are Very Positive".
"""
import argparse, json, os

from launch_queue import SKIP, reach

STORE = "https://store.steampowered.com/app/5195200/?utm_source=creator&utm_medium=email&utm_campaign=launch_followup&utm_content=engagement"
SUBJECT = "Re: Engagement is out today on Steam (your key inside)"
BODY = "\n".join([
    "Hi {GREET},", "",
    "A quick follow-up on Engagement in case my launch email got buried. It came out on Thursday, "
    "made the New & Trending list on Steam's front page on launch day, and {REVIEWS}.", "",
    "Your key still works and unlocks the full game: {KEY}", "",
    "You command one capital ship against a growing swarm, bolting salvaged guns onto the hull and "
    "raising a fleet of escorts, solo or in co-op. The 20% launch discount runs through November 19, "
    "so this week is a good time to cover it if it's a fit for you.", "",
    f"Steam page: {STORE}", "",
    "If you need anything from me, just reply here.", "",
    "Thanks,", "Trevor", "TrevorGames", "blizzxx2@gmail.com",
])
QUIET = ("replied", "covered", "passed", "bounced")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--queue", required=True)
    ap.add_argument("--contacts", required=True)
    ap.add_argument("--threads", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--plan")
    ap.add_argument("--replied")
    ap.add_argument("--per-hour", type=int, default=40)
    a = ap.parse_args()
    plan = json.load(open(a.plan)) if a.plan else {}
    plan = plan.get("data", plan)
    skip = SKIP | set(plan.get("skip", []))
    threads = {k.lower(): v for k, v in json.load(open(a.threads)).items()}
    replied = {x.lower() for x in json.load(open(a.replied))} if a.replied else set()

    rows, why = [], {}
    for r in json.load(open(a.queue)):
        cid, to = r["id"], r["to"][0].lower()
        path = os.path.join(a.contacts, cid + ".json")
        c = json.load(open(path)) if os.path.exists(path) else {}
        c = c.get("data", c)
        reason = ("had a personal note" if r.get("tier") == 0 else
                  "skipped in the plan" if cid in skip else
                  "launch email not sent" if not c.get("launchSentAt") else
                  "now " + c["status"] if c.get("status") in QUIET else
                  "on hold" if c.get("hold") else
                  "wrote back" if to in replied or any(x.lower() in replied for x in r.get("cc", [])) else
                  "no launch thread" if to not in threads else None)
        if reason:
            why.setdefault(reason, []).append(cid)
            continue
        n = plan.get("reach", {}).get(cid) or reach(c.get("notes"))
        if c.get("kind") == "press" and n < 10_000:
            n = 99_999
        rows.append({"id": cid, "name": r.get("name"), "to": r["to"], "cc": r.get("cc", []), "greet": r["greet"],
                     "key": r["key"], "thread": threads[to], "reach": n, "kind": c.get("kind")})

    rows.sort(key=lambda r: (-r["reach"], r["id"]))
    for i, r in enumerate(rows):
        r["batch"] = i // a.per_hour + 1
    assert "—" not in BODY and "–" not in BODY
    json.dump({"subject": SUBJECT, "body": BODY, "rows": rows}, open(a.out, "w"), indent=1, ensure_ascii=False)
    print(f"follow-up queue: {len(rows)} people in {-(-len(rows) // a.per_hour)} hourly batches of {a.per_hour}")
    for reason, ids in sorted(why.items(), key=lambda kv: -len(kv[1])):
        print(f"  left out, {reason}: {len(ids)}" + ("  " + ", ".join(ids) if len(ids) <= 25 else ""))


if __name__ == "__main__":
    main()
