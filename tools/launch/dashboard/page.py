#!/usr/bin/env python3
"""Builds the launch dashboard's page (index.html) from one template.

  python3 page.py OUT_DIR

The eight list cards and the list picker are generated from LISTS so the page
and the data files always agree on list ids.
"""
import os, sys

LISTS = [("bullet_heaven", "Bullet Heaven"), ("flight", "Flight"), ("space", "Space"), ("local_coop", "Local Co-Op"),
         ("action_roguelike", "Action Roguelike"), ("coop", "Co-op"), ("roguelike", "Roguelike"), ("overall", "All of Steam")]

CARD = """      <article class="lc-card" id="card-{k}">
        <h3 class="lc-card-name">{label}</h3>
        <p class="lc-rank"><span class="lc-hash">#</span><span data-draw="rank" data-list="{k}" data-source="standing" data-field="rank" data-where="list={k}">—</span></p>
        <p class="lc-move"><span class="lc-arrow" aria-hidden="true"></span><span class="lc-sr" data-draw="daydir" data-list="{k}" data-source="standing" data-field="day_dir" data-where="list={k}">—</span> <span data-draw="daymove" data-list="{k}" data-source="standing" data-field="day_move" data-where="list={k}">—</span> since yesterday</p>
        <div class="lc-spark" data-draw="spark" data-list="{k}" data-source="history" data-field="{k}" role="img" aria-label="{label} rank at each check"></div>
        <p class="lc-proj">Expected by launch eve <b class="lc-projnum">#<span data-draw="proj" data-list="{k}" data-source="standing" data-field="projected" data-where="list={k}">—</span></b></p>
{stays}      </article>
"""
STAYS = """        <p class="lc-stays"><span class="lc-k">Stays ahead</span> <span data-draw="stays" data-list="{k}" data-source="standing" data-field="stays" data-where="list={k}">—</span></p>
"""

HTML = r"""<meta name="dash-one-writer">
<style>
  .lc { display: flex; flex-direction: column; gap: var(--cds-gap-xl); font-family: var(--font-anthropic-sans); color: var(--color-fg); font-size: var(--cds-font-size-body); }
  .lc-head { display: flex; flex-direction: column; gap: var(--cds-gap-sm); }
  .lc-eyebrow { margin: 0; font-size: var(--cds-font-size-caption); letter-spacing: .06em; text-transform: uppercase; color: var(--color-fg-muted); }
  .lc-title { margin: 0; font-family: var(--font-anthropic-serif); font-weight: 400; font-size: var(--cds-font-size-title); text-wrap: balance; }
  .lc-take { margin: 0; max-width: 62ch; line-height: 1.5; }
  .lc-take b { font-weight: var(--cds-font-weight-medium); }
  .lc-stamp { margin: 0; font-size: var(--cds-font-size-caption); color: var(--color-fg-muted); }
  .lc-sec { display: flex; flex-direction: column; gap: var(--cds-gap-md); min-width: 0; }
  .lc-h2 { margin: 0; font-size: var(--cds-font-size-heading); font-weight: var(--cds-font-weight-medium); text-wrap: balance; }
  .lc-note { margin: 0; max-width: 68ch; color: var(--color-fg-muted); line-height: 1.5; }
  .lc-k { font-size: var(--cds-font-size-caption); letter-spacing: .04em; text-transform: uppercase; color: var(--color-fg-muted); }
  .lc-sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

  .lc-tiles { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: var(--cds-gap-md); }
  .lc-tile { display: flex; flex-direction: column; gap: var(--cds-gap-xs); min-width: 0; padding: var(--cds-pad-lg); background: var(--color-panel); border: 1px solid var(--color-border-line); border-radius: var(--cds-radius); }
  .lc-tile p { margin: 0; }
  .lc-big { font-family: var(--font-anthropic-serif); font-weight: 400; font-size: 2.1rem; line-height: 1.1; font-variant-numeric: tabular-nums; }
  .lc-big.lc-word { font-size: 1.5rem; }
  .lc-sub { color: var(--color-fg-muted); font-size: var(--cds-font-size-caption); line-height: 1.45; }

  .lc-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: var(--cds-gap-md); }
  .lc-card { position: relative; display: flex; flex-direction: column; gap: var(--cds-gap-xs); min-width: 0; padding: var(--cds-pad-lg); border: 1px solid var(--color-border-line); border-radius: var(--cds-radius); }
  .lc-card p, .lc-card h3 { margin: 0; }
  .lc-card-name { font-size: var(--cds-font-size-body); font-weight: var(--cds-font-weight-medium); }
  .lc-rank { font-family: var(--font-anthropic-serif); font-size: 2.4rem; line-height: 1; font-variant-numeric: tabular-nums; }
  .lc-hash { color: var(--color-fg-muted); font-size: 1.4rem; margin-right: 1px; }
  .lc-move { font-size: var(--cds-font-size-caption); color: var(--color-fg-muted); font-variant-numeric: tabular-nums; }
  .lc-arrow::before { content: "\25CF"; margin-right: 4px; font-size: .7em; vertical-align: 1px; }
  .lc-card.is-up .lc-move { color: var(--color-ok); }
  .lc-card.is-up .lc-arrow::before { content: "\25B2"; }
  .lc-card.is-down .lc-move { color: var(--color-bad); }
  .lc-card.is-down .lc-arrow::before { content: "\25BC"; }
  .lc-spark { position: relative; min-height: 64px; }
  .lc-spark svg, .lc-chart svg { display: block; overflow: visible; }
  .lc-proj { font-size: var(--cds-font-size-caption); color: var(--color-fg-muted); }
  .lc-projnum { color: var(--color-fg); font-weight: var(--cds-font-weight-medium); font-size: var(--cds-font-size-body); font-variant-numeric: tabular-nums; }
  .lc-stays { font-size: var(--cds-font-size-caption); line-height: 1.45; overflow-wrap: anywhere; }

  .lc-pick { display: flex; align-items: center; gap: var(--cds-gap-sm); color: var(--color-fg-muted); font-size: var(--cds-font-size-caption); }
  .lc-scroll { overflow-x: auto; min-width: 0; }
  .lc-table { width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; }
  .lc-table th { text-align: left; font-weight: var(--cds-font-weight-medium); font-size: var(--cds-font-size-caption); letter-spacing: .04em; text-transform: uppercase; color: var(--color-fg-muted); padding: var(--cds-pad-xs) var(--cds-pad-sm); border-bottom: 1px solid var(--color-border-line); white-space: nowrap; }
  .lc-table td { padding: var(--cds-pad-sm); border-bottom: 1px solid var(--color-border-line); vertical-align: top; }
  .lc-table .lc-num { text-align: right; }
  .lc-table a { color: inherit; text-decoration: underline; text-underline-offset: 2px; }
  .lc-table a:focus-visible, .lc select:focus-visible { outline: 2px solid var(--color-fg); outline-offset: 2px; }
  .lc-pill { display: inline-block; padding: 1px 8px; border-radius: 999px; border: 1px solid var(--color-border-line); font-size: var(--cds-font-size-caption); white-space: nowrap; }
  .lc-pill.is-leaving { color: var(--color-ok); }
  .lc-pill.is-staying { color: var(--color-warn); }
  .lc-chart { position: relative; min-height: 220px; }
  .lc-chart .tick text, .lc-spark .tick text { fill: var(--cds-text-secondary); font-size: var(--cds-font-size-caption); font-family: var(--font-anthropic-sans); }
  .lc-chart .domain { stroke: var(--cds-chart-axis); }
  .lc-chart .tick line { stroke: var(--cds-chart-grid); }
  .lc-tip { position: absolute; z-index: 2; pointer-events: none; transform: translate(-50%, -100%); padding: 4px 8px; white-space: nowrap; background: var(--cds-surface-popover); border: 1px solid var(--cds-border); border-radius: var(--cds-radius); box-shadow: var(--cds-shadow-popover); color: var(--color-fg); font-size: var(--cds-font-size-caption); font-variant-numeric: tabular-nums; }
  .lc-tip span { color: var(--cds-text-secondary); }
  .lc-two { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--cds-gap-xl); }
  .lc-two > * { min-width: 0; }
  .lc [data-dash-source-state=refreshing] { opacity: .5; }
</style>

<div class="lc">
  <header class="lc-head" id="top">
    <p class="lc-eyebrow">Launches Thursday, November 12 &middot; <span data-draw="countdown">—</span></p>
    <h1 class="lc-title">Engagement Launch Control</h1>
    <p class="lc-take" id="take-upcoming">Engagement is in the top 10 on <b><span data-draw="top10now" data-source="summary" data-field="top10_now" data-row="0">—</span> of 7</b> genre lists in Steam's Popular Upcoming right now. Once the games releasing before it drop off, it should be in the top 10 on <b><span data-draw="top10proj" data-source="summary" data-field="top10_proj" data-row="0">—</span> of 7</b> by launch eve.</p>
    <p class="lc-take" id="take-released" hidden>Engagement is out. It is on New &amp; Trending for <b><span data-draw="trendcount" data-source="summary" data-field="trending_lists" data-row="0">—</span> of 7</b> genre lists and has <b><span data-draw="reviews" data-source="latest" data-field="reviews" data-row="0">—</span></b> Steam reviews.</p>
    <p class="lc-stamp">Steam last checked <span data-draw="checked" data-source="latest" data-field="t" data-row="0">—</span>. Ranks come from Steam's public store pages.</p>
  </header>

  <section class="lc-tiles" id="tiles">
    <div class="lc-tile" id="tile-followers">
      <p class="lc-k">Steam followers</p>
      <p class="lc-big" data-draw="followers" data-source="latest" data-field="followers" data-row="0">—</p>
      <p class="lc-sub"><span data-draw="fday" data-source="latest" data-field="followers_day" data-row="0">—</span> gained since yesterday</p>
    </div>
    <div class="lc-tile" id="tile-wishlists">
      <p class="lc-k">Wishlists, after deletions</p>
      <p class="lc-big" data-draw="wlnet" data-source="wl_latest" data-field="net" data-row="0">—</p>
      <p class="lc-sub"><span data-draw="wltotal" data-source="wl_latest" data-field="total_added" data-row="0">—</span> added in total. From Steamworks, as of <span data-draw="wlwhen" data-source="wl_latest" data-field="when" data-row="0">—</span>. Tell Claude a new number to update it.</p>
    </div>
    <div class="lc-tile" id="tile-front">
      <p class="lc-k">Steam front page, Popular Upcoming</p>
      <p class="lc-big lc-word" data-draw="fronttab" data-source="latest" data-field="upcoming_tab" data-row="0">—</p>
      <p class="lc-sub">That tab holds the top 30 upcoming games on all of Steam. After launch this tile matters less than Popular New Releases, which goes by first-day sales.</p>
    </div>
  </section>

  <section class="lc-sec" id="lists">
    <h2 class="lc-h2">Popular Upcoming rank on each list</h2>
    <p class="lc-note">The big number is the rank now. A game leaves these lists the day it releases, so "expected by launch eve" counts only the games that release on or after November 12 and are ahead today.</p>
    <div class="lc-cards">
%%CARDS%%    </div>
  </section>

  <section class="lc-sec" id="ahead">
    <h2 class="lc-h2">Who is ahead of you</h2>
    <label class="lc-pick" for="ahead-list">List
      <select class="dash-select" id="ahead-list" aria-label="List">
%%OPTIONS%%      </select>
    </label>
    <div class="lc-scroll">
      <table class="lc-table" data-source="ahead" data-row-key="list,pos">
        <thead><tr><th data-field="pos">#</th><th data-field="name">Game</th><th data-field="release">Releases</th><th data-field="leaves">By your launch</th><th data-field="followers" class="lc-num">Followers</th></tr></thead>
        <tbody data-draw="aheadrows"></tbody>
      </table>
    </div>
    <p class="lc-note">Follower counts are looked up only for the games that stay ahead.</p>
  </section>

  <section class="lc-sec" id="released" hidden>
    <h2 class="lc-h2">After launch: New &amp; Trending and Top Sellers</h2>
    <p class="lc-note">Rank on each list's New &amp; Trending and Top Sellers. A dash means Engagement is not on that list yet. New &amp; Trending is short: only a handful of games per genre make it.</p>
    <div class="lc-scroll">
      <table class="lc-table" data-source="standing" data-row-key="list">
        <thead><tr><th data-field="label">List</th><th data-field="trending" class="lc-num">New &amp; Trending</th><th data-field="sellers" class="lc-num">Top Sellers</th></tr></thead>
        <tbody data-draw="relrows"></tbody>
      </table>
    </div>
  </section>

  <section class="lc-sec" id="growth">
    <h2 class="lc-h2">Followers and wishlists</h2>
    <div class="lc-two">
      <div class="lc-sec">
        <p class="lc-note">Steam followers at each check. Followers are public, so they stand in for wishlists between your Steamworks readings.</p>
        <div class="lc-chart" data-draw="followchart" data-source="history" data-field="followers" role="img" aria-label="Steam followers at each check"></div>
      </div>
      <div class="lc-sec">
        <p class="lc-note">Wishlist numbers you have reported from Steamworks.</p>
        <div class="lc-scroll">
          <table class="lc-table" data-source="wishlists" data-row-key="when">
            <thead><tr><th data-field="when">When</th><th data-field="net" class="lc-num">After deletions</th><th data-field="total_added" class="lc-num">Added in total</th><th data-field="source">Source</th></tr></thead>
            <tbody data-draw="wlrows"></tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <section class="lc-sec" id="coverage">
    <h2 class="lc-h2">Coverage so far</h2>
    <p class="lc-note">Articles and videos that feature Engagement. Views are read from each channel's public video list.</p>
    <div class="lc-scroll">
      <table class="lc-table" data-source="coverage" data-row-key="url">
        <thead><tr><th data-field="date">Date</th><th data-field="outlet">Who</th><th data-field="title">What</th><th data-field="kind">Type</th><th data-field="views" class="lc-num">Views</th></tr></thead>
        <tbody data-draw="covrows"></tbody>
      </table>
    </div>
  </section>
</div>

<script>
  const LAUNCH_DAY = new Date(2026, 10, 12); // November 12, 2026, the release date Trevor set
  const GENRE_LISTS = 7;
  const has = (v) => v !== null && v !== undefined && v !== '';
  const num = (v) => (has(v) && !isNaN(+v) ? +v : null);
  const fmtInt = d3.format(',');
  const fmtWhen = d3.timeFormat('%b %-d, %-I:%M %p');
  const fmtDay = d3.utcFormat('%b %-d');
  const enc = (v) => String(v).replace(/[%,&=]/g, (c) => encodeURIComponent(c));

  dash.calc('latest', {
    inputs: ['history'],
    title: 'Latest Steam check',
    description: 'The newest check, with followers gained since the check closest to a day earlier.',
    fn: (history) => {
      const rows = history.map((r) => ({...r, ms: Date.parse(r.t)})).filter((r) => !isNaN(r.ms));
      if (!rows.length) return [];
      const cur = rows[rows.length - 1];
      let dayAgo = null;
      for (const r of rows) if (cur.ms - r.ms >= 20 * 3600e3 && r.followers !== null && r.followers !== '' && r.followers !== undefined) dayAgo = r;
      const n = (v) => (v === null || v === undefined || v === '' ? null : +v);
      return [{t: cur.t, phase: cur.phase, followers: n(cur.followers), followers_day: dayAgo && n(cur.followers) !== null ? n(cur.followers) - n(dayAgo.followers) : null, upcoming_tab: n(cur.upcoming_tab), new_tab: n(cur.new_tab), reviews: n(cur.reviews)}];
    },
  });

  dash.calc('summary', {
    inputs: ['standing'],
    title: 'Top 10 count',
    description: 'How many of the 7 genre lists have Engagement in the top 10 now, how many should by launch eve, and how many New & Trending lists it is on.',
    fn: (standing) => {
      const genre = standing.filter((r) => r.list !== 'overall');
      const ok = (v) => v !== null && v !== undefined && v !== '';
      return [{
        top10_now: genre.filter((r) => ok(r.rank) && +r.rank <= 10).length,
        top10_proj: genre.filter((r) => ok(r.projected) && +r.projected <= 10).length,
        trending_lists: genre.filter((r) => ok(r.trending)).length,
      }];
    },
  });

  dash.calc('wl_latest', {
    inputs: ['wishlists'],
    title: 'Latest wishlist reading',
    description: 'The most recent wishlist numbers Trevor reported from Steamworks.',
    fn: (wishlists) => {
      const rows = wishlists.slice().sort((a, b) => Date.parse(a.when) - Date.parse(b.when));
      return rows.length ? [rows[rows.length - 1]] : [];
    },
  });

  const one = (id) => { const d = dash.data(id); return d.status === 'ok' && d.data && d.data.length ? d.data[0] : null; };
  const standingRow = (list) => { const d = dash.data('standing'); return d.status === 'ok' ? d.data.find((r) => r.list === list) : null; };
  const put = (el, text) => { el.textContent = has(text) ? text : '—'; };

  // Words and numbers
  dash.draw('countdown', (el) => {
    const days = Math.ceil((LAUNCH_DAY - Date.now()) / 864e5);
    el.textContent = days > 1 ? days + ' days to go' : days === 1 ? 'tomorrow' : days === 0 ? 'today' : 'out now';
  });
  dash.draw('checked', (el) => { const r = one('latest'); put(el, r ? fmtWhen(new Date(r.t)) : null); });
  dash.draw('top10now', (el) => { const r = one('summary'); put(el, r ? r.top10_now : null); });
  dash.draw('top10proj', (el) => { const r = one('summary'); put(el, r ? r.top10_proj : null); });
  dash.draw('trendcount', (el) => { const r = one('summary'); put(el, r ? r.trending_lists : null); });
  dash.draw('reviews', (el) => { const r = one('latest'); put(el, r && r.reviews !== null ? fmtInt(r.reviews) : null); });
  dash.draw('followers', (el) => { const r = one('latest'); put(el, r && r.followers !== null ? fmtInt(r.followers) : null); });
  dash.draw('fday', (el) => { const r = one('latest'); put(el, r && r.followers_day !== null ? fmtInt(r.followers_day) : null); });
  dash.draw('fronttab', (el) => { const r = one('latest'); put(el, r ? (r.upcoming_tab !== null ? '#' + r.upcoming_tab : 'Not on it yet') : null); });
  dash.draw('wlnet', (el) => { const r = one('wl_latest'); put(el, r && num(r.net) !== null ? fmtInt(num(r.net)) : null); });
  dash.draw('wltotal', (el) => { const r = one('wl_latest'); put(el, r && num(r.total_added) !== null ? fmtInt(num(r.total_added)) : null); });
  dash.draw('wlwhen', (el) => { const r = one('wl_latest'); put(el, r ? fmtWhen(new Date(r.when)) : null); });

  // List cards
  const cell = (field, fmt) => (el) => { const r = standingRow(el.dataset.list); const v = r ? r[field] : null; put(el, has(v) ? (fmt ? fmt(v) : v) : null); };
  dash.draw('rank', cell('rank', (v) => fmtInt(+v)));
  dash.draw('proj', cell('projected', (v) => fmtInt(+v)));
  dash.draw('daydir', cell('day_dir'));
  dash.draw('daymove', cell('day_move', (v) => fmtInt(+v)));
  dash.draw('stays', (el) => { const r = standingRow(el.dataset.list); put(el, r ? (has(r.stays) ? r.stays : 'Nobody. You would be #1.') : null); });

  // Charts share one tooltip helper. The tooltip lives inside the chart's own box.
  function hover(el, svg, pts, x, y, label, w, h) {
    const tip = d3.select(el).append('div').attr('class', 'lc-tip').property('hidden', true);
    const dot = svg.append('circle').attr('r', 4).style('fill', 'var(--color-bg)').style('stroke', dash.colors[0]).style('stroke-width', 2).style('display', 'none');
    const bis = d3.bisector((p) => p.t).center;
    const show = (ev) => {
      const box = svg.node().getBoundingClientRect();
      const px = (ev.clientX - box.left) * (w / (box.width || w));
      const p = pts[bis(pts, x.invert(px))];
      if (!p) return;
      dot.style('display', null).attr('cx', x(p.t)).attr('cy', y(p.v));
      tip.property('hidden', false).style('left', Math.min(Math.max(x(p.t), 70), Math.max(70, w - 70)) + 'px').style('top', Math.max(y(p.v) - 8, 26) + 'px');
      tip.node().replaceChildren(document.createTextNode(label(p) + ' '), Object.assign(document.createElement('span'), {textContent: fmtWhen(p.t)}));
    };
    svg.append('rect').attr('width', w).attr('height', h).style('fill', 'transparent')
      .on('pointermove', show).on('pointerdown', show)
      .on('pointerleave', () => { tip.property('hidden', true); dot.style('display', 'none'); });
  }
  const series = (key) => {
    const d = dash.data('history');
    if (d.status !== 'ok') return null;
    return d.data.map((r) => ({t: new Date(r.t), v: num(r[key])})).filter((p) => p.v !== null && !isNaN(p.t));
  };

  dash.draw('spark', (el) => {
    const pts = series(el.dataset.list);
    el.replaceChildren();
    if (!pts || pts.length < 2) { el.textContent = pts ? '' : '—'; return; }
    const w = Math.max(el.clientWidth, 160), h = 64, pad = 7;
    const x = d3.scaleTime().domain(d3.extent(pts, (p) => p.t)).range([pad, w - pad]);
    const lo = d3.min(pts, (p) => p.v), hi = d3.max(pts, (p) => p.v);
    const y = d3.scaleLinear().domain(lo === hi ? [lo - 1, hi + 1] : [lo, hi]).range([pad, h - pad]); // rank 1 is the top of the box
    const svg = d3.select(el).append('svg').attr('width', '100%').attr('height', h).attr('viewBox', `0 0 ${w} ${h}`);
    svg.append('line').attr('x1', pad).attr('x2', w - pad).attr('y1', h - 1).attr('y2', h - 1).style('stroke', 'var(--cds-chart-grid)');
    svg.append('path').attr('d', d3.line().x((p) => x(p.t)).y((p) => y(p.v))(pts)).style('fill', 'none').style('stroke', dash.colors[0]).style('stroke-width', 1.75).style('stroke-linejoin', 'round');
    const last = pts[pts.length - 1];
    svg.append('circle').attr('cx', x(last.t)).attr('cy', y(last.v)).attr('r', 3.5).style('fill', dash.colors[0]);
    hover(el, svg, pts, x, y, (p) => '#' + fmtInt(p.v), w, h);
  });

  dash.draw('followchart', (el) => {
    const pts = series('followers');
    el.replaceChildren();
    if (!pts || pts.length < 2) { el.textContent = pts ? 'Not enough checks yet.' : '—'; return; }
    const w = Math.max(el.clientWidth, 240), h = 220;
    const svg = d3.select(el).append('svg').attr('width', '100%').attr('height', h).attr('viewBox', `0 0 ${w} ${h}`);
    const lo = d3.min(pts, (p) => p.v), hi = d3.max(pts, (p) => p.v), room = Math.max(2, (hi - lo) * 0.12);
    const y = d3.scaleLinear().domain([lo - room, hi + room]).nice(4);
    const probe = svg.append('g').attr('class', 'tick').append('text').text(fmtInt(y.domain()[1]));
    const m = {t: 10, r: 14, b: 26, l: Math.ceil(probe.node().getComputedTextLength()) + 12};
    probe.node().parentNode.remove();
    y.range([h - m.b, m.t]);
    const x = d3.scaleTime().domain(d3.extent(pts, (p) => p.t)).range([m.l, w - m.r]);
    svg.append('g').attr('transform', `translate(${m.l},0)`).call(d3.axisLeft(y).ticks(4).tickFormat(fmtInt).tickSize(-(w - m.l - m.r))).call((g) => g.select('.domain').remove());
    svg.append('g').attr('transform', `translate(0,${h - m.b})`).call(d3.axisBottom(x).ticks(Math.max(2, Math.floor((w - m.l) / 120))).tickFormat(d3.timeFormat('%b %-d, %-I %p')).tickSize(4)).call((g) => g.selectAll('.tick line').style('stroke', 'var(--cds-chart-axis)'));
    svg.append('path').attr('d', d3.line().x((p) => x(p.t)).y((p) => y(p.v))(pts)).style('fill', 'none').style('stroke', dash.colors[0]).style('stroke-width', 2).style('stroke-linejoin', 'round');
    svg.append('g').selectAll('circle').data(pts).join('circle').attr('cx', (p) => x(p.t)).attr('cy', (p) => y(p.v)).attr('r', 2.5).style('fill', dash.colors[0]);
    hover(el, svg, pts, x, y, (p) => fmtInt(p.v) + ' followers', w, h);
  });

  // Tables. Cells are built with textContent so nothing in the data can run as markup.
  function fill(tbody, rows, key, cols) {
    tbody.replaceChildren(...rows.map((r) => {
      const tr = document.createElement('tr');
      tr.dataset.key = key(r);
      for (const c of cols) {
        const td = document.createElement('td');
        if (c.cls) td.className = c.cls;
        const v = c.node ? c.node(r) : (c.text ? c.text(r) : r[c.field]);
        if (v instanceof Node) td.append(v); else td.textContent = has(v) ? v : '—';
        tr.append(td);
      }
      return tr;
    }));
  }
  const rowsOf = (id) => { const d = dash.data(id); return d.status === 'ok' ? d.data : []; };
  const intCell = (field) => (r) => (num(r[field]) !== null ? fmtInt(num(r[field])) : null);

  dash.draw('aheadrows', (tbody) => {
    const pick = document.getElementById('ahead-list');
    const list = pick ? pick.value : 'bullet_heaven';
    fill(tbody, rowsOf('ahead').filter((r) => r.list === list), (r) => enc(r.list) + ',' + enc(r.pos), [
      {field: 'pos'}, {field: 'name'}, {field: 'release'},
      {node: (r) => Object.assign(document.createElement('span'), {className: 'lc-pill ' + (/^Leaves/.test(r.leaves) ? 'is-leaving' : 'is-staying'), textContent: /^Leaves/.test(r.leaves) ? 'Gone by then' : 'Still ahead'})},
      {text: intCell('followers'), cls: 'lc-num'},
    ]);
  });
  dash.draw('relrows', (tbody) => {
    fill(tbody, rowsOf('standing'), (r) => enc(r.list), [{field: 'label'}, {text: intCell('trending'), cls: 'lc-num'}, {text: intCell('sellers'), cls: 'lc-num'}]);
  });
  dash.draw('wlrows', (tbody) => {
    fill(tbody, rowsOf('wishlists').slice().sort((a, b) => Date.parse(b.when) - Date.parse(a.when)), (r) => enc(r.when), [
      {text: (r) => fmtWhen(new Date(r.when))}, {text: intCell('net'), cls: 'lc-num'}, {text: intCell('total_added'), cls: 'lc-num'}, {field: 'source'},
    ]);
  });
  dash.draw('covrows', (tbody) => {
    fill(tbody, rowsOf('coverage'), (r) => enc(r.url), [
      {text: (r) => (has(r.date) ? fmtDay(new Date(r.date)) : null)}, {field: 'outlet'},
      {node: (r) => (/^https:\/\//.test(r.url || '') ? Object.assign(document.createElement('a'), {href: r.url, target: '_blank', rel: 'noopener', textContent: r.title || r.url}) : document.createTextNode(r.title || '—'))},
      {field: 'kind'}, {text: intCell('views'), cls: 'lc-num'},
    ]);
  });

  // Outside the drawings: listen, and switch sections and card colors.
  document.querySelectorAll('#ahead-list').forEach((sel) => sel.addEventListener('change', () => dash.draw('aheadrows')));
  dash.onData(() => {
    const h = dash.data('history');
    const released = h.status === 'ok' && h.data.length > 0 && h.data[h.data.length - 1].phase === 'released';
    document.querySelectorAll('#take-upcoming, #lists, #ahead').forEach((el) => { el.hidden = released; });
    document.querySelectorAll('#take-released, #released').forEach((el) => { el.hidden = !released; });
    for (const r of rowsOf('standing')) {
      document.querySelectorAll('#card-' + r.list).forEach((card) => {
        card.classList.toggle('is-up', r.day_dir === 'Up');
        card.classList.toggle('is-down', r.day_dir === 'Down');
      });
    }
  });
</script>
"""


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    cards = "".join(CARD.format(k=k, label=label, stays=STAYS.format(k=k) if k != "overall" else "") for k, label in LISTS)
    options = "".join(f'        <option value="{k}">{label}</option>\n' for k, label in LISTS if k != "overall")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w") as fh:
        fh.write(HTML.replace("%%CARDS%%", cards).replace("%%OPTIONS%%", options))
    print("wrote", os.path.join(out, "index.html"))


if __name__ == "__main__":
    main()
