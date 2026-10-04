# TrevorGames website

Static site for TrevorGames, served by GitHub Pages at https://blizzxx2-dev.github.io/web/.

Plain HTML, one CSS file, one JS file and self-hosted fonts. No build step is needed to serve it, and every
internal link is relative.

- `index.html`, `games/<game>/`, `press/`, `404.html`: the pages
- `assets/`: CSS, JS, fonts, icons, images and press-kit files
- `engagement/`, `fight/`, `street-takeover/`, `field-surgeon/`, `trevorgames/`: clips and images the pages play
- `tools/site/`: authoring scripts. `python3 tools/site/build.py` regenerates the pages, and
  `python3 tools/site/linkcheck.py` must print `PROBLEMS: 0`.

## Moving to a custom domain

Change `BASE` in `tools/site/build.py` to `https://<domain>/`, run the build, add a `CNAME` file containing the
domain, and set the domain under Settings > Pages.
