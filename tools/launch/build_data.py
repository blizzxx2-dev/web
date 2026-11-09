#!/usr/bin/env python3
"""Turn steamwatch output into the CSV files the launch dashboard reads.

  python3 build_data.py --dir DIR

Reads DIR/history.jsonl and DIR/latest.json (written by steamwatch.py) and
writes DIR/pub/standing.csv, history.csv and ahead.csv.

  python3 build_data.py --dir DIR --restore history.csv

rebuilds history.jsonl from a history.csv downloaded from the dashboard, for
when the local history file is gone.
"""
import argparse, csv, datetime as dt, json, os

KEYS = [("bullet_heaven", "Bullet Heaven"), ("flight", "Flight"), ("space", "Space"), ("local_coop", "Local Co-Op"),
        ("action_roguelike", "Action Roguelike"), ("coop", "Co-op"), ("roguelike", "Roguelike"), ("overall", "Overall")]
HIST_COLS = ["t", "phase", "followers"] + [k for k, _ in KEYS] + ["upcoming_tab", "new_tab", "reviews"] + \
            [k + s for k, _ in KEYS for s in ("_trend", "_sell")]


def load(path):
    out = []
    for line in open(path):
        line = line.strip()
        if line:
            out.append(json.loads(line))
    out.sort(key=lambda h: h["ms"])
    return out


def move(now, then):
    """(direction word, places moved). A smaller rank number is better, so it reads as 'Up'."""
    if now is None or then is None:
        return "", ""
    if now == then:
        return "No change", 0
    return ("Up" if now < then else "Down"), abs(then - now)


def restore(csv_path, out_path):
    with open(csv_path) as fh, open(out_path, "w") as out:
        for r in csv.DictReader(fh):
            d = {"t": r["t"], "ms": int(dt.datetime.strptime(r["t"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc).timestamp() * 1000)}
            for k, v in r.items():
                if k == "t" or v == "":
                    continue
                d[k] = v if k == "phase" else int(v)
            out.write(json.dumps(d) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--restore")
    a = ap.parse_args()
    hp = os.path.join(a.dir, "history.jsonl")
    if a.restore:
        restore(a.restore, hp)
        print("history.jsonl rebuilt from", a.restore)
        return
    hist = load(hp)
    latest = json.load(open(os.path.join(a.dir, "latest.json")))
    pub = os.path.join(a.dir, "pub")
    os.makedirs(pub, exist_ok=True)

    with open(os.path.join(pub, "history.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=HIST_COLS, extrasaction="ignore")
        w.writeheader()
        for h in hist:
            w.writerow({c: ("" if h.get(c) is None else h.get(c)) for c in HIST_COLS})

    cur = hist[-1]
    prev = hist[-2] if len(hist) > 1 else {}
    day = {}
    for h in hist[:-1]:
        if cur["ms"] - h["ms"] >= 20 * 3600 * 1000:
            day = h
    released = latest["phase"] == "released"
    with open(os.path.join(pub, "standing.csv"), "w", newline="") as fh:
        cols = ["list", "label", "rank", "total", "last_dir", "last_move", "day_dir", "day_move", "ahead", "leaving",
                "projected", "stays", "trending", "trending_total", "sellers"]
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for k, label in KEYS:
            e = latest["lists"].get(k, {})
            field = k + "_trend" if released else k
            now = cur.get(field)
            ld, lm = move(now, prev.get(field))
            dd, dm = move(now, day.get(field))
            stay = [r["name"] for r in e.get("stay_list", [])]
            more = (e.get("projected") or 1) - 1 - len(stay[:4])
            stays = "; ".join(stay[:4]) + (f" and {more} more" if more > 0 and stay else "")
            w.writerow({"list": k, "label": label, "rank": e.get("rank") or "", "total": e.get("total") or "",
                        "last_dir": ld, "last_move": lm, "day_dir": dd, "day_move": dm,
                        "ahead": e.get("ahead", ""), "leaving": e.get("leaving", ""), "projected": e.get("projected") or "",
                        "stays": stays if k != "overall" else "", "trending": e.get("trending") or "",
                        "trending_total": e.get("trending_total") or "", "sellers": e.get("sellers") or ""})

    with open(os.path.join(pub, "ahead.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["list", "label", "pos", "name", "release", "leaves", "followers"])
        for k, label in KEYS:
            for i, r in enumerate(latest["lists"].get(k, {}).get("ahead_list", []), 1):
                w.writerow([k, label, i, r["name"], r["rel"], "Leaves before your launch" if r.get("leaves") else "Stays ahead",
                            "" if r.get("followers") is None else r["followers"]])
    print("wrote", pub, "| history rows:", len(hist), "| latest:", cur["t"])


if __name__ == "__main__":
    main()
