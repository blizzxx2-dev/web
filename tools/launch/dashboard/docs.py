#!/usr/bin/env python3
"""Writes the JSON documents the launch dashboard's store expects.

  python3 docs.py OUT_DIR id=/_blob/<asset id> [id=/_blob/...] [--page index.html]

One file per dataset named after its id, each pointing at an uploaded CSV, and
optionally the page itself. Claude then writes them to the dashboard in one
batch. Used for the first build and for every data refresh.
"""
import datetime as dt, json, os, sys

DATASETS = {
    "standing": ("Engagement rank on each Steam list", "Where Engagement sits on each Steam list at the latest check, with the move since the previous check and since about a day earlier.", "standing.csv", "Rewritten by Claude at every Steam check.", 12),
    "history": ("Steam checks over time", "One row per check of Steam's public store pages: followers and the rank on each list.", "history.csv", "One row added by Claude at every Steam check.", 12),
    "ahead": ("Games ahead of Engagement", "Every game above Engagement on each genre list at the latest check, with its release date.", "ahead.csv", "Rewritten by Claude at every Steam check.", 12),
    "wishlists": ("Wishlists reported from Steamworks", "Wishlist totals Trevor has read out from his Steamworks dashboard.", "wishlists.csv", "A row is added by Claude when Trevor shares a new Steamworks number.", 72),
    "coverage": ("Coverage of Engagement", "Articles and videos that feature the game.", "coverage.csv", "Refreshed by Claude when it scans for coverage.", 72),
}


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    edit = {"via": "claude", "at": now}
    args = sys.argv[2:]
    if "--page" in args:
        page = args[args.index("--page") + 1]
        args = [a for a in args if a not in ("--page", page)]
        json.dump({"text": open(page).read(), "edit": edit}, open(os.path.join(out, "index.html.json"), "w"))
        json.dump({"title": "Engagement Launch Control", "lang": "en"}, open(os.path.join(out, "meta.json"), "w"))
    for a in args:
        ds, url = a.split("=", 1)
        title, desc, name, schedule, stale = DATASETS[ds]
        by = "Trevor, entered by Claude" if ds == "wishlists" else "Claude, from public Steam and YouTube pages"
        json.dump({"title": title, "description": desc, "source": {"kind": "file", "url": url, "name": name, "format": "csv"},
                   "updated": {"at": now, "by": by}, "schedule": schedule, "staleAfterHours": stale, "edit": edit},
                  open(os.path.join(out, ds + ".json"), "w"), indent=1)
    print("docs written to", out, "at", now)


if __name__ == "__main__":
    main()
