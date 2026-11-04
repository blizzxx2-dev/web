# Steam-native launch tactics beyond the basics (8 days before launch and the weeks after) for "Engagement"

Source labels used throughout: **[Valve]** = Steamworks documentation or Valve statement; **[Analyst]** = independent newsletter/analyst (GameDiscoverCo, How To Market A Game); **[Vendor]** = commercial tool or service blog with a stake in the topic (Steam Page Analyzer, Immutable, SteamData.ai, etc.); **[Developer-reported]** = a developer's own claim; **[Press]** = news coverage. Dates noted where known; pre-2023 sources are flagged "OLDER".

Headline finding for the report writer: **Valve's own visibility documentation says store-page traffic, store-page conversion rate, wishlists and review score are NOT factors in algorithmic visibility; players and purchases are.** So store-page optimisation only matters for turning visits into buyers, and the main levers for "more visibility after launch" are sales volume, language support, accurate tags, and Update Visibility Rounds. Almost none of the "store page change X lifts conversion by Y%" claims online come from controlled tests; they are vendor benchmarks without published sample sizes.

## Which store page changes have measured effects on visit-to-wishlist or visit-to-purchase conversion (with numbers)?

### Takeaway
No public controlled study (from Valve or anyone else) isolates the effect of a capsule, first screenshot, short description, tags or About-section GIF change on Steam conversion; the numbers available are vendor benchmarks without published sample sizes. The best-supported pieces are (a) Valve saying conversion rate does not feed the algorithm, (b) vendor benchmarks of roughly 8-15% visit-to-purchase in launch week and 2-5% at full price after it, and (c) a reported 2-3x conversion gap between "Overwhelmingly Positive" and "Mixed" review labels (vendor observation, not a controlled comparison).

### Cited Findings
**Valve statements on conversion and visibility**
- [Valve] "The traffic landing on your store page is **not a factor** in your Steam store visibility"; the conversion rate of store page visitors "is **not a factor** in visibility on Steam"; "wishlists are **not a factor** in your game's algorithmic visibility on Steam" (exception: Popular Upcoming). — [Steamworks: Visibility on Steam](https://partner.steamgames.com/doc/marketing/visibility)
- [Valve] "Steam will be more likely to show your game to players that speak a language supported by your game." This is one of the few store-page-level settings Valve says directly affects who sees the game. — [Steamworks: Visibility on Steam](https://partner.steamgames.com/doc/marketing/visibility)
- [Valve] A demo can show as a "Download Demo" button on the base game page, either as a subtle sidebar entry or "a more prominent green box in the center of the base game's store page"; after release "you need to manually re-publish the base game's store page for the Download Demo button to appear." — [Steamworks: Demos](https://partner.steamgames.com/doc/store/application/demos)

**Conversion benchmarks (vendor, no published sample size)**
- [Vendor] Steam Page Analyzer (March 2026) puts median visit-to-wishlist on Coming Soon pages at 8-12% (bands: <5% poor, 12-18% good, 18-25% excellent, >25% exceptional). Wishlist rates are said to be "1.5-2x higher" on Coming Soon pages than on live pages. It says the figures come from "aggregated Steamworks traffic screenshots shared by developers" plus its own reviews, with no n, and that Valve publishes no conversion rates. — [Steam Page Analyzer: conversion benchmarks](https://www.steampageanalyzer.com/blog/steam-store-page-conversion-benchmarks)
- [Vendor] Same source: visit-to-purchase medians of **8-15% in launch week**, 5-12% during a sale event, **2-5% at full price after launch**, 3-8% for an Early Access launch. Full-price bands: <1.5% poor, 3-5% average, 5-8% good, 8-12% excellent. — [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/steam-store-page-conversion-benchmarks)
- [Vendor] Same source, conversion by traffic source (no n): Direct 15-25% (highest), Steam Search 10-20%, External/social 8-15%, Curator 5-15%, Sale browsing 5-12%, Tag browsing 4-10%, **Discovery Queue 3-8% (lowest)**. — [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/steam-store-page-conversion-benchmarks)
- [Vendor] Same source: an "Overwhelmingly Positive" review label converts first-time visitors at **2-3x** the rate of "Mixed"; the vendor itself says this is an observation with "no controlled comparison, no sample size". It also claims a demo raises wishlist conversion "10-20%" (no basis given) and that $14.99-$19.99 "generally convert better" than $9.99 or below (no figures). — [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/steam-store-page-conversion-benchmarks)
- [Vendor] Same source uses capsule CTR below 2% as a diagnostic threshold for a capsule that is not earning clicks (no source stated) and warns that dividing visits by impressions "overstates click-through rate" because external traffic never sees a capsule impression. — [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/steam-store-page-conversion-benchmarks)

**Descriptive page-content data (vendor corpus, 2026; describes what pages do, not effects)**
- [Vendor] In a 405-page corpus (Feb-July 2026), median 9 screenshots (released pages 10), median 1 trailer (released pages 2), median short description 232 characters, median long description 4,404 characters. — [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/steam-store-page-conversion-benchmarks)
- [Vendor] In 220 self-selected analyzer reports (Feb-Sep 2026), 20.9% of first screenshots "did not communicate the game's core or hook"; 63.6% of pages lacked a UI/systems shot and 54.1% lacked a progression/payoff shot. — [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/steam-store-page-conversion-benchmarks)
- [Vendor] Of 764 public pages (Sep 2026), 78.4% used all 20 tags; 17.1% of first-five tag slots held a generic Steam genre word. — [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/steam-store-page-conversion-benchmarks)
- No source found gave a measured effect for GIFs in the About section.

**A/B testing**
- [Vendor] Several 2026 guides state Steam has no built-in store-page or capsule A/B test, and describe workarounds such as running two paid-ad sets with different capsule images and comparing CTR. One engineering blog summarising Valve Q&A notes mentions a Steamworks "artwork override" for short capsule/trailer tests that revert automatically; I could not confirm this in Valve docs. Sources conflict. — [Steam Page Analyzer: A/B testing](https://www.steampageanalyzer.com/blog/steam-page-ab-testing); [engineered.at: notes from Q&A sessions with Steam](https://engineered.at/articles/notes-from-the-q-a-sessions-with-steam)

**Wishlist-to-sale context (for sizing launch-week effects)**
- [Analyst] GameDiscoverCo data (2024-2025, via a newsletter summary): median first-week sales of **0.15x** wishlists for games with >25,000 wishlists (about 15,000 sales per 100,000 wishlists); median drops to **0.10x** for games priced above $10. — [gamedevreports summary of GameDiscoverCo](https://gamedevreports.substack.com/p/gamediscoverco-the-state-of-steam)

**Regional pricing (a conversion lever for non-US visitors)**
- [Vendor] Third-party estimates of Valve's recommended regional tiers: Brazil about 55% of the US price, China about 65%, Russia/CIS about 40%. These are estimates, not Valve-published figures. — [Steam Page Analyzer: regional pricing calculator](https://www.steampageanalyzer.com/tools/regional-pricing-calculator)
- [Vendor] Claims 30-40% of indie Steam revenue comes from outside the US and Western Europe, much of it enabled by regional pricing; no measured lift from a price cut is given. — [Steam Page Analyzer: regional pricing guide](https://www.steampageanalyzer.com/blog/steam-regional-pricing-guide)
- [Vendor/blog] Chinese buyers mostly use international Steam, and Steam sales reports may undercount Chinese players, which makes China unit effects hard to measure. — [Hooded Horse: How many Chinese players buy your game on Steam?](https://hoodedhorse.com/?p=1248)
- [Press] Valve has revised its regional price guides before, raising suggested prices in most regions outside the US (GamesRadar headline). — [GamesRadar](https://www.gamesradar.com/steams-new-regional-price-guides-make-games-more-expensive-pretty-much-everywhere-outside-the-us)

### Inferences
- Because Valve says conversion rate doesn't feed visibility, page changes in the last 8 days pay off only through more buyers per visit, mostly launch-day wishlist-email traffic and New Releases traffic. The highest-value fixes are the ones a launch-day visitor sees first: capsule, first 1-2 screenshots or trailer, short description, and the review label once it appears.
- The 2-3x gap between "Overwhelmingly Positive" and "Mixed" (even though it isn't a controlled figure) points the same way as Valve's <40% featuring penalty: protecting review score in week one matters more for conversion than any art tweak.
- Discovery Queue traffic converts worst (3-8% per vendor benchmarks). A launch-day spike in Discovery Queue impressions with low conversion is normal, not a sign the page is broken.
- Turning on the green-box "Download Demo" placement and republishing the base page after launch is a zero-cost Steam-native step that is easy to miss (see the demo section).
- For regional pricing, the defensible advice is to accept Valve's suggested regional prices (or close to them) and check the Steamworks regional sales report after 2 weeks. There is no public data on units gained.

### Gaps
- No controlled or Valve-published data on the conversion effect of changing capsule art, first screenshot, short description, tags or About-section GIFs. All numeric claims are vendor benchmarks without sample sizes.
- Whether Steamworks has a native capsule/artwork test ("artwork override") is unconfirmed; Valve docs were not located.
- No public data quantifying unit lift from regional pricing for a specific indie game.

## Does broadcasting on the store page during launch measurably help conversion?

### Takeaway
No measured evidence, from Valve or developers, shows that Steam Broadcasting on the store page raises conversion. Valve presents it as free and lists benefits based on "partner feedback". Developer reports are anecdotal: some see nothing, while others say its value is the chance of front-page placement when a stream ranks in the top viewer slots, which is most likely during launch or a sale when traffic is already high.

### Cited Findings
- [Valve] "Broadcast is a complimentary service and is available to all partners at no additional cost." "Streamed content shows up on the game's store page and on the Broadcast hub under the Community section." "If popular, the stream also gets featured on the Home Page." It "Automatically shows the 'Live' tag when applicable throughout the Steam store." — [Steamworks: Broadcasting](https://partner.steamgames.com/doc/store/broadcast)
- [Valve] Valve lists benefits (engaging the target audience, expanding the fan base, helping players explore the full game, generating excitement around updates) as coming from "partner feedback". The page makes no claim about conversion, sales or wishlists, and contains no metrics. Setup requires OBS or similar (or a multistream service such as Restream.io), and every performer's Steam account must be whitelisted per game. — [Steamworks: Broadcasting](https://partner.steamgames.com/doc/store/broadcast)
- [Developer-reported, OLDER 2019] Mike Rose (No More Robots) asked developers whether regular Steam streaming affected sales and said his own past streams "did not seem to do much". He also noted that reported positive effects usually coincide with launches, key dates or sales, which confounds them. — [WN Hub: Does streaming on Steam affect wishlisting?](https://wnhub.io/news/analytics/item-2439)
- [Developer-reported, OLDER 2019] Erik Johnson (Life Goes On: Done to Death): if a stream reaches the **top six** by viewers, the game can appear on Steam's front page, visibility that is otherwise hard to get. Gergo Vas (NeocoreGames PR): streams need to run **at least 4-5 hours** to have any effect. Some unnamed developers think streaming improves conversion rather than traffic. None of these claims comes with data. — [WN Hub](https://wnhub.io/news/analytics/item-2439)
- [Developer-reported, OLDER 2019] The general view in that piece: developers stream 24/7 around launches and updates, and streaming helps "at times you are likely to have high traffic" (publisher sales, launches). — [WN Hub](https://wnhub.io/news/analytics/item-2439)
- [Vendor] A live-streaming tool vendor argues that a 24/7 stream can help a page reach viewer thresholds for store placement. The vendor sells this service. — [LiveReacting blog](https://blog.livereacting.com/steam-24-7-live-streaming-game-visibility/)

### Inferences
- For a solo developer, the Steam-native case for broadcasting during launch week is cheap insurance and a shot at front-page broadcast placement while concurrent traffic is highest, not a proven conversion booster. A looped gameplay or prerecorded stream running through launch week costs little beyond setup; a live developer stream for the first hours after launch adds a human element, but there's no evidence on which works better.
- Launch week is the one period when the top-six viewer threshold is reachable for a small game, because many concurrent store visitors become broadcast viewers automatically. Starting the broadcast just before the release hour and running it 24/7 for the first days best fits the anecdotal mechanism.
- Moderate broadcast chat (Valve recommends this): a toxic or empty chat on the store page could plausibly hurt more than help.

### Gaps
- No Valve data on broadcast viewer thresholds for home-page featuring, and no developer A/B data (stream vs no stream) on conversion. The promised No More Robots random-day streaming test (2019) has no published result.
- Steamworks "Stats & Reporting" for broadcasts was not reviewed.

## What does launch hour/day matter for (e.g. 10am PT), and any data?

### Takeaway
The data is thin. Most Steam games launch between roughly 6am and 10am Pacific (GameDiscoverCo, OLDER 2021), and the common 10am PT recommendation rests on reasoning that Valve's systems and staff work on Pacific time, not on published outcome data. Releasing earlier in the Pacific morning (e.g., when based in Europe) may help capture Chinese buyers on day one. Avoiding major Steam sales, the opening of Next Fest, and weeks with huge releases matters more than the exact hour.

### Cited Findings
- [Analyst, OLDER 2021] GameDiscoverCo: "most games launched between 6am and 10am West Coast time" on Steam. Releasing even earlier (if based in Europe) "can be even better for getting Chinese sales on release day"; no figures given for this. — [GameDiscoverCo: What's the best timing to release your game?](https://newsletter.gamediscover.co/p/whats-the-best-timing-to-release)
- [Analyst, OLDER 2021] Same piece: avoid launching during major Steam sales (Summer/Winter), because you lose front-page boosts like "Popular New"; avoid the first days of a Next Fest if streamers will be swamped with demo requests; avoid the week of a massive title (the "Cyberpunk avoidance zone", when only two games with over 1,000 Steam followers launched). Fan interest and game quality matter more than the exact time of year. — [GameDiscoverCo](https://newsletter.gamediscover.co/p/whats-the-best-timing-to-release)
- [Vendor, April 2026] SteamData.ai recommends 10:00 AM Pacific on a Thursday, arguing that Steam's recommendation engine and editorial features run largely on Pacific time (the author's reasoning, not confirmed by Valve), and says Thursday accounts for roughly 40% of launches. — [SteamData.ai: Why Thursday 10am could make or break your Steam launch](https://steamdata.ai/blog/why-thursday-10am-could-make-or-break-your-steam-launch)
- [Vendor] Steam Page Analyzer argues Tuesday is the best launch day; its basis is less clear. Day-of-week advice conflicts across vendors. — [Steam Page Analyzer: best Steam launch dates](https://www.steampageanalyzer.com/blog/best-steam-launch-dates)
- [Valve] New & Trending: "Your title may be bumped off this list quickly if many other popular products are releasing at the same time." The New Releases queue prioritises "the titles that have the least amount of views since release." — [Steamworks: Visibility on Steam](https://partner.steamgames.com/doc/marketing/visibility)
- I found no Valve statement on how launch hour affects visibility.

### Inferences
- The launch hour matters mainly for (1) being awake and available for the first several hours, when bug reports, the first reviews and broadcast viewers peak; (2) the wishlist email arriving at a reasonable local time for the main audience (NA/EU); (3) being live during Valve's working hours in case a store-page or build problem needs support. Launching 9-10am PT gives EU evening and NA morning coverage. 6-8am PT trades some NA morning attention for more Asian daytime.
- The New Releases queue favours titles with the fewest views, so launching on a crowded day mostly costs New & Trending time ("bumped off quickly"), not queue slots. Checking SteamDB's upcoming list for the launch week, and avoiding days with several high-follower releases, is a free tactic.

### Gaps
- No hour-by-hour outcome data (first-day sales by launch hour) was found from Valve or analysts. How To Market A Game's 2023 "what's the best day to release" post was surfaced in search but not reviewed ([link](https://howtomarketagame.com/2023/02/14/whats-the-best-day-to-release-an-indie-game/)).

## Should the demo stay up after launch? Any data on demo removal vs keeping it?

### Takeaway
The only data-driven look (How To Market A Game, Feb 2026, correlational) found that keeping a demo up made no measurable difference to follower/wishlist growth for narrative games. Games with a demo still live had a higher average review score (89.83 vs 84.22), plausibly because players who wouldn't like the game try the demo instead of buying and leaving a negative review. Valve gives no direction on keeping or removing it, but supports a prominent "Download Demo" box on the base game page after launch. The default advice is to keep a good, well-received demo up and pull one that is costly to maintain or gives away too much.

### Cited Findings
- [Analyst, Feb 2026] How To Market A Game sampled Steam on Feb 1, 2026: **21%** of 2025 indie games with 1,000+ reviews had a demo live post-launch; 27% of hit narrative games and 30% of hit horror games; Souls-likes had the highest share, City Builders and Rhythm about 50%; no NSFW game had one. — [HTMAG: Should you keep your demo up post launch?](https://howtomarketagame.com/2026/02/02/should-you-keep-your-demo-up-post-launch/)
- [Analyst, Feb 2026] Same study: average daily follower increase for narrative games **with a demo 10.62 vs without 10.57**, so "no meaningful difference" (follower data from SteamDB, starting one month after launch). — [HTMAG](https://howtomarketagame.com/2026/02/02/should-you-keep-your-demo-up-post-launch/)
- [Analyst, Feb 2026] Same study: average review score for 1,000+ review games **with a demo live 89.83 vs 84.22 without**, a gap of more than 5.5 points (all genres; correlational, no controls). — [HTMAG](https://howtomarketagame.com/2026/02/02/should-you-keep-your-demo-up-post-launch/)
- [Developer-reported] Tomas Sala (The Falconeer, Bulwark) keeps demos up, reasoning that players who dislike the game try the demo, don't buy, and so don't leave negative reviews. Other developers remove demos because keeping them in sync with main-game patches is extra work. — [HTMAG](https://howtomarketagame.com/2026/02/02/should-you-keep-your-demo-up-post-launch/)
- [Analyst conclusion] Demos clearly help pre-launch (festivals, creators), but post-launch benefit is unclear. "Keep a demo up if it is good and well received"; remove it "without much visibility loss" if upkeep is heavy. — [HTMAG](https://howtomarketagame.com/2026/02/02/should-you-keep-your-demo-up-post-launch/)
- [Valve] Valve doesn't say whether to keep a demo indefinitely. "Deactivating a demo will prevent players from downloading or launching your demo"; players who already have it "will continue to see the demo." A deactivated demo may still run outside Steam unless it checks for a license. — [Steamworks: Demos](https://partner.steamgames.com/doc/store/application/demos)
- [Valve] Recommendations: use shared depots and shared Steam Cloud saves so demo progress carries over to the full game; disable achievements in the demo and grant them in the full game after purchase; "Steam currently doesn't support multiplayer matchmaking between the full game and the demo." — [Steamworks: Demos](https://partner.steamgames.com/doc/store/application/demos)
- [Valve] "Wishlist notifications have a two week cooldown per App ID." The demo-release wishlist notification can be sent once, within two weeks of the demo's first playable release; space it at least two weeks from other wishlist-triggering events such as discounts. — [Steamworks: Demos](https://partner.steamgames.com/doc/store/application/demos)
- [Vendor] Steam Page Analyzer and Wishlistlab lean toward keeping demos live post-launch (new visitors can try before buying; it keeps a channel open for streamers). Gamosy notes some developers think a live demo reduces launch-day urgency. These are opinions. — [Steam Page Analyzer: do Steam demos increase sales?](https://www.steampageanalyzer.com/blog/do-steam-demos-increase-sales); [Wishlistlab](https://wishlistlab.io/guides/steam-next-fest-demo-tips); [Gamosy](https://gamosy.com/blog/steam-next-fest-guide)
- [Vendor] Benchmarks of roughly 10-20% demo-to-wishlist during Next Fest (about 20% called "good") and 5-10% for a standalone demo launch; no published basis. — summarised across [Steam Page Analyzer: demo best practices](https://www.steampageanalyzer.com/blog/steam-demo-best-practices) and [Wishlistlab](https://wishlistlab.io/guides/steam-next-fest-demo-tips)

### Inferences
- For "Engagement", keeping the demo up post-launch is low-risk if it is good and stable. The strongest (correlational) signal is the review-score benefit (self-selection of non-fans away from buying), which feeds back into the 2-3x review-label conversion effect above and keeps the game away from the <40% featuring penalty.
- Steam-native steps that matter more than the keep/remove decision: (1) republish the base page after launch so the Download Demo button appears, and consider the prominent green-box placement; (2) make sure demo saves carry over (shared Cloud) so demo players can buy and continue; (3) grant demo-equivalent achievements in the full game; (4) if the demo covers the narrative opening, consider whether it gives away the hook (the narrative-genre worry HTMAG describes).
- Demo-to-full purchase conversion after launch is not published anywhere. The developer's own Steamworks data (demo players who later own the full game) is the only reliable read.

### Gaps
- No public data on demo-player-to-purchase conversion after launch, and no controlled comparison of sales with the demo removed vs kept.
- The HTMAG sample sizes for most comparisons are not given; the review-score difference is correlational and may reflect genre mix (Souls-likes, which have high demo-live rates, may also differ in review scores).

## What do developers report about Steam Deck Verified, achievements, trading cards affecting sales or visibility?

### Takeaway
None of the three has measured causal evidence of affecting sales. Deck Verified is a compatibility badge that Valve says doesn't gate availability. Deck players are a small share of users but a larger share of playtime, with developer anecdotes of about 5-10% of launch sales on Deck. Achievements and trading cards do not show up as success drivers in available analysis. Trading cards are gated behind a sales threshold and bring negligible revenue to small indies; the old argument that they drive Discovery Queue traffic is opinion.

### Cited Findings
**Steam Deck Verified**
- [Valve] "The results of a compatibility review will not affect whether your game is available to customers on Deck or Machine"; customers "aren't prevented from viewing or purchasing content that may not work well on their device." Deck users can sort and filter their library by compatibility. Any game Verified on Deck is "guaranteed to be Verified on Steam Machine as well." Reviews can be requested before release, target completion within a week, and auto-publish after about a week. The Valve page does not mention "Great on Deck" featuring or any sales effect. — [Steamworks: Steam Deck compatibility](https://partner.steamgames.com/doc/steamdeck/compat)
- [Analyst, via newsletter summary] GameDiscoverCo estimates 5-7 million Steam Decks sold; Deck users are about 0.7% of Steam users but about **2.75% of Steam playtime**. It advises it is "not worth targeting the Steam Deck specifically yet," though it can add sales if resources allow. — [gamedevreports summary: GameDiscoverCo, which games are successful on Steam Deck](https://gamedevreports.substack.com/p/gamediscoverco-which-games-are-successful?open=false)
- [Developer-reported, secondhand] The Pale Beyond reportedly saw about **10% of launch sales on Deck**, falling to about **5%** later; another unnamed indie reported 10% of launch sales on Deck. These are forum reposts and I could not verify the original developer statements. — [GamingOnLinux comment thread](https://www.gamingonlinux.com/2024/08/black-myth-wukong-shows-very-clearly-valve-are-selling-a-lot-of-steam-decks/page=1)
- [Press, July 2026] Boiling Steam estimates Steam Deck hardware sales dropped about 82% after Valve's price increase (chart-rank-based estimate, unconfirmed by Valve). This bears on how large the Deck audience will grow, not on Verified's effect. — [Wccftech](https://wccftech.com/steam-deck-sales-reportedly-crater-82-after-valves-price-hike-slipping-from-5th-to-14th-on-steam/)

**Achievements and trading cards**
- [Vendor, 2026] "No public study isolates achievements or cards as a causal sales driver." In the vendor's review of success factors, concurrent players correlated most with revenue; achievements and cards did not show up as drivers. Most indie cards trade for cents and the developer's cut is "a dime on the dollar". — [Steam Page Analyzer: achievements and trading cards](https://www.steampageanalyzer.com/blog/steam-achievements-trading-cards)
- [Developer guide/community] Cards unlock only after a game passes a sales threshold based on revenue, not units, so cheap or heavily bundled indies often don't qualify early. — [Game Developer: Steam Trading Cards guide for developers (2020, OLDER)](https://gamedeveloper.com/business/steam-trading-cards-a-guide-for-developers-2020-); [Tech4Gamers: How Steam struggles with its smallest games](https://tech4gamers.com/?p=272179)
- [Opinion, OLDER] Older pieces argue cards bring exposure because players work through Discovery Queues during major sales to earn cards, sending traffic to game pages. Opinion, not measured. — [GamesRadar: The toll Steam Trading Cards take on indies](https://www.gamesradar.com/toll-steam-trading-cards-take-indies)
- [Valve] Valve recommends disabling achievements in demos and granting them in the full game after purchase (a demo-to-full continuity lever). — [Steamworks: Demos](https://partner.steamgames.com/doc/store/application/demos)

### Inferences
- For a solo dev 8 days out: request the Deck compatibility review now if not already done (about one-week turnaround). Verified/Playable matters for the 2.75%-of-playtime Deck segment and now Steam Machine buyers, and an "Unknown" or "Unsupported" badge is shown on store pages to those users. Expect a small single-digit-to-~10% share of launch sales from Deck at most (anecdotal).
- Achievements are cheap table stakes that a segment of buyers looks for, but don't expect a measurable sales effect. Trading cards are not something a solo dev can switch on for launch, since eligibility depends on revenue, so they are not a launch lever.

### Gaps
- No controlled or Valve data on whether Verified status changes visibility (e.g., placement in Deck-specific store sections) or conversion.
- No 2024-2026 developer postmortem with a measured achievements effect was found.

## Bundles with similar indie games (complete-the-set bundles) and developer/franchise pages: reported effects?

### Takeaway
Complete-the-set bundles are a sanctioned way to cross-promote on a Steam store page: the bundle box appears on each member game's page and buyers pay only for what they don't own. Reported effects are anecdotal, ranging from big spikes when a partner game launches to bundle volumes below organisers' projections. A two-game bundle with a well-matched indie (especially one whose audience already overlaps) is the most practical version for a new solo launch.

### Cited Findings
- [Valve] With a Complete-the-Set bundle, customers "pay for and receive only the bundle items missing from their Steam library," and the same rule applies when gifting. Adding items to an existing bundle lets past buyers purchase just the new ones. — [Steamworks: Bundles](https://partner.steamgames.com/doc/store/application/bundles?language=english)
- [Vendor/blog, unverified] A Steam-focused developer blog reports one developer's daily sales rising **over 15x** when a bundle partner launched and settling at about **2x the prior baseline** after 30 days. Single anecdote, not audited; the search summary did not clearly name which of the two blogs below carried it. — [Steam Page Analyzer: bundle strategy](https://www.steampageanalyzer.com/blog/steam-bundle-strategy); [Bugnet: Steam bundles for indie devs](https://bugnet.io/blog/steam-bundles-for-indie-devs)
- [Vendor/blog] One guide argues bundles don't cannibalise individual sales because the discount applies only to items the buyer doesn't own, and says bundles have been one of the few sanctioned ways to cross-promote on a Steam store page since September 2024 (rule-change claim not verified against Valve docs). — [Bugnet](https://bugnet.io/blog/steam-bundles-for-indie-devs)
- [Press, 2026] Two indie games with identical names ran a joint Steam bundle at $18.57 that generated strong Reddit buzz (2k+ upvotes); no sales data. — [Pulse.bot coverage](https://www.pulse.bot/gaming/news/freak-steam-game-naming-coincidence-unintentionally-results-in-some-of-the-best-indie-marketing-ive-a5785057-4456-4458-aba3-f365e4078bb1)
- [Developer-reported, OLDER] In a Bundle Stars (third-party bundle, not a Steam bundle) case study, the developer sold about 6,500 bundles against organiser expectations of 12,000-20,000. — [Game Developer: Rubicon's Bundle Stars postmortem](https://gamedeveloper.com/business/rubicon-s-bundle-stars-postmortem)
- [Press] Since May 2023, Steam search surfaces developers, publishers and franchises (plus tags), so a developer/franchise page is reachable from search. — [Game Developer: Steam games can now be searched by developer, franchise and tag](https://gamedeveloper.com/business/steam-games-can-now-be-searched-for-by-developer-franchise-and-tag); [GamingOnLinux](https://gamingonlinux.com/2023/05/valve-gave-steam-store-search-a-very-useful-upgrade)

### Inferences
- A solo developer with only "Engagement" can still bundle with a friendly developer's thematically similar game (same top tags). The bundle box on the partner's page exposes "Engagement" to the partner's owners and visitors, and the partner gets a boost when "Engagement" launches. Bundles typically need Valve review and lead time, so starting it in the 8-day window is tight; it is more realistic for the weeks after launch or the first seasonal sale.
- If the developer has prior or future titles, a developer homepage (Creator page) gives followers a channel for future releases, and since 2023 it can surface in search. That matters more given the generic title (next section).

### Gaps
- No systematic, measured study of Steam bundle lift for indie games was found; the 15x/2x anecdote is unverified.
- Valve's lead time for bundle review and the exact store-page placement rules weren't confirmed in this research.
- Developer homepage follower-notification mechanics weren't documented in sources reviewed.

## How do Steam's recommendation systems (More Like This, Discovery Queue, Interactive Recommender) respond after launch, per Valve statements? (Includes Update Visibility Rounds, events cadence, reviews and refunds.)

### Takeaway
Per Valve, post-launch algorithmic visibility is driven by "players and purchases", language support and tags, not by wishlists, traffic, conversion rate or review score (except a featuring penalty below 40% positive). The New Releases queue favours titles with the fewest views. New & Trending and Top Sellers reward sales momentum and are crowded out on busy weeks. The Interactive Recommender is trained on playtime, so it cannot recommend a brand-new game until people have played it; the Discovery Queue is designed to cover new games. After the launch window, Update Visibility Rounds (shown to owners and wishlisters) and well-timed events are the main Steam-native ways to re-surface.

### Cited Findings
**Valve: what drives visibility after launch**
- [Valve] Players and purchases: "This is a strong signal to Steam that there is interest in your game." The Main capsule "is driven by what players spend time and money on, rather than Valve curation"; "The main capsule is different for every customer"; a product "doing really well" may get bumped into it. — [Steamworks: Visibility on Steam](https://partner.steamgames.com/doc/marketing/visibility)
- [Valve] New Releases queue: "prioritizing the titles that have the least amount of views since release"; tag or product-type filters can keep a title out of a user's queue. All New Releases lists titles at full launch and Early Access. — [Steamworks: Visibility](https://partner.steamgames.com/doc/marketing/visibility)
- [Valve] New & Trending: "Your title may be bumped off this list quickly if many other popular products are releasing at the same time." Top Sellers: "It can appear on 'top sellers' list on the store home page," plus genre and tag pages once it has a sales rank. Discovery Queue: "Your title might be recommended by Steam Curators or appear in the Discovery Queue." — [Steamworks: Visibility](https://partner.steamgames.com/doc/marketing/visibility)
- [Valve] Review score "is **not a factor** in algorithmic visibility," but "If your game dips below 40% into Mostly Negative, your game will be less likely to be featured." Paid visibility: "Nope." — [Steamworks: Visibility](https://partner.steamgames.com/doc/marketing/visibility)
- [Valve] The visibility documentation doesn't mention More Like This, the Interactive Recommender, or refunds. — [Steamworks: Visibility](https://partner.steamgames.com/doc/marketing/visibility)

**Interactive Recommender and Discovery Queue**
- [Press quoting Valve, OLDER 2019] The Interactive Recommender is a neural-network model trained on users' playtime histories and doesn't use tags or reviews. Per Valve, it "can't recommend new releases that nobody has played yet," whereas the Discovery Queue is designed to do that. — [PC Gamer: Interactive Recommender uses machine learning, not tags or reviews](https://www.pcgamer.com/steams-new-interactive-recommender-uses-machine-learning-not-tags-or-reviews-to-tell-you-what-to-play)
- [Press, OLDER 2019] Coverage says the model picks up new releases after a few days of play data when retrained; sources disagree on how fast, and it was later built into the store. — [GameGrin](https://www.gamegrin.com/news/steam-introduces-the-interactive-recommender/); [PC Gamer: now built into the store](https://pcgamer.com/steams-interactive-recommender-is-now-built-into-the-store-to-help-you-find-hidden-gems)

**More Like This and tags (third-party, not Valve docs)**
- [Vendor] More Like This is driven mainly by overlap in top tags; the top tags carry more weight, and changes take a few days to propagate. One guide quotes Steamworks as saying some recommendation algorithms weight less-frequently used tags more heavily than very common ones (Valve original not verified here). — [Immutable: Steam tags guide](https://www.immutable.com/guides/steam-tags); [Immutable: how the Steam algorithm works](https://www.immutable.com/guides/steam-discovery-algorithm)
- [Vendor] A sudden post-launch traffic drop is the normal decay of launch visibility, not a penalty. — [Steam Page Analyzer: traffic sources](https://www.steampageanalyzer.com/blog/steam-traffic-sources)

**Update Visibility Rounds**
- [Valve] Rounds highlight products with major updates on the front page, shown to customers who own the game or have it wishlisted. Early Access titles must wait two weeks after launch; otherwise rounds must wait until initial launch visibility ends. "There is no limit to how much time must be between the use of your Update Rounds." DLC has no rounds of its own; use the base app's. — [Steamworks: Visibility](https://partner.steamgames.com/doc/marketing/visibility)
- [Vendor, unverified] Valve reviews whether an update qualifies as "major" and can deny a round. One guide says every game gets one free round and earns more through engagement, and that a round paired with a discount is "significantly more effective" than either alone; this conflicts with or adds to the Valve text above. — [Steam Page Analyzer: update visibility rounds](https://www.steampageanalyzer.com/blog/steam-update-visibility-rounds)
- [Developer-reported, via press] One developer said their fourth visibility round "was over five times more effective than previous rounds in terms of clickthrough." — [MCV/Develop](https://mcvuk.com/?p=73540)

**Events and announcements cadence**
- [Valve] "All users who are following a product will receive its announcements in their activity feeds." The last two announcements appear on the store page below the DLC section; events show on the Library detail page and can surface at the top of Library home. Valve sets no posting frequency, warning that "constant communication just to fill space risks player fatigue." Special featuring "should only be used for major events." For major updates, pair the announcement with an Update Visibility Round. Events take about an hour to appear in Library because of moderation, and Steam uses the first visible time as the post-time for deciding whether a customer has "seen" it. — [Steamworks: Event tools](https://partner.steamgames.com/doc/marketing/event_tools)

### Inferences
- Week-one priorities follow from Valve's statements: maximise purchases and playtime in the first days (New & Trending, Top Sellers and the main capsule respond to sales momentum and time played), keep tags accurate (they gate the New Releases queue and More Like This), and add supported languages if feasible (Valve explicitly boosts showing to speakers of supported languages).
- Valve says review score is not an algorithmic factor, but reviews still matter through conversion (label effect) and featuring (<40% penalty). Fast responses to negative reviews and quick patches protect the score.
- Plan the first major post-launch patch (2-4 weeks out) as a real "major update" with an announcement event plus an Update Visibility Round, ideally timed with a discount after the wishlist-email cooldown. Rounds reach owners and wishlisters, so they recapture wishlisters who didn't buy at launch.
- The Library-surfacing of events means post-launch announcements mostly reach owners, which helps retention and playtime (a Valve-stated signal) more than new sales. Post events for meaningful updates rather than on a fixed cadence.

### Gaps
- No Valve documentation was found on More Like This mechanics or how refunds affect visibility. Refund-rate effects on visibility or featuring remain undocumented in sources reviewed.
- No measured data on Update Visibility Round lift beyond the single "5x clickthrough" anecdote; the "one free round, then earned" claim is unverified against Valve's text.
- Steam Workshop and community-hub activity: no data or Valve statement found on effects on sales or visibility.
- A 2026 article claiming Steam "quietly rewrote its algorithm" with devs getting "72% more" visibility was surfaced in search ([tech-insider.org](https://tech-insider.org/steam-personalized-storefront-discoverability-2026/)) but not verified; treat it as unconfirmed.

## What to do when a game title is a common word for Steam search ("Engagement")?

### Takeaway
Steam search results match title strings literally and reportedly weight popularity heavily, while search suggestions are predictive and favour games with momentum. A common-word title like "Engagement" will compete with every title containing that word and with more popular games. Since May 2023, Steam search also surfaces tags, developers, publishers and franchises, which gives a solo dev extra hooks. No source gives measured data on generic-title penalties.

### Cited Findings
- [Analyst, OLDER 2019] GameDiscoverCo: search **suggestions** are "hot and predictive" and favour games with momentum (typing "Yes" put Yes, Your Grace at the top, likely driven by followers/wishlists), while search **results** are "extremely literal" title-string matches (e.g., "roguelike" returns any title containing that string, not games tagged roguelike). Suggestions may vary by territory. Follower-to-wishlist ratio is roughly 1:5 to 1:10. — [GameDiscoverCo: Steam search suggestions & premium positioning](https://newsletter.gamediscover.co/p/steam-search-suggestions-and-premium)
- [Developer/user-reported] A Steam community user reports Steam gives search results "more depending on popularity than on how well the title matches the searched term," and that a generic title like "Experience" leaves users little practical way to find the game except a direct link. — [Steam Community discussion](https://steamcommunity.com/discussions/forum/1/5706632550015964315)
- [Press, May 2023] Valve's search upgrade surfaces suggested tags, developers, publishers and franchises alongside game titles (e.g., "dungeon" suggests "Dungeon Crawler" tags alongside games with Dungeon in the name) and improved typo handling. — [GamingOnLinux](https://gamingonlinux.com/2023/05/valve-gave-steam-store-search-a-very-useful-upgrade); [Game Developer](https://gamedeveloper.com/business/steam-games-can-now-be-searched-for-by-developer-franchise-and-tag); [PC Gamer](https://www.pcgamer.com/steams-search-bar-just-got-a-lot-better)
- [Vendor] Steam Search traffic converts at 10-20% (vendor benchmark), second only to direct traffic, so losing searchers to a generic title has a real cost. — [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/steam-store-page-conversion-benchmarks)

### Inferences
- Steam-native mitigations for "Engagement" (inferred from how search works; none measured):
  1. Use a distinctive subtitle or descriptor in the Steam title if still possible before launch (e.g., "Engagement: <distinct phrase>"), so a unique string matches literally. Changing the store name close to launch may need Valve review; check Steamworks.
  2. Use the launch spike: suggestions favour momentum, so launch-week sales and wishlists are when "Engagement" is most likely to rank in the search dropdown. Point all off-Steam calls to action at the direct store URL (store.steampowered.com/app/<ID>) rather than "search for Engagement on Steam".
  3. Make the developer name distinctive and consistent (search surfaces developers since 2023), and create a developer homepage so "<developer name>" works as a fallback search.
  4. Choose accurate, distinctive top tags. Searches for genre words surface tag suggestions, and tag pages and More Like This depend on tag overlap, so tags are where a generic-title game is found by browsing rather than by name.
  5. Check search results for "Engagement" (and common misspellings) in a logged-out browser and from different regions after launch, since suggestions may vary by territory.

### Gaps
- No measured data on how much search traffic a common-word title loses, and no Valve documentation on how search ranks results (popularity vs title match).
- GameDiscoverCo's search analysis is from 2019; the 2023 search upgrade may have changed literal-match behaviour, and I found no newer analysis.
- Whether Valve allows store title changes (adding a subtitle) close to launch, and how long review takes, wasn't confirmed.
