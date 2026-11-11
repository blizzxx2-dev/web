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
3. Leave the old assets alone for a day (an open dashboard tab may still be
   reading them), then delete the ones no dataset points at.

If `history.jsonl` is lost, download the dashboard's `history.csv` and run
`python3 build_data.py --dir $D --restore history.csv`.

Wishlist numbers come from Trevor (Steamworks is private): add a row to
`wishlists.csv` and upload it the same way. Coverage: run `coverage.py`, look
at anything it prints as NEW before clearing its `new` flag in `known.json`.

## Launch-day emails (Thursday Nov 12, about 10am US Eastern)

`launch_queue.py` builds the "it's out, your key works" queue. Nothing is sent
by the script; Claude sends from the queue file with the Gmail tools.

Rules Trevor set: 40 emails an hour at most, no dashes, no website link, no
other games named, true claims only, nothing to Steam curators.

1. Do not send on the clock. First confirm Steam shows the game as released:
   `python3 -c "import steamwatch; print(steamwatch.app_state())"` must show
   `coming_soon: False`. Note `discount`: the 20% line goes in only if it is 20.
2. Fresh inputs, all into a scratch dir (never the repo, the queue holds keys):
   export the tracker's `contacts` collection (ArtifactData list with
   `out_dir`), and get document `launch/plan` from the same database (greeting
   names, the hand-written notes for people who replied or covered, skips).
3. `python3 launch_queue.py --contacts <dir>/contacts --plan <dir>/launch/plan.json
   --out <dir>/queue.json [--discount]` (the wishlist figure comes from the
   plan; Trevor set it to "10,000" on Nov 11. `--wishlists` overrides it.)
4. Check the inbox for new replies from the people with personal notes, and
   for anyone who asked to stop, before the first batch.
5. Send `day` 1, `batch` 1 first (personal notes go inside their old thread via
   `thread`; everyone else gets a new email with the queue's `subject`). One
   batch an hour. Day 2 batches go out the next morning.
6. After each batch: check for bounces (`from:mailer-daemon newer_than:1d`) and
   mark the batch in the tracker (`launchSentAt` on each contact).
