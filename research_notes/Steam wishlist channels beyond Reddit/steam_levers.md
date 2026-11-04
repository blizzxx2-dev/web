# Steam-native platform levers for wishlists and launch sales (small indie, ~5,500 wishlists, launching ~Nov 12, 2026)

## What is the typical first-week conversion of wishlists to sales (median, ranges), and what affects it?

### Takeaway
The best recent benchmark is GameDiscoverCo's. For Steam games launched Aug–Oct 2024 with 5k or more launch wishlists, median first-week sales were about 10.5% of wishlists. The 25th percentile was 4.8% and the 10th percentile was 1.9%. Older developer surveys give a higher median, about 0.2x. Better conversion goes with good early reviews, a shorter Coming Soon period, and a cheaper price. Wishlist velocity just before launch predicts conversion better than the total wishlist count.

### Cited Findings
- GameDiscoverCo looked at Steam releases from Aug–Oct 2024 with at least 5,000 launch wishlists. Median first-week sales were 10.5% of launch wishlists, the 25th percentile was 4.8%, and the 10th percentile was 1.9%. GameDiscoverCo said the median was lower than it expected. Note that these "sales" include buyers who never wishlisted the game. — [Game World Observer summary](https://gameworldobserver.com/2024/12/06/wishlist-to-sales-ratio-steam-gamediscoverco-benchmark); [GameDiscoverCo](https://newsletter.gamediscover.co/p/revealed-new-data-on-steam-wishlist)
- GameDiscoverCo's 2024 developer survey (self-reported) found a median of 0.2x first-week sales per launch wishlist, unchanged from 2021. Games launching with more than 10k wishlists had a median of 0.17x. Games with hundreds or low thousands of wishlists tended to do better than the median. A pre-launch spike in wishlists or followers was the best predictor of conversion. — [GameDiscoverCo 2024 survey](https://newsletter.gamediscover.co/p/revealed-the-state-of-steam-wishlist)
- The 2025 GameDiscoverCo report covers Sept 2024–Sept 2025 launches with 25k+ wishlists. The median was 0.15x. For games priced above $10 the median fell to 0.10x, and excluding NSFW games it was about 0.14x. In the same report, underperformers had a median first-7-day review score of 67% (Mixed) versus 91% for overperformers. Underperformers had also spent an average of 411 days on Steam before release, versus 214 days for overperformers. GameDiscoverCo says conversion varies by about an order of magnitude between games. — [GameDevReports summary of GameDiscoverCo](https://gamedevreports.substack.com/p/gamediscoverco-the-state-of-steam)
- An earlier GameDiscoverCo analysis (early 2022 to early 2024) found the median dipped about 15%, from just over 0.15 to about 0.125. GameDiscoverCo says there is no clear long-term decline, and that the real change is that wishlists have become harder to gather. — [search summary of GameDiscoverCo/Game World Observer](https://gameworldobserver.com/2024/12/06/wishlist-to-sales-ratio-steam-gamediscoverco-benchmark); [GameDevReports](https://gamedevreports.substack.com/p/gamediscoverco-the-state-of-steam)
- Valve's own position is that "there's no formula for predicting sales from wishlists," though it calls wishlists valuable. — [Steamworks: Wishlists](https://partner.steamgames.com/doc/marketing/wishlist)
- Conflicting figure: Presskit.gg attributes a median of about 20% for games with 5k–40k wishlists to Simon Carless and GameDiscoverCo. That matches the survey-based 0.2x figure, not the 10.5% figure, which comes from GameDiscoverCo's own outside estimates. — [Presskit.gg](https://presskit.gg/field-guides/why-steam-wishlists-dont-convert)

### Inferences
- The two medians measure different things. The 0.2x figure comes from self-selected developer survey responses and skews optimistic. The 10.5% figure is GameDiscoverCo's estimate across all qualifying games. Planning should use 10–20% as the median band and 2–5% as a realistic downside.
- Some levers can still be pulled 8 days out: a cheaper price or launch discount, getting positive reviews early, and creating a pre-launch wishlist spike (velocity).

### Gaps
- I found no GameDiscoverCo breakdown by genre or price for games under 10k wishlists. The 2025 report's text only covers the 25k+ bucket.
- The Automaton article on how genre, timing and reviews affect conversion could not be read, because the fetch was truncated.

## Does a launch discount (10-20%) help, and by how much? What do the launch discount wishlist emails do?

### Takeaway
Steam sends a wishlist email at launch whether or not the game is discounted. A launch discount of 20% or more can also trigger the discount email, but a 2-week per-app email cooldown means a launch-day discount email is very likely the same notification, not a second one. The main value of a discount is the strikethrough price, a "% off" message in the email, and placement in Specials. No reliable public dataset puts a size on the lift. The launch discount has to be set up before the release date.

### Cited Findings
- Launch discount rules: it runs 7–14 days and can be 10% to 40% off. Valve suggests "around 10% to 15%." It is set up near the release-date setting and must be configured before release. It is the one exception to the 30-day cooldown after release, but it does start a 30-day discount cooldown afterwards. Seasonal Sales are exempt from that cooldown. Valve warns that a very deep launch discount can signal low value. — [Steamworks: Discounting](https://partner.steamgames.com/doc/marketing/discounts)
- Discounts of 20% or more trigger wishlist email notifications. The page is inconsistent here: one section says they "will automatically trigger" the email and another says they "can." Discounted titles can also appear in "specials" sections. — [Steamworks: Discounting](https://partner.steamgames.com/doc/marketing/discounts)
- Wishlist emails go out when a game releases in Early Access or Full Release, and again when it moves from Early Access to 1.0. A discount email requires at least 20% off, lasting more than 8 hours, on the lowest-priced package. Only users with a verified email who haven't opted out receive them. There is a 2-week per-app cooldown covering all email types for that app, and it can be extended during seasonal sales. Discount emails held up for more than a week are dropped. — [Steamworks: Wishlists](https://partner.steamgames.com/doc/marketing/wishlist)
- Chris Zukowski says a launch discount "emails everyone who wishlisted," and the resulting sales feed the algorithm because "Steam loves spikes." The Specials tab features discounted games that are selling well. — [How To Market A Game, 2023](https://howtomarketagame.com/2023/09/04/killing-the-myths-behind-steams-visibility/)
- Unverified claim: some third-party blogs say a 10–15% launch discount gives 20–40% higher week-one conversion, and that only 60–75% of wishlisters receive notifications. I found no underlying dataset for either figure. — [steampageanalyzer.com](https://www.steampageanalyzer.com/blog/steam-wishlist-conversion-rates); [bugnet.io](https://bugnet.io/blog/steam-launch-discounts-how-deep-should-you-go)

### Inferences
- With 8 days to go, the launch discount must be configured right away, because it cannot be added after release.
- A 10–15% discount costs little and adds strikethrough urgency. 20% would make sure it qualifies as a discount email, though the release email already reaches wishlisters. The 2-week cooldown means you cannot get a separate discount email within 14 days of the release email.
- Both a launch discount and the Winter Sale are possible. Valve's page says the launch discount's 30-day cooldown doesn't apply to Seasonal Sales, and a mid-November release would be more than 30 days before the Winter Sale starts on Dec 17.

### Gaps
- No primary data quantifies the conversion lift of 10% vs 20% vs no discount.
- No Valve figure says what share of wishlisters actually receive or open the email.

## How important are early reviews (10 reviews threshold etc.) and how do devs get them in week one?

### Takeaway
At 10 reviews Steam starts showing a review score summary, which is a real conversion signal. Whether 10 reviews also unlocks algorithmic visibility is disputed. Zukowski's 2022 view was that it unlocks Discovery Queue testing. By 2023 he reported that Valve says nothing in the algorithm boosts a game at 10 reviews, and that review score is ignored while it is Mixed or better. Early review quality does correlate with conversion. Week-one reviews come from personally asking fans for them, with no incentives. Reviews from free keys do not count toward the score.

### Cited Findings
- 2022 claim: a game needs 10 reviews from paying buyers before it gets Discovery Queue traffic, and the DQ burst typically fades within a few days. The author calls this "98% confident" speculation. Reviews from free keys can be posted but don't count. Valve developers say Mixed reviews aren't penalized, and games are hidden only at Mostly Negative or worse. — [How To Market A Game, 2022](https://howtomarketagame.com/2022/01/25/why-your-first-10-reviews-are-the-most-important/)
- 2023 update: Valve says no part of the algorithm boosts a game at 10 reviews. The effect likely comes from the thumbs-up review summary that appears at 10 reviews. The algorithm ignores review percentage while a game is Mixed or above (about 40% positive or higher). — [How To Market A Game, 2023](https://howtomarketagame.com/2023/09/04/killing-the-myths-behind-steams-visibility/). This contradicts the 2022 post.
- Review rate: the Boxleiter method estimates about 1 review per 30 buyers, so roughly 300 sales are needed for 10 reviews. — [How To Market A Game, 2022](https://howtomarketagame.com/2022/01/25/why-your-first-10-reviews-are-the-most-important/)
- Underperforming 2024–25 launches had a median first-7-day review score of 67%, versus 91% for overperformers. — [GameDevReports/GameDiscoverCo](https://gamedevreports.substack.com/p/gamediscoverco-the-state-of-steam)
- How to get week-one reviews within Valve's rules: build a VIP list of friends, family and community members, message them personally before launch to ask for a day-one review, and send reminders on launch day and later in the week. Post to Discord, X and the mailing list. Valve forbids offering rewards for reviews, asking for reviews from inside the game, and manipulating reviews. — [How To Market A Game, 2022](https://howtomarketagame.com/2022/01/25/why-your-first-10-reviews-are-the-most-important/)
- FirstLook argues that a game which cannot reach 10 reviews organically in week one simply lacked demand. — [FirstLook](https://firstlook.gg/blog/how-many-steam-reviews-does-your-game-need-at-launch)

### Inferences
- At 5,500 wishlists and the 10.5% median (about 580 units), the 1-in-30 rule gives about 19 reviews in week one. At the 10th percentile (about 105 units) it gives about 3–4. Treating friends and community buyers as a seeded source of the first 10 reviews is therefore worthwhile insurance.

### Gaps
- I found no current Valve statement on the 10-review mechanics. The claim that Valve denies a boost is relayed secondhand by Zukowski.

## What do store events/announcements do for visibility and traffic?

### Takeaway
Steam events appear in the Library "What's New" row, the activity feed, on the store page and on the community hub. They mainly reach people who already own or follow the game, so they matter more after launch. Update Visibility Rounds (five per product, up to 1M homepage impressions each) are a post-launch homepage lever for major updates. Hard numbers on the traffic events drive are scarce.

### Cited Findings
- Event placements: the Library home "What's New" row, the Library app-detail activity feed, the store product page and the community hub. Impressions count only when the capsule is actually seen, and signed-out users are not counted. — [Steamworks: Event stats](https://partner.steamgames.com/doc/marketing/event_tools/stats)
- Update Visibility Rounds: each product gets 5, and more can be granted to games that sell well. Each round lasts up to 30 days or up to 1M homepage impressions, whichever comes first. They typically don't show during major seasonal sales. — [Steamworks: Update Visibility Rounds](https://partner.steamgames.com/doc/marketing/visibility/update_rounds)
- In 2025–26, Steam's Discounts & Events section began showing smaller games. One indie got 7,355 visits from that grid over six months, and other small games reported going from almost nothing to several thousand visits (anecdotal, via Hooded Horse's Tim Bender). — [80.lv](https://80.lv/articles/steam-quietly-made-a-huge-discoverability-change-for-indie-games/)
- Zukowski's guide to using Steam events as a marketing tool (2021, older). — [How To Market A Game, 2021](https://howtomarketagame.com/2021/04/28/how-to-market-your-game-using-steams-events-system/)

### Inferences
- Before launch, a "launch date / launching soon" event reaches followers and wishlisters through the Library feed. After launch, the first big patch is the natural use for an Update Visibility Round, ideally timed away from the Winter Sale (Dec 17–Jan 4).

### Gaps
- I found no measured click-through or wishlist uplift from a pre-launch announcement event.

## What festivals or Steam sales near mid-November 2026 could a launching game join, and does launching near Steam sales hurt?

### Takeaway
The Steamworks calendar shows only one fest in the mid-November window, the Auto-Battler RPG Fest (Nov 16–23, 2026), which is limited to its genre. The Winter Sale runs Dec 17, 2026–Jan 4, 2027, and a game released at least 30 days before it can join with a discount. A Nov 12 launch qualifies. The 2026 Autumn Sale reportedly moved to Oct 1–8, so no Steam sale falls on Black Friday. Zukowski's 2026 data suggests launching during a sale can mean less competition for the front-page widgets, which challenges the "avoid sales" advice.

### Cited Findings
- Steamworks Upcoming Events lists the Auto-Battler RPG Fest (Nov 16–23, 2026, auto-battler genre only) and the Winter Sale (Dec 17, 2026–Jan 4, 2027). For the Winter Sale, games released at least 30 days before the start can join with a discount. The navigation also lists a Steam Medieval Fest 2026, but no dates were shown. The next Next Fests are Feb 22–Mar 1, 2027 and Jun 14–21, 2027. — [Steamworks: Upcoming Events](https://partner.steamgames.com/doc/marketing/upcoming_events)
- The 2026 Autumn Sale ran Oct 1–8, moved from its old late-November slot (a secondary press source). The Steamworks page showed no October events when fetched, probably because past events had been removed. — [Playnews](https://www.playnews.gg/en/deals/steam-autumn-sale-2026-october-1-to-8-starting-at-7-pm-paris-time)
- Products still in a release cooldown or price-increase cooldown cannot join Seasonal Sales. — [Steamworks: Discounting](https://partner.steamgames.com/doc/marketing/discounts)
- Zukowski analysed the Winter Sale of Dec 18, 2025–Jan 5, 2026. Few games launched during it, and games on Popular Upcoming stayed there all week. In January, Popular Upcoming stays averaged 2.1 days (median 1). New & Trending stays averaged 4.25 days (median 4). His view is that launching during the sale gives more front-page time. This is one month of data, with some days missing. — [How To Market A Game, Feb 2026](https://howtomarketagame.com/2026/02/18/the-counterintuitive-advantage-of-launching-during-steams-busiest-event/)
- The conventional view (blog claims without published sample sizes): Popular Upcoming and New & Trending disappear during big sales, and buyers wait for discounts. — [Fungies](https://fungies.io/when-to-time-the-release-of-your-indie-game); [steampageanalyzer](https://www.steampageanalyzer.com/blog/best-steam-launch-dates)

### Inferences
- A launch around Nov 12 sits in a quiet window. It is about 5 weeks before the Winter Sale and clear of the Autumn Sale, which in 2026 ran in October. The Winter Sale then works as the first post-launch discount, and its traffic gives a second wave. The game is eligible, and the launch-discount cooldown is exempt for Seasonal Sales. Unless the game is an auto-battler, no themed fest is available in its launch week.

### Gaps
- The full Steamworks fest list for late 2026 was only partly visible. Check the Steamworks events page and the opt-in deadlines directly.

## How much traffic do Steam curators drive in practice?

### Takeaway
There is little hard data. The available evidence and anecdotes say curators drive negligible traffic compared with Steam's algorithmic surfaces. Curator Connect is mainly a safe way to send keys, a filter against fake curators who scam keys, and a source of social-proof quotes on the store page. Reviews from free keys don't count toward the score, so curators can't fill the 10-review count.

### Cited Findings
- Curator Connect lets developers send game copies directly to curators they choose, once a Coming Soon page is live, and it was built to cut down on key-scam emails. — [MCV/UK](https://www.mcvuk.com/steam-curator-connect-now-live-for-all-developers/); [Steamworks: Curators](https://partner.steamgames.com/doc/marketing/curators)
- One developer's analysis after Steam's Discovery update reported negligible curator traffic, while the Discovery Queue was a major source of visits (anecdotal and older). — [Game Developer, "I Wish Upon a Steam"](https://www.gamedeveloper.com/business/i-wish-upon-a-steam)
- Following a curator, developer or publisher counts as a "hardcore purchase-intent" signal for Steam. — [How To Market A Game, 2023](https://howtomarketagame.com/2023/09/04/killing-the-myths-behind-steams-visibility/)
- Free-key reviews don't count toward the review score. — [How To Market A Game, 2022](https://howtomarketagame.com/2022/01/25/why-your-first-10-reviews-are-the-most-important/)

### Inferences
- Curator Connect is worth a couple of hours sending keys to curators who fit the game's genre. The payoff is "Recommended by" curator quotes and a few followers, not meaningful traffic.

### Gaps
- I found no 2023–2026 postmortem that measures Curator Connect traffic or sales.

## What does a ~5,500 wishlist count at launch typically mean for first-week and first-year sales?

### Takeaway
At 5,500 wishlists the median first week is about 550–1,100 units (10.5%–20%). The downside is about 100–265 units (10th–25th percentile). Year-one revenue typically runs about 3x week-one revenue (median 3.16x, range roughly 2x to 6x). 5,500 is right at the reported 5–7k entry level for Popular Upcoming, so a brief or zero stay on that list is likely. Reaching New & Trending reportedly takes about $8k in a few days.

### Cited Findings
- Benchmarks: median first week 10.5%, 25th percentile 4.8%, 10th percentile 1.9% (5k+ wishlist cohort, Aug–Oct 2024). — [Game World Observer/GameDiscoverCo](https://gameworldobserver.com/2024/12/06/wishlist-to-sales-ratio-steam-gamediscoverco-benchmark)
- Survey median 0.2x. Games with hundreds or low thousands of wishlists tended to beat the median. Year-one gross revenue was a median 3.16x week one (range under 2x to over 6x). Month one was 1.39x week one, year two cumulative 4.2x, and year three 5.5x (n≈10). — [GameDiscoverCo 2024 survey](https://newsletter.gamediscover.co/p/revealed-the-state-of-steam-wishlist)
- Popular Upcoming entry takes about 5,000–7,000 wishlists. Average stays are about 1–2 days, about 4 days at best outside sales. New & Trending entry is about $8k gross in a couple of days, which Zukowski calls a "gut feeling." — [How To Market A Game, Feb 2026](https://howtomarketagame.com/2026/02/18/the-counterintuitive-advantage-of-launching-during-steams-busiest-event/)
- Popular Upcoming ranks by total wishlists, and New & Trending uses an undisclosed earnings threshold that varies by country and language, so localization helps. The Discovery Queue is driven by short-term wishlist gains. — [How To Market A Game, 2023](https://howtomarketagame.com/2023/09/04/killing-the-myths-behind-steams-visibility/)
- Steam says there is no minimum wishlist count before it shows a game. — [Steamworks: Wishlists](https://partner.steamgames.com/doc/marketing/wishlist)

### Inferences
- These figures are my arithmetic on the cited benchmarks, not reported data. At a 10.5% median, 5,500 wishlists gives about 580 week-one units. At the 0.2x survey median it gives about 1,100, at the 25th percentile about 265, and at the 10th percentile about 105. At a $10–15 net-of-discount price, a median week is about $6k–$9k gross before Steam's cut. That is near Zukowski's estimated $8k bar for New & Trending, so the launch spike and discount matter. Year one at about 3.16x week-one revenue gives roughly $18k–$28k gross at the median.
- Popular Upcoming is borderline at 5,500 wishlists, so a push to gain wishlists in the final week (velocity) could also help with Discovery Queue placement.

### Gaps
- I found no specific 2024–2026 postmortem with about 5–6k launch wishlists and exact sales. VG Insights/Gamalytic cohort data for this size wasn't retrieved.
- I didn't research demo effects in depth. Secondhand figures I could not verify: a median of 16.33% of demo players wishlist the game (Zukowski survey), and a median February 2026 Next Fest demo gained about 200 wishlists (GameDiscoverCo estimate, via a search summary). The demo wishlist email is available once, within 2 weeks of the demo going live. — [Steamworks: Wishlists](https://partner.steamgames.com/doc/marketing/wishlist)
