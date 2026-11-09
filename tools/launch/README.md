# Launch tools

Scripts Claude runs for the Engagement launch. They read public Steam and
YouTube pages only: no logins, no keys, nothing here is secret.

| Script | What it does |
|---|---|
| `steamwatch.py` | One Steam check: rank on every list, who is ahead and when they release, where the game should land by launch eve. After release: New & Trending, Top Sellers, reviews. Appends to `history.jsonl`. |
| `build_data.py` | Turns steamwatch output into the CSV files the dashboard reads. |
| `coverage.py` | Coverage radar: scans every contacted creator's channel and YouTube search for videos that name the game, and refreshes view counts. |
| `dashboard/page.py` | Builds the dashboard page. |
| `dashboard/docs.py` | Wraps uploaded CSVs (and the page) as the documents the dashboard stores. |

Dashboard: https://claude.ai/artifact/MsXvHzof9MKFwtx8tYNgz2 (private to Trevor).

## Refreshing the dashboard

Working files live outside the repo (pass `--out`/`--dir`), because they change
on every run.

    D=<scratch dir>
    python3 steamwatch.py --out $D            # about 25 seconds
    python3 build_data.py --dir $D            # writes $D/pub/*.csv

Then, with the Artifact tools:

1. Upload `standing.csv`, `history.csv` and `ahead.csv` from `$D/pub` as assets
   of the dashboard (one call each).
2. `python3 dashboard/docs.py $D/docs standing=/_blob/<id> history=/_blob/<id> ahead=/_blob/<id>`
   and write the three files to `datasets/<id>` in one batch.
3. Delete the three assets the datasets pointed at before.

If `history.jsonl` is lost, download the dashboard's `history.csv` and run
`python3 build_data.py --dir $D --restore history.csv`.

Wishlist numbers come from Trevor (Steamworks is private): add a row to
`wishlists.csv` and upload it the same way. Coverage: run `coverage.py`, look
at anything it prints as NEW before clearing its `new` flag in `known.json`.
