# TrevorGames website

Static site for TrevorGames, served by GitHub Pages at https://trevorgameshq.com/ (the domain is set by the `CNAME` file and in Settings > Pages; DNS is at GoDaddy).

Plain HTML, one CSS file, one JS file and self-hosted fonts. No build step is needed to serve it, and every
internal link is relative.

- `index.html`, `games/<game>/`, `press/`, `404.html`: the pages
- `assets/`: CSS, JS, fonts, icons, images and press-kit files
- `engagement/`, `fight/`, `street-takeover/`, `field-surgeon/`, `trevorgames/`: clips and images the pages play
- `tools/site/`: authoring scripts. `python3 tools/site/build.py` regenerates the pages, and
  `python3 tools/site/linkcheck.py` must print `PROBLEMS: 0`.

## Changing the domain

Change `BASE` in `tools/site/build.py`, run the build, update `CNAME`, and set the domain under Settings > Pages.
