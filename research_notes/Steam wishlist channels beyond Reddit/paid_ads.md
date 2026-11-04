# Paid Advertising for Steam Indie Games: CPW, CPC and Wishlist Conversion by Platform

Research note scope: about 19 tool calls. Many search results were SEO or vendor blogs (steampageanalyzer.com, gamosy.com, immutable.com, presskit.gg) that repeat each other. The only primary, dev-reported numbers I could verify are **Reddit-centric**. Meta, TikTok, Google/YouTube and X figures below are mostly vendor benchmarks without stated sources. A reddit mirror (redlib.ssps.io) was blocked by the session network, so the Feb 2025 r/gamedev "Reddit ads postmortem" thread could not be read directly.

## What cost-per-wishlist ranges do indie devs report on each platform (with dates, genres and budgets)?

### Takeaway
Verified dev postmortems (2024-2026) put **Reddit ads at about $1.10-$2.25 per wishlist**, with CPCs of $0.12-$0.50, on budgets of $925 to $7,000. Meta, TikTok, Google and X numbers come almost entirely from unsourced vendor benchmarks, and those benchmarks contradict each other by an order of magnitude.

### Cited Findings
**Reddit (primary dev data):**
- *This Grand Life 2* (solo dev Patrick Tang / Poking Water Games, life sim, article dated May 31, 2024). The campaign spent $4,365 on paid ads, mostly Reddit plus some Twitter and Facebook, and produced about 4,000 wishlist additions. Average CPW was about $1.10, ranging from $0.80 to $2.50 by ad group. The goal was to reach Steam's Popular Upcoming list, which the game hit at 5,228 total wishlists. — [Game World Observer](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study)
- Same case: Reddit CTR was generally above 0.8%, and about 1.5-2% on relevant game subreddits. The best subreddits were r/capitalismlab (5.8%), r/bigambitions (4.3%), r/cartelycoon (3.9%), r/softwareinc (3.3%) and r/tycoon (2.8%). — [Game World Observer](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study)
- Same case: CPC in non-English-speaking countries was about 60-70% of CPC in English-speaking countries. Mobile accounted for about 90% of tracked visits and 96% of tracked wishlists, and the dev recommends targeting mobile even for a PC-only game. — [Game World Observer](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study)
- *Danchi Days* (cozy adventure/RPG/visual-novel hybrid, planned price $15-20). The campaign ran on Reddit only from Dec 20, 2025 to Apr 7, 2026, spent $7,000, and produced 3,600-3,900 ad-attributed wishlists. That works out to $1.79-$1.94 CPW overall, or $1.70-$2.25 by month. — [Melodic Ambient newsletter](https://buttondown.com/melodicambient/archive/danchi-days-3600-wishlists-through-reddit-ads-was)
  - Monthly breakdown: CPC ran $0.12, $0.15, $0.14 and $0.19. CTR ran 0.43%, 1.21%, 0.82% and 1.64%. CPW ran $1.88, $1.70, $2.25 and $1.92. Monthly spend was about $620, $2,380, $1,830 and $2,105.
  - Top subreddits were r/CozyGamers, r/PixelArt, r/Undertale and r/OMORI. "Lowest cost" bidding beat cost cap.
- *Match Morphosis* (match-3 puzzle, Dec 2025, funded by a $1,000 Gimersia grant). The dev spent $925 on Reddit ads for about 600 tracked wishlists, roughly $1.50 CPW. CPC was $0.20-0.30, or $0.30-0.50 when targeting the US. CTR was 0.6-1%. 93% of Steam traffic came from mobile. — [ernesernesto blog, "How I Spend 1000$ On Reddit Ads"](https://ernesernesto.github.io/writes/howispend1000onredditads)
- Search snippets, not verified: one Reddit user called about $1 per wishlist a typical good Reddit result, and another dev reported about €2.50 per tracked wishlist from a combined Reddit and Instagram campaign. — surfaced via search; original threads not fetched

**Meta (Facebook/Instagram), vendor benchmarks only:**
- Immutable (2026) says Facebook/Instagram is the cheapest paid channel at $0.30-$3 CPW, rising past $10 with weak creative or a cold audience. It cites no named sources. — [Immutable](https://www.immutable.com/insights/how-much-does-a-steam-wishlist-cost)
- Presskit.gg says Facebook/Instagram ads typically cost $1-3 per wishlist, but calls them a bad investment for most devs. — [presskit.gg](https://presskit.gg/field-guides/how-to-build-steam-wishlist)
- Gamosy, a creator-marketing vendor, gives a much higher estimate: Facebook/Instagram at $0.50-2 CPC, 2-5% click-to-wishlist, and $10-100 CPW. It also estimates Reddit ads at $17-300 CPW. These figures conflict with every primary Reddit postmortem above. — [Gamosy](https://gamosy.com/blog/steam-wishlist-strategy)

**Google Ads / YouTube:**
- Immutable puts Google Ads at $25+ per wishlist (2026), saying gaming keywords compete with large non-gaming advertisers. It does not separate YouTube in-stream, Shorts or placement targeting. — [Immutable](https://www.immutable.com/insights/how-much-does-a-steam-wishlist-cost)
- Gamosy gives Google Ads at $25-167 CPW and a YouTube Shorts CPM of $5-12. Neither figure is sourced. — [Gamosy TikTok guide](https://gamosy.com/blog/tiktok-game-marketing)
- The Danchi Days dev planned a Google Ads comparison through an ad firm, but no results were published. — [Melodic Ambient](https://buttondown.com/melodicambient/archive/danchi-days-3600-wishlists-through-reddit-ads-was)

**X/Twitter:**
- This Grand Life 2 dev on X/Twitter: "terrible CTR and lower WL to TV [wishlist-to-visit] than Reddit when targeting the same audiences." No numbers were given. — [Game World Observer](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study)

**TikTok:** see the Spark Ads question below. No dev-reported TikTok in-feed CPW was found.

**Common rule of thumb:** a CPW of $1-2 is "healthy" and anything above $3 should be stopped or reworked. Steampageanalyzer attributes this to Chris Zukowski's paid-ads guidance and Patrick Tang's data, but I could not locate Zukowski's own statement. — [Steampageanalyzer](https://www.steampageanalyzer.com/blog/indie-game-marketing-metrics)

### Inferences
- Across three independent Reddit campaigns (2024-2026), CPW clusters tightly at about $1.1-2.2. That makes Reddit the best-documented baseline. Niche games with clearly matching subreddits (tycoon/sim, cozy) sit at the low end.
- Mobile placements dominate attributed wishlists on Reddit, at 90-96% in two separate cases.
- The vendor figures for Meta ($0.30-3) and Google ($25+) are plausible directionally but unverified. Gamosy's $17-300 Reddit CPW is contradicted by every primary datapoint, so that source should be discounted.

### Gaps
- No primary dev postmortem with Meta CPW for a Steam game (2023-2026) was found, and none with a survivors-like or roguelite genre on any platform.
- No primary data on YouTube in-stream, in-feed, Shorts or placement-targeting CPW.
- No primary X ads CPW numbers, only the qualitative "terrible CTR."
- The r/gamedev "Reddit ads postmortem: what I learned after 2..." thread (Feb 2025) could not be fetched because the mirror domain was blocked.

## How does Reddit ads CPW compare to TikTok, Meta, Google/YouTube and X?

### Takeaway
On the evidence available, Reddit is the best-documented channel at about $1-2 CPW. Meta is claimed (by vendors) to be equal or cheaper. Google search ads are reported as the worst at $25+. X performed worse than Reddit in the one head-to-head test found.

### Cited Findings
- Reddit: $1.10 average, $1.50 and $1.79-1.94 CPW in three campaigns. — [GWO](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study), [ernesernesto](https://ernesernesto.github.io/writes/howispend1000onredditads), [Melodic Ambient](https://buttondown.com/melodicambient/archive/danchi-days-3600-wishlists-through-reddit-ads-was)
- Meta at $0.30-3 versus Google Ads at $25+ (vendor, 2026). — [Immutable](https://www.immutable.com/insights/how-much-does-a-steam-wishlist-cost)
- X was worse than Reddit for the same audiences (qualitative). — [GWO](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study)

### Inferences
- **Best:** Reddit (documented) and possibly Meta (claimed). **Worst:** Google search ads, then X.
- TikTok in-feed and YouTube cannot be ranked from verified data.

### Gaps
- There is no single campaign that tested all platforms with the same creative and UTM setup.

## Do Spark Ads (boosting organic TikTok posts) outperform regular TikTok ads for games?

### Takeaway
Industry and vendor commentary consistently says that boosting already-performing organic posts (Spark Ads) is the only paid TikTok approach worth trying. No verified dev numbers back this up.

### Cited Findings
- Gamosy estimates "paid organic" (Spark-style boosting) at $1-4 CPM, 3-8% wishlist conversion and $1-10 CPW. It compares this with "traditional paid ads" at $5-15 CPM, 0.5-2% conversion and $25-300 CPW (also given as $25-167). Its budget tiers are $200/month → 200-1,000 wishlists, $500-1,000/month → 800-5,000, and $2,000-5,000/month → 3,000-15,000. It recommends $10-20/day per post for 3-5 days, scaling if CPC is under $0.50 and pausing if over $2. None of this is sourced, and the article's own math does not reconcile: $1-4 CPM at 3-8% conversion would imply roughly $0.03-0.13 CPW. The TikTok gaming CPM is given as $3-8. — [Gamosy](https://gamosy.com/blog/tiktok-game-marketing)
- Presskit.gg says paid TikTok is usually poor because the view → link → Steam → wishlist path is too long, with an exception for Spark Ads on content that already performs organically. — [presskit.gg TikTok guide](https://presskit.gg/field-guides/tiktok-indie-game-marketing)
- Organic TikTok data points from How To Market A Game and Game Developer:
  - One viral menu video took a game from 3,000 to 6,000 wishlists. — [howtomarketagame.com](https://howtomarketagame.com/2024/02/07/how-to-get-tiktok-influencers-to-cover-your-game-and-earn-millions-of-impressions/)
  - A Game Developer blog reports going "from 400 to 20,000 wishlists with 1 video." — [Game Developer](https://www.gamedeveloper.com/game-platforms/from-400-to-20-000-wishlists-with-1-video-how-tiktok-can-make-your-game-go-viral)
  - One video got about 571k views and about 2,900 wishlists, with many viewers searching Steam instead of clicking, which UTM tracking undercounts. — [The Game Marketer](https://www.thegamemarketer.com/insight-posts/tiktok-marketing-for-indie-games-turn-views-into-steam-wishlists)

### Inferences
- The consensus logic is that a Spark Ad only amplifies a hook already proven organically. TikTok's value appears to come mainly from virality, not from paid in-feed reach.
- Because TikTok viewers often search Steam rather than click, UTM-based CPW on TikTok will look worse than the true cost.

### Gaps
- No verified head-to-head Spark Ads versus non-Spark in-feed CPW for a Steam game was found.

## How small can a budget be (e.g. $50 to $500) and still produce useful signal or wishlists?

### Takeaway
A few hundred dollars at $10-40/day over 2-3 weeks gives enough data to calculate CPW. Meaningful wishlist volume (thousands) took $4k-7k in the documented Reddit cases.

### Cited Findings
- The Match Morphosis dev had a usable CPW signal ($2) by day 2, from about $20 of spend, 1,200 impressions, 20 clicks and 10 wishlists. Starting at $60/day was "too aggressive" for a small budget. The total spend of $925 yielded about 600 wishlists. Audiences saturated quickly, and Reddit ad review delayed campaigns over weekends. The dev says running ads over the holidays as a small dev was "a really big mistake." — [ernesernesto](https://ernesernesto.github.io/writes/howispend1000onredditads)
- One guide recommends $10-20/day over 2-3 weeks rather than a $200 burst. — [Steampageanalyzer $1k plan](https://www.steampageanalyzer.com/blog/indie-game-marketing-1000-budget)
- Danchi Days spent about $620 in its first month for 276 UTM wishlists. — [Melodic Ambient](https://buttondown.com/melodicambient/archive/danchi-days-3600-wishlists-through-reddit-ads-was)
- This Grand Life 2 needed $4,365 to add about 4,000 wishlists and reach Popular Upcoming. — [GWO](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study)
- Gamosy claims $200/month in TikTok Spark Ads yields 200-1,000 wishlists. This is unverified. — [Gamosy](https://gamosy.com/blog/tiktok-game-marketing)

### Inferences
- $50-500 is enough to test creative and targeting, and to read CTR and wishlist-to-visit ratio. It is not enough to move Steam algorithm thresholds.
- At about $1.5-2 CPW, a $500 budget buys roughly 250-330 wishlists.

### Gaps
- No platform-specific minimum spends for Meta or TikTok learning phases were sourced.

## What is the typical wishlist-to-purchase conversion rate, and does ad-driven traffic convert worse than organic?

### Takeaway
GameDiscoverCo's median first-week conversion is about 0.15x of wishlists, or about 0.10x for games priced over $10. One dev reports that Reddit-ad wishlists converted noticeably worse than other wishlists. A widely repeated claim that "ad wishlists convert worse" (Furnish Master) could not be verified.

### Cited Findings
- GameDiscoverCo (Nov 3, 2025) covers games with 25k+ wishlists. Median first-week sales were 0.15x wishlists, 0.10x for games priced over $10, and about 0.14x excluding NSFW titles. Results vary by an order of magnitude. The data shows no long-term decline in conversion, only that wishlists are getting harder to gather. — [GameDevReports summary of GameDiscoverCo](https://gamedevreports.substack.com/p/gamediscoverco-the-state-of-steam)
- An older GameDiscoverCo benchmark puts median first-month conversion at about 27% and first-week at about 22%. Date not verified, likely pre-2024. — [GameDevReports](https://gamedevreports.substack.com/p/gamediscoverco-conversion-benchmarks)
- The Danchi Days dev, in a post-launch edit, said Reddit-ad wishlist conversion was "quite low," lower than other wishlist types, and that Reddit ads are likely not worth it unless the game has a very focused niche. No exact rate was given. The dev's pre-launch projection assumed 10-15% conversion in the first year. — [Melodic Ambient](https://buttondown.com/melodicambient/archive/danchi-days-3600-wishlists-through-reddit-ads-was)
- Steampageanalyzer claims a "Furnish Master" postmortem showed ad wishlists converting worse than organic, and cites GameDiscoverCo for it. The GameDiscoverCo summary I fetched does not mention ads, and a search found no such postmortem, so treat the claim as unverified. — [Steampageanalyzer](https://www.steampageanalyzer.com/blog/indie-game-marketing-metrics)
- Break-even math attributed to GameDiscoverCo's Simon Carless: on a $15 game, about $8.50 net per sale is available for acquisition. At $1.10 CPW, roughly one in eight paid wishlists must convert just to break even. — via [Steampageanalyzer budget guide](https://www.steampageanalyzer.com/blog/indie-game-marketing-budget) (secondary)

### Inferences
- With median conversion of about 10-15% and ad wishlists possibly converting below that, a $1.5-2 CPW on a $10-20 game is roughly break-even or loss-making in direct sales. The case for ads rests on algorithmic visibility, such as Popular Upcoming and launch velocity, which is exactly how the This Grand Life 2 dev framed it.

### Gaps
- No quantified conversion rate for ad-sourced versus organic wishlists, on any platform, was found.

## What do Steam UTM analytics case studies show about ad traffic quality?

### Takeaway
UTM data shows that ad traffic is overwhelmingly mobile and undercounts true ad impact by about 20-30%. A wishlist-to-visit ratio of about 20% or more is used as the quality bar.

### Cited Findings
- Danchi Days used utm_source=redditad, with campaign and content tags for ad groups and A/B tests.
  - The KPI was wishlists ÷ total visits of 20% or more; ads below that were treated as weak or overexposed.
  - UTM undercounted Reddit wishlists by about 1.2-1.3x, with untracked "Reddit-attributed" wishlists at about 20-30% of UTM wishlists.
  - A 6-second, quick-cut 4:5 video converted better than the trailer but did not improve CPC.
  - — [Melodic Ambient](https://buttondown.com/melodicambient/archive/danchi-days-3600-wishlists-through-reddit-ads-was)
- Mobile shares of tracked traffic: This Grand Life 2 had 90% of visits and 96% of wishlists from mobile, and Match Morphosis had 93% of traffic from mobile. — [GWO](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study), [ernesernesto](https://ernesernesto.github.io/writes/howispend1000onredditads)
- This Grand Life 2: X traffic had a lower wishlist-to-visit ratio than Reddit for the same audiences. — [GWO](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study)
- Further reading: How To Market A Game's UTM walkthrough (2021) — [HTMAG](https://howtomarketagame.com/2021/04/14/how-to-use-steams-utm-feature-to-track-the-number-of-wishlists-and-sales-your-marketing-is-generating/); and the Steamworks UTM docs — [Steamworks](https://partner.steamgames.com/doc/marketing/utm_analytics)

### Inferences
- Mobile-heavy ad traffic means wishlists are added for later. That likely contributes to weaker purchase conversion than desktop and organic Steam traffic, though no source quantifies this.

### Gaps
- No UTM case study was found that compares wishlist-to-visit rates across Meta, TikTok and Google for one game.
