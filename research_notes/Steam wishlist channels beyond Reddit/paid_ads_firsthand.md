# First-hand developer results from paid ads on Meta, TikTok, YouTube/Google and X for Steam indie games, plus launch-week ads

Scope note: this pass only counts data where a developer or publisher reports its own spend and results. Vendor and agency claims are listed separately and labelled "VENDOR". Reddit (reddit.com) was blocked to the search and fetch tools in this pass, so r/gamedev, r/IndieDev and r/IndieGaming threads could not be read directly. First-hand data was found only where a developer had posted it off Reddit (Notion, WN Hub, Game World Observer, HowToMarketAGame).

The most important new primary source is the **Furnish Master** postmortem by solo developer Alex Blintsov (cozy decorating sim, Steam Early Access Feb 20 2024). It has campaign-level Meta, X and Reddit tables and a dated spending ledger. The second is the **Dead Weight** X-ads case study by Klukva Games (steampunk tactical roguelite, launched July 16 2026).

---

## 1. Developer-reported cost per wishlist for Meta (Facebook/Instagram) ads, 2023 to 2026

### Takeaway
One solid first-hand Meta dataset was found: Furnish Master, cozy decorating sim, Nov 2022 to Jan 2023. A broad "Designers & Builders, Global" Facebook ad set cost about **$0.43 per estimated wishlist**. A "Sims Tycoons, Top Countries" set cost about **$1.10 per wishlist**. The same developer's US-only Facebook campaign in July 2023 produced **0 UTM wishlists from 84 visits**, and he turned it off. Meta results were cheap but unstable over time, and nothing first-hand was found for 2024 to 2026.

### Cited Findings
**Furnish Master (Alex Blintsov; cozy decorating/interior sim; PC/Steam) — first-hand**
- First ads experiment table. Wishlists are the developer's estimate, calculated as Steam UTM wishlists × 1.7. Screenshots are dated 2023-01-31, and the ledger shows the spend ran Oct 2022 to Jan 2023. [Furnish Master first ads campaign experiment (Notion)](https://grizzly-trampoline-7e3.notion.site/86abdf371ea846f0a170c4f0b4548880); [spending ledger](https://docs.google.com/spreadsheets/d/1m_ontmd-FiBXBR-hCUIc99dm91c5ubYhzRxB6UgLWkA/)
  - **Facebook "Designers & Builders – Global"**: $518.68 spent, about 1,188 wishlists, 671,089 impressions, $0.03 CPC, 14,940 clicks, **about $0.43 per wishlist**.
  - **Facebook "Sims Tycoons – Top Countries"**: $273.05 spent, about 238 wishlists, 82,980 impressions, $0.13 CPC, 2,102 clicks, **about $1.10 per wishlist**.
  - For comparison, from the same table: **Reddit total** was $929.69 for about 836 wishlists (×2 multiplier, no per-campaign UTM), $0.09 CPC, 10,295 clicks, about $1.10 per wishlist. **Twitter US** was about $0.13 per wishlist and **Twitter Europe+Asia** about $0.34 (see section 4).
  - "All campaigns were launched in the range of $10 - $25 per day." The creative was a 30-second trailer cut. [Notion experiment page](https://grizzly-trampoline-7e3.notion.site/86abdf371ea846f0a170c4f0b4548880)
  - The developer's observations: "Click campaigns seemed more effective, especially on Reddit… Optimization for impressions is almost useless." He also says: do not change settings after launch, create a new campaign instead; link straight to Steam; and give each campaign its own UTM. [Notion experiment page](https://grizzly-trampoline-7e3.notion.site/86abdf371ea846f0a170c4f0b4548880)
  - Measurement: "turn the campaign on/off and observe the changes in partner.steampowered on the Wishes By Day chart. UTM shows significantly fewer values." [Notion experiment page](https://grizzly-trampoline-7e3.notion.site/86abdf371ea846f0a170c4f0b4548880)
- Demo push, July 2023. Facebook Ads gave "Pretty much the same result as Reddit. High CPI + very low wishlist conversion ratio. It was okay in November, but not now… Campaign was US only. UTM shows 84 visits with 0 wishlists." He turned it off. [Furnish Master Demo Marketing Results (Notion)](https://grizzly-trampoline-7e3.notion.site/c7847e9170d44780b9b411b3a40db4f8)
- Lifetime pre-release Meta spend was **$1,185.85** out of $7,905.78 total ad spend (my sum of the ledger rows). Meta spend was heaviest Nov to Dec 2022 ($387 and $423), then occasional small amounts through Oct 2023. [Spending ledger](https://docs.google.com/spreadsheets/d/1m_ontmd-FiBXBR-hCUIc99dm91c5ubYhzRxB6UgLWkA/)
- "Facebook group was giving 0 views, so I dropped it very quickly. All the wishlists from X and Meta came from ads." [Furnish Master EA 100k sales postmortem (Notion)](https://grizzly-trampoline-7e3.notion.site/Furnish-Master-EA-100k-sales-1a0e2a4b318d8014b4bbcc3f91389384)
- Secondary coverage says the developer found ad-sourced wishlists "converted into sales less effectively" than other wishlists. I did not find that exact sentence in the Notion text I read, so treat it as reported by the secondary sources. [GameDiscoverCo](https://newsletter.gamediscover.co/p/the-state-of-steam-wishlist-conversions); [Steam Page Analyzer (vendor summary)](https://www.steampageanalyzer.com/blog/indie-game-marketing-budget)
- Context: the game launched in EA with about 96,000 wishlists from 885,124 pre-release page visits (10.8% visit-to-wishlist). It grossed over $787k in its first 12 months. [Notion postmortem](https://grizzly-trampoline-7e3.notion.site/Furnish-Master-EA-100k-sales-1a0e2a4b318d8014b4bbcc3f91389384); [Game World Observer](https://gameworldobserver.com/2025/02/24/furnish-master-revenue-787k-sales-wishlists-alex-blintsov)

**Other first-hand or publisher mentions (no usable Meta CPW)**
- This Grand Life 2 (life sim, 2024) included some Facebook spend. The developer "didn't have time to properly experiment with a strategy that seemed to work for Facebook ads". No Facebook-specific numbers were reported. [Game World Observer](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study)
- Hooded Horse's Tim Bender (publisher, 2021) says Facebook interest targeting is unreliable for niche PC games and its game-interest list is short. He recommends custom and lookalike audiences, and cross-sections such as Kickstarter backers combined with genre interests. He gives no dollar figures. [GameDiscoverCo, June 2021](https://newsletter.gamediscover.co/p/can-paid-ads-for-pcconsole-games)
- Older: the This Means Warp postmortem (2021) put Facebook ads at "<$2 per wishlist on average I would say" and still listed Facebook among the channels that did not work for them. [HowToMarketAGame, 2021](https://howtomarketagame.com/2021/12/27/what-worked-in-2021/)
- Older: a 2021 itch.io forum poster said the Facebook ads conversion rate was "totally not worth it". [itch.io forum](https://itch.io/t/1329203/marketing-on-facebook-2021)
- Older: Creepy Mahjong (2022) posted "results of the promotion… through the use of Facebook and Google Ads", but the numbers are only in an embedded video, not the text. [itch.io](https://itch.io/t/2271451/from-0-to-full-time-indie-game-developer-in-1-year-week-07-low-budget-ads-results)

**VENDOR / secondary claims (not first-hand)**
- Immutable: Facebook/Instagram at roughly $0.30 to $3 per wishlist and Google Ads at $25 or more (2026). It also notes that in-app browsers rarely carry a Steam login, so UTM undercounts Meta wishlists. [Immutable](https://www.immutable.com/guides/steam-ads)
- Steam Page Analyzer: $1 to $2 per wishlist is "healthy"; stop above $3. [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/indie-game-marketing-metrics)

### Inferences
- Furnish Master's best Meta ad set (broad global interest audience, about $0.43 per estimated wishlist) was much cheaper than its "top countries" set (about $1.10). That fits the general pattern that global or low-CPM geographies lower CPW, though the wishlists come from cheaper regions. China and Southeast Asia were a large share of Furnish Master's wishlists.
- The same Meta setup degraded badly from Nov 2022 to July 2023. A single good test window should not be taken as a durable CPW.
- Every Furnish Master CPW depends on the developer's ×1.7 or ×2 uplift over UTM. On raw UTM counts the costs are roughly 1.7 to 2 times higher (about $0.73 and $1.87 per UTM wishlist for the two Facebook sets).

### Gaps
- I found no developer-reported Meta or Instagram CPW for 2024 to 2026 with spend, wishlists and targeting. Reddit threads, the likeliest place, could not be accessed.
- No first-hand Instagram-only (Reels) placement data was found, and no comparison of Advantage+ against manual targeting.

---

## 2. Developer-reported TikTok ad and Spark Ad results; Spark Ads vs regular TikTok ads

### Takeaway
**I found no first-hand developer report of paid TikTok or Spark Ad spend with resulting Steam wishlists.** The TikTok evidence with real numbers is all organic. All Spark Ads figures come from vendors, and they are inconsistent even within one vendor.

### Cited Findings
- Organic only: Mortal Rite (Round Toast Studios) reported over 120M TikTok views, 640k followers and over 60,000 Steam wishlists "without spending a single dollar on paid advertising". They estimated that only about "1 in every 2,000+ people who view a video" wishlists. [Game Developer](https://www.gamedeveloper.com/blogs/this-game-used-tiktok-to-get-120m-views-60k-steam-wishlists-)
- Green Man Gaming's Voyages of Nera case (co-op survival crafting, June 2025 Next Fest) is **VENDOR**. It used Google, TikTok, Reddit, X and Meta with an average CPM of $2.02, 12M impressions and 139k+ clicks. It reports 60k+ wishlists and 50k+ demo downloads for the whole Next Fest campaign, and says over 78% of page visits were attributed to the campaign. Spend, CPW and the per-platform split are not disclosed. [Green Man Gaming](https://www.greenmangaming.com/company/news-category/case-studies/case-study-treehousegames/)
- The 2022 HowToMarketAGame view (Chris Zukowski) recommends ads on "Facebook, Reddit, or Tiktok" and reports "1 wishlist per $1". This is a rule of thumb, not a TikTok-specific result. [HowToMarketAGame, 2022](https://howtomarketagame.com/2022/03/08/what-should-you-spend-money-on-if-you-have-a-small-marketing-budget/)

**VENDOR claims on TikTok and Spark Ads (not first-hand)**
- Gamosy suggests boosting organic winners with Spark Ads after 24 to 48 hours. One Gamosy page projects 200 to 1,000 wishlists at **$0.20 to $1.00** each from boosting 3 to 5 posts. Another Gamosy page claims **$1 to $10** per wishlist versus "$25-167" for traditional paid ads. The two ranges are inconsistent. [Gamosy TikTok playbook](https://gamosy.com/blog/tiktok-game-marketing); [Gamosy wishlist strategy](https://gamosy.com/blog/steam-wishlist-strategy)
- Presskit.gg: "for most indie games, no," because the funnel (view → bio → Steam → wishlist) is too long. It says Spark Ads on organically proven content "can extend existing success". [Presskit.gg](https://presskit.gg/field-guides/tiktok-indie-game-marketing)
- Trapplan: Spark Ads (boosting existing posts) "consistently beat" from-scratch ad uploads on cost, but no number is given. Steam "doesn't fire a pixel back to TikTok, so you can't optimize for wishlists directly"; it suggests correlating spend with the daily wishlist graph. [Trapplan](https://www.trapplan.com/es/blog/do-tiktok-ads-work-for-steam-wishlists)
- Metricus: indie TikTok campaigns at $500 to $2,000 per push, with wishlist conversion "sub-1% even on viral hits". [Metricus](https://metricusapp.com/blog/indie-game-distribution-user-acquisition-painpoints-2025-2026/)
- Phantom Cave (2026): paid TikTok or Reels boosting at $100 to $200 per amplified post. It claims organic TikTok reach "declined sharply since 2025". [Phantom Cave](https://phantomcave.com/blog/market-indie-game-2026/)

### Inferences
- With Mortal Rite's organic rate of about 1 wishlist per 2,000+ views, a paid TikTok view would need to cost very little to beat the $0.40 to $1.10 per wishlist seen on Meta, X and Reddit. TikTok CPMs were not reported first-hand, so this cannot be confirmed.
- The only defensible "Spark vs regular" claim is directional and comes from vendors: boosting a post that already performs organically is cheaper than a new ad creative. No developer has published an A/B test.

### Gaps
- No developer-reported TikTok Ads or Spark Ads spend, CPM, CPC or wishlist numbers were found, and no developer-run Spark vs in-feed comparison.

---

## 3. Developer-reported YouTube / Google Ads results (in-stream, Shorts, Demand Gen, placement targeting)

### Takeaway
**I found no first-hand developer report of YouTube or Google Ads results for a Steam game with spend and wishlists.** The only developer-reported Google Ads numbers found are for a 2019 mobile game, and they were unprofitable. Steam-specific Google CPW figures come only from vendors.

### Cited Findings
- Tents and Trees (mobile puzzle, 2019, **not Steam**): Google Ads (Google Play) cost €782 for about 2,600 to 3,009 installs. Facebook iOS cost €236.76 at €0.56 CPI. The developer concluded: "I tried 8 different sources, and none of them was profitable." [Game Developer, 2019](https://www.gamedeveloper.com/business/an-indie-game-developer-discovering-the-world-of-user-acquisition-and-advertising-with-numbers-)
- Creepy Mahjong (2022) reported Facebook plus Google Ads results only in a video; the text has no figures. [itch.io](https://itch.io/t/2271451/from-0-to-full-time-indie-game-developer-in-1-year-week-07-low-budget-ads-results)
- YouTube as an organic channel, not ads: Perelesoq's Russian-language trailer "got into recommendations and became a superb source of regular wishlists" (about 50k wishlists in the announcement month). [WN Hub](https://wnhub.io/news/stores-and-publishing/item-47233)
- Green Man Gaming's Voyages of Nera campaign (VENDOR) included Google, but gave no Google or YouTube breakdown. [Green Man Gaming](https://www.greenmangaming.com/company/news-category/case-studies/case-study-treehousegames/)

**VENDOR claims (not first-hand)**
- Immutable puts Google Ads at "$25+" per wishlist. [Immutable](https://www.immutable.com/guides/steam-ads)
- Gamosy gives "$25-167 on Google Ads". [Gamosy](https://gamosy.com/blog/steam-wishlist-strategy)

### Inferences
- The lack of any developer write-up, against several for Reddit, X and Meta, suggests few Steam indies run YouTube or Google Ads, or that those who do don't publish results. Vendor CPW estimates are far higher ($25+) than any first-hand social number in this pass. This supports keeping YouTube/Google as a low-priority test, though the claim is not verified.

### Gaps
- No first-hand data on YouTube in-stream, Shorts, Demand Gen, or placement targeting (for example, buying placements on specific gaming channels) for Steam games.

---

## 4. Developer-reported X/Twitter ad results with numbers

### Takeaway
X has the strongest first-hand data in this pass, and it contradicts older advice that "Twitter ads don't work".
- **Furnish Master** got **about $0.13 to $0.34 per estimated wishlist** in its first tests (Dec 2022 to Jan 2023), about **$0.30 per wishlist in the US** on a constant $10/day, and about **$0.10 to $0.15 in East Asia** (2023). X became the developer's main paid channel ($5,342 of $7,906).
- **Dead Weight** reports **about 14,000 UTM wishlists (about 23,800 estimated) from X**. Ad groups ran at **about $0.34 to $0.68 per UTM wishlist**, and at **$50 to $60 per day** it got 70 to 80 UTM wishlists a day at about $0.70 each (2024 to 2025).
- This Grand Life 2, by contrast, found X had "terrible CTR" compared with Reddit.

### Cited Findings
**Furnish Master (cozy decorating sim) — first-hand**
- First experiment. Wishlists are estimated as UTM × 1.7. [Notion experiment page](https://grizzly-trampoline-7e3.notion.site/86abdf371ea846f0a170c4f0b4548880)
  - **Twitter "US (After New Year)"**: $76.47 spent, about 557 wishlists, 140,876 impressions, $0.54 CPM, $0.07 CPC, 1,040 clicks, **about $0.13 per wishlist**.
  - **Twitter "Europe + Asia (Before New Year)"**: $308.63 spent, about 889 wishlists, 573,415 impressions, $0.53 CPM, $0.13 CPC, 2,368 clicks, **about $0.34 per wishlist**.
- Demo push, July 2023. He had "been maintaining a daily budget of $10 in US since March", raised it to $20/day in the US, and added another $20/day ad group for Japan, Korea, Malaysia and the Philippines. The promoted tweet produced **723 UTM wishlists**, and the developer estimates 1,200 to 1,700 actual. **US: $172 for about 400 to 500 wishlists (about $0.30 per wishlist)**. **East Asia: $120** for three times the clicks, about **$0.10 to $0.15 per wishlist**. Objective: Website Traffic. Total demo-week ad spend across platforms was $375. Wishlists went from about 42,000 to about 51,000 in a week, but that figure includes SimFest featuring and organic Reddit posts. [Demo Marketing Results (Notion)](https://grizzly-trampoline-7e3.notion.site/c7847e9170d44780b9b411b3a40db4f8)
- Creative and format tip, which he says he tested on three projects: promote a normal post with a video and the Steam link in the tweet text. Do not attach the link to the media as a website card, and do not use link shorteners: "If you attach a link to your media, you will see a very low visit-to-wishlist ratio." A later note says "They have banned doing it as of August 2025". Which practice X banned is ambiguous. [Demo Marketing Results](https://grizzly-trampoline-7e3.notion.site/c7847e9170d44780b9b411b3a40db4f8); [Experiment page](https://grizzly-trampoline-7e3.notion.site/86abdf371ea846f0a170c4f0b4548880)
- "Later I ran a Twitter campaign on an almost permanent basis. This not only gave new wishlists, but also offered some influencers and media the opportunity to notice the game." Also: "Twitter (X) did not give anything for free." [Notion postmortem](https://grizzly-trampoline-7e3.notion.site/Furnish-Master-EA-100k-sales-1a0e2a4b318d8014b4bbcc3f91389384)
- Ledger: total X spend was **$5,342.10**, Dec 2022 to Feb 2024 (my sum of the ledger rows). It ran at **$800/month in each of Dec 2023, Jan 2024 and Feb 2024**, the three months up to the Feb 20 2024 EA launch. [Spending ledger](https://docs.google.com/spreadsheets/d/1m_ontmd-FiBXBR-hCUIc99dm91c5ubYhzRxB6UgLWkA/)

**Dead Weight (Klukva Games; steampunk tactical roguelite; $12.99) — first-hand case study by founder Pavel Belchenko, published 26 Aug 2025**
- X brought "nearly 14,000" UTM wishlists. The studio estimates "actual wishes = UTM wishes x 1.5-2" and uses 1.7, which gives about 23,800 (the "25k" headline). Total wishlists were over 73,000 at the time. [WN Hub](https://wnhub.io/news/stores-and-publishing/item-48634)
- Ad groups: an RPG group (interests and keywords) got 730 UTM wishlists at "0.34". An adventure group (interests) got 609 at "0.41" and is also described as spending **$249.91**. A turn-based T1-geo group got 633 at "0.68". Top creatives cost "0.06" to "0.09" per UTM wishlist (AC2: 330, RglkDan5: 387); a weaker one cost "0.4" (Logo_love: 366). [WN Hub](https://wnhub.io/news/stores-and-publishing/item-48634)
  - **Unit error in the source:** the article writes "cents", but $249.91 ÷ 609 = $0.41, so these are **dollars per wishlist**.
- Recovery period 24.07 to 11.08 (2025): "daily project spending reached $50-60" and they "started to haul 70-80 wishlists via UTM at 0.7 cents each" (read as about $0.70). Nearly all came from T1 countries. [WN Hub](https://wnhub.io/news/stores-and-publishing/item-48634)
- Settings:
  - Objective "website traffic with a target cost of 0.12-0.18" (likely $ per click).
  - Audiences of 200k to 300k per group.
  - Targeting by "handles": "we throw them into Follower look-alikes as competitors". The handles are mostly 10k to 50k-follower relevant accounts, and are cleaned after launch.
  - 10 to 15 settings tested per month.
  - "if it works, don't touch it."
  - The same article says "Interests and keywords — not used, as they currently don't work", yet it labels two groups as interest or keyword groups. This is an internal inconsistency.

  [WN Hub](https://wnhub.io/news/stores-and-publishing/item-48634)
- Outcome: Dead Weight launched July 16 2026 at $12.99. Coverage cites 120,000 wishlists at launch. Steam shows 81% positive of 613 reviews. games-stats estimates revenue at about $200k (third-party, unverified). No sales attribution to X ads was published. [Noisy Pixel](https://noisypixel.net/dead-weight-steam-release-date-july-2026/); [Steam](https://store.steampowered.com/app/2646720/Dead_Weight/); [games-stats](https://games-stats.com/steam/game/dead-weight/)

**Contrary evidence**
- This Grand Life 2 (2024): Twitter "had terrible CTR and lower WL to TV [ratio] than Reddit when targeting the same audiences". [Game World Observer](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study)
- Chris Zukowski (2022): "don't do Twitter ads, they don't work". [HowToMarketAGame, 2022](https://howtomarketagame.com/2022/03/08/what-should-you-spend-money-on-if-you-have-a-small-marketing-budget/)

### Inferences
- Both X successes share three things: art-forward games with broad visual appeal, cheap or global geographies (East Asia and Europe for Furnish Master; global rotation for Dead Weight), and promoting a native post with the link in the text, optimized for traffic or clicks. Dead Weight's T1-only group cost more ($0.68 per UTM wishlist) than its global groups.
- Reported X costs ($0.10 to $0.70 per wishlist) are at or below the best Reddit numbers ($1.10 to $1.94) from the earlier pass. Both X results lean on 1.5 to 2× uplift multipliers the studios estimated themselves, and the US-only Furnish Master number (about $0.30 estimated) is the most comparable.
- Format may be a confound. This Grand Life 2's poor X result may reflect how its ads were built, given Furnish Master's finding that website-card ads convert very poorly. This was not verified.

### Gaps
- No first-hand X data for 2026, after the ambiguous "banned as of August 2025" format change. No X ad-to-sales attribution.

---

## 5. Ads during launch week pointed at a live game: cost per sale, and did it lift Steam visibility?

### Takeaway
**I found no developer-reported launch-week cost per sale for Meta, TikTok, YouTube or X.** Valve's own documentation says store-page traffic is **not** a visibility factor; only resulting purchases and player activity are. A Valve GDC 2025 talk said the same, and Chris Zukowski withdrew his earlier claim that Steam "likes external traffic". The plausible mechanism for launch ads is that they create extra sales, and sales and engagement feed placement. No developer data proving or quantifying this lift was found.

### Cited Findings
**Valve (primary)**
- "The traffic landing on your store page is not a factor in your Steam store visibility." More visitors "may result in additional sales", which can affect visibility, but "traffic alone doesn't matter." [Steamworks: Visibility on Steam](https://partner.steamgames.com/doc/marketing/visibility)
- New & Trending: a title may appear "if the title is doing well" and can be bumped "quickly if many other popular products are releasing at the same time". Top Sellers is by "sales rank". To "Can I pay for my game to show up to more customers?" the answer is "Nope." [Steamworks: Visibility on Steam](https://partner.steamgames.com/doc/marketing/visibility)
- At GDC 2025 a Valve presenter said, as paraphrased by Zukowski: "We sometimes read people on the internet saying external traffic is a factor. It just isn't true." The slides said "whenever there is a burst of customer interest, Steam's algorithms react to player interest quickly and automatically." Zukowski: "So I will stop saying that the Steam algorithm likes 'External traffic' because it doesn't". [HowToMarketAGame, Apr 2025](https://howtomarketagame.com/2025/04/14/what-i-heard-from-valve-at-gdc/)

**Developer launch and visibility data points**
- Furnish Master spent $800 on X in launch month (Feb 2024), and about $500 on ads in total after release. No launch cost per sale was reported. [Spending ledger](https://docs.google.com/spreadsheets/d/1m_ontmd-FiBXBR-hCUIc99dm91c5ubYhzRxB6UgLWkA/); [Notion postmortem](https://grizzly-trampoline-7e3.notion.site/Furnish-Master-EA-100k-sales-1a0e2a4b318d8014b4bbcc3f91389384)
- Furnish Master's developer believed the opposite of Valve. He timed the demo with SimFest and ads "because I knew that Steam might showcase my game more prominently during the fest if there was activity on my page". He was featured on the SimFest front page ("Upcoming"): 594,793 impressions, 3,863 visits, and an estimated 1,500 to 2,000 wishlists from SimFest. His advice: "Ads can help maintain organic Steam traffic, as many of Steam's algorithms use your page activity". This belief is contradicted by Valve's doc for traffic alone. [Demo Marketing Results](https://grizzly-trampoline-7e3.notion.site/c7847e9170d44780b9b411b3a40db4f8)
  - Inconsistency: the demo page gives a "Demo release date: 20th July 2023", while the main postmortem says the demo went to Steam "on August 27, 2023, during the SimFest event". [Notion postmortem](https://grizzly-trampoline-7e3.notion.site/Furnish-Master-EA-100k-sales-1a0e2a4b318d8014b4bbcc3f91389384)
- Bills Must Be Paid (incremental, launched July 29 2026): $200 in Reddit ads earned 19 tracked wishlists (about $10.50 each). The game spent one day in Popular New Releases. The developer said launching next to a big release cost "one fewer spot in Popular New Releases… Can't say anything about effects." [HowToMarketAGame, Aug 2026](https://howtomarketagame.com/2026/08/20/part-2-the-week-of-the-golden-age/)
- This Grand Life 2 bought about 4,000 pre-launch wishlists ($4,365) specifically "to receive the blessings of the Steam algorithm at launch by getting on Popular Upcoming". No post-launch sales or ad analysis was published. [Game World Observer](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study)
- Developer claims on X (June 2026) say Steam changed Popular Upcoming from chronological to algorithmic. One says "The lowest wishlist count on there right now is 80k," against about 6k to 7k before. If true, this undercuts the This Grand Life 2 strategy of buying about 5k wishlists to reach Popular Upcoming. These are unverified social posts. [RegisKillbin on X](https://x.com/RegisKillbin/status/2062679476547264568); [Ryan T. Brown on X](https://x.com/Toadsanime/status/2062823126564560911)
- Hooded Horse and GameDiscoverCo (2021): Carless says launch spend for visibility is reasonable, assuming some is recouped. His break-even math: a $30 game leaves about $17.25 (57.5% of price, after Steam's cut and refunds) to acquire a buyer, and a $15 game about $8.50. He estimates (unsourced) that about 90% of UTM clickers are not logged in. [GameDiscoverCo, June 2021](https://newsletter.gamediscover.co/p/can-paid-ads-for-pcconsole-games)

**VENDOR claims (not first-hand)**
- Second Stage: concentrate paid spend in the first 48 to 72 hours because New & Trending is driven by "sales velocity". [Second Stage Academy](https://secondstage.io/academy/steam-marketing/launch-week-steam)
- Immutable: the same budget in a quiet week yields higher CPW than when stacked with a demo or Next Fest. [Immutable](https://www.immutable.com/guides/steam-ads)
- SteamForecast: Steam under-reports paid-campaign wishlists by about 75% (its own benchmark). [SteamForecast](https://steamforecast.app/guides/steam-wishlist-conversion-rate)

### Inferences
- Valve's position implies that the useful metric for launch-week ads is **cost per purchase** (Steam UTM reports purchases as well as wishlists), not visits.
- Illustration only, not data: at Furnish Master-like costs of $0.30 to $0.45 per wishlist, and if paid wishlists converted at 10 to 25%, that is roughly $1.20 to $4.50 per sale-equivalent. That is well under Carless's $8.50 to $17.25 break-even. However, Furnish Master reported that ad wishlists convert worse, and launch-day buyers from ads are a different funnel. Do not cite this as a measured result.

### Gaps
- No first-hand launch-week Meta, TikTok, YouTube or X cost-per-purchase data. No developer A/B evidence that launch ads moved a game into or kept it in New & Trending or Popular New Releases.

---

## 6. Minimum useful daily budgets and test durations reported by developers

### Takeaway
Developers who report figures used **$10 to $25 per day per campaign** for tests (Furnish Master, all platforms) and **about $10/day on X as an always-on baseline**. They scaled to $20 to $40/day around a demo, and to about $26/day in the three months before launch. Dead Weight ran X at **$50 to $60/day** during a scale period. Kill decisions came after **a couple of days** when a campaign clearly failed. No developer-reported minimums were found for TikTok or YouTube.

### Cited Findings
- Furnish Master: "All campaigns were launched in the range of $10 - $25 per day" across Facebook, Twitter and Reddit. [Notion experiment page](https://grizzly-trampoline-7e3.notion.site/86abdf371ea846f0a170c4f0b4548880)
- Furnish Master, X: a constant $10/day in the US from March 2023; $20/day US plus $20/day East Asia during the demo push; about $800/month (about $26/day) Dec 2023 to Feb 2024. [Demo Marketing Results](https://grizzly-trampoline-7e3.notion.site/c7847e9170d44780b9b411b3a40db4f8); [Spending ledger](https://docs.google.com/spreadsheets/d/1m_ontmd-FiBXBR-hCUIc99dm91c5ubYhzRxB6UgLWkA/)
- Furnish Master: Reddit ads were dropped after "a couple of days" (465 clicks, 6 UTM wishlists) and the money moved to X. Facebook was switched off after poor US results. [Demo Marketing Results](https://grizzly-trampoline-7e3.notion.site/c7847e9170d44780b9b411b3a40db4f8)
- Dead Weight, X: $50 to $60/day over an 18-day window (24.07 to 11.08) gave 70 to 80 UTM wishlists a day. They test 10 to 15 settings a month with 200k to 300k-person audiences. [WN Hub](https://wnhub.io/news/stores-and-publishing/item-48634)
- Hooded Horse (Tim Bender): start a new campaign at about 20% of the intended daily spend, raise to about 25% after a couple of days, and check the Steam UTM report daily. [GameDiscoverCo, June 2021](https://newsletter.gamediscover.co/p/can-paid-ads-for-pcconsole-games)
- Chris Zukowski: start with "small amounts every day like $10 – $20," and increase only once ads are proven to produce wishlists. [HowToMarketAGame, 2022](https://howtomarketagame.com/2022/03/08/what-should-you-spend-money-on-if-you-have-a-small-marketing-budget/)
- Measurement practice from both first-hand X sources: multiply UTM wishlists by 1.5 to 2 to estimate the true total, or toggle campaigns on and off and watch Steamworks' "Wishes By Day". [WN Hub](https://wnhub.io/news/stores-and-publishing/item-48634); [Notion experiment page](https://grizzly-trampoline-7e3.notion.site/86abdf371ea846f0a170c4f0b4548880)
- Conflict on device targeting:
  - Furnish Master: "On Reddit, it's best to target only desktops… It works much better." [Notion experiment page](https://grizzly-trampoline-7e3.notion.site/86abdf371ea846f0a170c4f0b4548880)
  - This Grand Life 2: "Mobile accounted for 90% of tracked visits and 96% tracked wishlists across all ads." [Game World Observer](https://gameworldobserver.com/2024/05/31/paid-ads-steam-wishlists-this-grand-life-2-case-study)

### Inferences
- A $10 to $25/day test for about a week ($70 to $175 per platform) was enough for Furnish Master to separate a working setup (X) from a failing one (Reddit and Facebook in July 2023). At $0.30 to $1.10 per wishlist, that budget yields roughly 60 to 500 wishlists, enough to see in the daily graph.
- The on/off toggle method needs spend high enough to be visible above the game's organic daily baseline. Games with large organic baselines need bigger tests.

### Gaps
- No developer-reported minimum budgets or learning-phase durations for TikTok, Meta Advantage+ or YouTube/Demand Gen.
- No reports of how long Meta or TikTok "learning" took for Steam-traffic objectives.
- Reddit-hosted threads, likely the richest source for 2024 to 2026 small tests, were inaccessible in this pass.
