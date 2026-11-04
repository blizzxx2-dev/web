# International markets for a small Steam survivors-like / roguelite: China, Japan, Korea, Brazil, Russia/CIS, Germany

Scope note: the research covers 2017–2026 sources, and older items are flagged. "Vendor" means a localization or marketing agency with a commercial interest. "Dev-reported" means numbers a developer or publisher released about its own game. "Estimate" means third-party modelled data (Gamalytic, GameDiscoverCo ownership data, Boxleiter-style estimates). Steam does not publish country sales.

I tried to pull per-language Steam review counts directly from Steam's public review API for 10 survivors-likes. The endpoint redirected to the store homepage from this environment, so no first-party review-language data was collected. This is a gap.

---

## Q1. Which non-English markets matter most, and what share of Steam sales for roguelites and survivors-likes comes from China and other regions?

### Takeaway
Simplified Chinese is the biggest or joint-biggest language on Steam, and roguelikes overindex in China. Gamalytic estimates Brotato at about 42% Chinese players, and GameDiscoverCo data puts The King Is Watching at 39% of units from China. After China, the next tier for a survivors-like is Russian (CIS), German, Brazilian Portuguese, Japanese and Korean, roughly in that order of Steam audience size. Japan and Korea are smaller but grow faster for new games.

### Cited Findings
**Steam-wide language and country data**
- Valve's full-year 2024 account data, presented at GDC 2025, shows these primary-language shares among Steam users:
  - Simplified Chinese 33.7%
  - English 33.5%
  - Russian 8.2%
  - Spanish 4.6%
  - Brazilian Portuguese 2.8%
  - This is secondary reporting of Valve's talk. [WN Hub](https://wnhub.io/news/stores-and-publishing/item-47433); [GamesRadar](https://www.gamesradar.com/games/english-is-no-longer-the-biggest-language-on-steam-as-chinese-gamers-embrace-pc-gaming-even-harder-after-black-myth-wukong)
- Valve's Erik Peterson gave 33.6% Simplified Chinese at Devcom/Gamescom 2025. [WN Hub](https://wnhub.io/news/stores-and-publishing/item-47433)
- The monthly opt-in Hardware Survey spiked to 50.06% Simplified Chinese in February 2025 during Chinese New Year. Treat monthly survey figures as volatile. [GamingOnLinux](https://gamingonlinux.com/2025/03/steam-sees-a-big-rise-in-simplified-chinese-for-february-2025-bringing-linux-down-below-2p)
- GameDiscoverCo's country split of players for Steam games with more than 100k lifetime players (July 2024) is below. [GameDiscoverCo](https://newsletter.gamediscover.co/p/whats-the-country-split-for-players)
  - Shares: US 20.8%, China 8.4%, Russia 5.7%, Germany 5.3%, UK 4.5%, Canada 3.8%, Brazil 3.0%, France 2.6%, Poland 2.4%, Australia 2.3%. Japan is #11 and Korea #19.
  - For games launched from January 2021 onward, China rises to 11.45%, which the author believes is an undercount. Japan moves to #10 and Korea to #18.
  - China may be undercounted because the profile country field is optional, many new profiles are private by default, and Steam China is a grey market.
- A consultant (Llama & Griffin, May 2026) claims about 79% of Chinese PC gamers play premium titles on the international Steam client, mostly without a VPN, paying in yuan. He also says China's share for well-localized Steam top-20 titles "floors at about 20%". These are consultant claims and I could not check the methodology. [Recognizing Patterns](https://recognizingpatterns.substack.com/p/congratulations-you-ignored-the-chinese)

**Roguelike and survivors-like specific**
- Brotato, by Gamalytic estimate, has players by country of about 41.6% China, 10.8% US and 7.6% Germany, with about 40% other. Gamalytic labels this "players by country", not a units split. Its total of about 7.9M copies (range 5M–10.8M) conflicts with other trackers at about 3M. [Gamalytic](https://gamalytic.com/game/1942280)
- The King Is Watching, a roguelike priced at €15 base, sold 39% of units in China, 16% in the US and 9% in Germany. GameDiscoverCo ranks it #30 for Chinese ownership share among 325 Steam roguelikes with more than 100k sales. This is GameDiscoverCo data, August 2025. [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-the-king-is-watching-sold-200k)
  - Inference from that ranking: at least 29 roguelikes with more than 100k sales have an even higher Chinese share than 39%.
- Bramble Royale, a roguelike deckbuilder, sold 30% in the US and 18% in China. [GameDiscoverCo](https://newsletter.gamediscover.co/p/why-did-this-excellent-roguelike) (via search summary)
- Mortal Glory, an indie roguelike, saw China's share of sales grow from 3% to 24% after CJK localization. This is a vendor-published case study from ECI Games. The page sat behind a bot check, so the figure comes from a search summary and was not read in full. [ECI Games](https://www.ecigames.net/media/real-localization-results-how-an-indie-roguelike-grew-unit-sales-with-cjk-localization)
- No public country split was found for Megabonk, Ball x Pit, Vampire Survivors, Halls of Torment or Deep Rock Galactic: Survivor. Sensor Tower/VG Insights keeps country splits behind enterprise accounts. [Sensor Tower VGI – Megabonk](https://app.sensortower.com/vgi/game/megabonk)

**Context on China-centric hits (not survivors-likes)**
- Chinese-themed indies reach 75–80% Chinese ownership, according to GameDiscoverCo estimates from January 2024:
  - Back to the Dawn: about 75%.
  - Wandering Sword: about 80% Chinese ownership, with 200k copies in its first month.
  - [GameDiscoverCo](https://newsletter.gamediscover.co/p/pc-game-discovery-in-china-how-does)
- The top 10 Chinese games with more than 100k sales have over 88% Chinese players. [GameDiscoverCo](https://newsletter.gamediscover.co/p/whats-the-country-split-for-players)

### Inferences
- For a Western survivors-like, China is likely the #1 or #2 market by units if the game has Simplified Chinese. Two comparable roguelikes with data both land in a 39–42% China share (Brotato, The King Is Watching), against an 8–11% all-games baseline. The genre overindexes in China.
- Russian-language players (8.2% of Steam users) and Germany (5.3% of players) are the next largest single markets. Brazil (about 3%) and Japan/Korea (top-20 but smaller) follow.
- For a solo dev, a sensible priority is:
  1. Simplified Chinese.
  2. Russian and German.
  3. Brazilian Portuguese, Japanese and Korean.
- Spanish (4.6% of users) and Traditional Chinese are cheap add-ons worth considering, though they were outside the assigned list.

### Gaps
- No public, verified country split exists for Vampire Survivors, Halls of Torment, Deep Rock Galactic: Survivor, Megabonk or Ball x Pit. VG Insights/Sensor Tower and Gamalytic Pro hold this behind paywalls, and Gamalytic returned HTTP 429 on a Vampire Survivors fetch.
- I could not collect per-language review shares for survivors-likes, which would have been a first-party proxy, because the Steam API was blocked from this environment.

---

## Q2. What measured effects does localization (especially Simplified Chinese) have on sales and reviews, and what are the downsides of poor or machine translation?

### Takeaway
Developer-reported data shows Chinese localization can move China from a marginal market to the top region. Results for other languages are mixed: one dev's 2021 data showed most added languages failed to pay back within six months, apart from Thai. Bad Chinese translation, whether machine-made or merely stilted, is punished with language-specific review bombs. Chinese reviewers are also slightly stricter on average. Steam now shows per-language review scores, which contains the damage to the global score but makes the Chinese score visible to Chinese buyers.

### Cited Findings
**Positive effects (dev-reported or data-firm)**
- Defender's Quest is dev-reported by Lars Doucet and dates from March 2017. [Game Developer](https://www.gamedeveloper.com/business/china-is-kind-of-a-big-deal-for-indie-games)
  - Before Chinese localization, China ranked #22 in lifetime sales. After adding Simplified and Traditional Chinese, China became the #1 region by units and revenue for one week.
  - That week brought 45% of the game's lifetime Chinese revenue, and 50% of copies sold during the sale were in East Asia.
- The King Is Watching localized its demo into Chinese before Steam Next Fest in February 2025, along with progressive localization of the store page, logo, capsule, trailers and news posts.
  - Nearly a third of total demo downloads came from China, and China reached 39% of units.
  - Data is from GameDiscoverCo (August 2025). [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-the-king-is-watching-sold-200k)
- Mortal Glory's China share went from 3% to 24% after CJK localization. This is vendor-published and unverified. [ECI Games](https://www.ecigames.net/media/real-localization-results-how-an-indie-roguelike-grew-unit-sales-with-cjk-localization)

**Mixed results for other languages**
- Academia: School Simulator measured revenue in each language for six months after a March 2021 localization update versus six months before. It already had Japanese, Chinese, German and Spanish. This is dev-reported (Ryan Sumo) via GameDiscoverCo, December 2021. [GameDiscoverCo](https://newsletter.gamediscover.co/p/case-study-how-localization-amps)

  | Language added | Revenue change, 6 months after vs before |
  |---|---|
  | Thai | +331% |
  | Turkish | +8% |
  | Polish | +8% |
  | Brazilian Portuguese | −6% |
  | Russian | −20% (fan translation mods already existed) |
  | Italian | −25% |
  | Indonesian | −34% |

  - Total revenue fell 17% over the same period, so most languages roughly tracked or beat the decline.
  - Only Thai paid back its localization cost within six months. Turkish and Polish were expected to pay back within a year.
- 11 bit studios (Frostpunk, This War of Mine) attributes stable Japanese Steam sales partly to shipping Japanese on day one. This is publisher opinion from 2022. [Automaton](https://automaton-media.com/en/interviews/20220913-15656/)

**Vendor claims (treat with care)**
- Alconost claims store-page localization can "drive 30 to 50% more interest" from non-English markets, with no source given. It also states that Chinese is 27% of Steam play and Russian 9% in 2025. [Alconost](https://alconost.com/en/blog/steam-language-mix-indies)

**Review effects and negative effects**
- GameDiscoverCo found Chinese reviewers about 2% stricter at the median than English reviewers. At the 10th percentile, English opinions were up to 15% more positive. [Gamepressure summarizing GameDiscoverCo](https://www.gamepressure.com/newsroom/do-chinese-gamers-actually-rate-western-games-worse-analysts-have/za7388)
- Steam shows language-specific review scores for games with 2,000+ reviews. For example, Helldivers 2 was "Mostly Positive" (78%) overall but "Mostly Negative" (27%) in Chinese. [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-the-king-is-watching-sold-200k)
- Hollow Knight: Silksong (2025) received about 14,000 negative Chinese reviews over its Simplified Chinese translation.
  - The translation was human-made; complaints centred on an overly flowery, archaic style. Team Cherry promised a new script.
  - Steam's per-language review segregation limited the hit to the global score. [GamesRadar](https://www.gamesradar.com/games/action/as-hollow-knight-silksongs-wonky-chinese-translation-leads-to-over-14-000-negative-steam-reviews-team-cherry-says-well-be-working-to-improve-the-translation-over-the-coming-weeks); [80.lv](https://80.lv/articles/hollow-knight-silksong-s-steam-score-drops-over-poor-chinese-localization)
- Kerbal Space Program (2017) was review-bombed by Chinese players over a translation. Squad admitted it had outsourced the work and could not check quality, and players called it machine-translated. [PCGamesN](https://pcgamesn.com/kerbal-space-program/ksp-review-bombing-chinese-translation)
- A machine-translated Japanese Steam title rendered a game's name as "Sh***y Dungeon". It became a viral joke, an accidental marketing win rather than a review bomb. [PC Gamer](https://www.pcgamer.com/games/rpg/a-game-was-unintentionally-listed-as-sh-y-dungeon-on-steam-in-japan-thanks-to-goofed-up-machine-translation); [Automaton](https://automaton-media.com/en/news/this-mysterious-japanese-indie-game-has-quietly-sold-over-210k-copies/) (search summary)
- Lars Doucet's 2017 advice: a partial translation beats a poor full one, avoid Google-Translate-style machine translation, and localize at least the store page. For minimal-text games, the store page alone may be enough. [Game Developer](https://www.gamedeveloper.com/business/china-is-kind-of-a-big-deal-for-indie-games)

### Inferences
- For a text-light survivors-like, Simplified Chinese is the localization with the strongest evidence of large upside. Adding it to the demo before Next Fest or launch seems to matter, because Chinese creators and Heybox users discover games via demos (see Q4).
- Other languages can fail to pay back for a small game, as Academia's results show, so use Steam wishlist-by-country data to decide on languages after Simplified Chinese.
- The main reputational risk is a visibly bad Chinese translation, because the Chinese-language review score is now shown to Chinese shoppers. At minimum, have a native speaker review machine output (MTPE plus LQA).

### Gaps
- No controlled study measures wishlist conversion with versus without Simplified Chinese for survivors-likes specifically.
- No developer-reported numbers were found for AI or LLM translation outcomes, good or bad, from 2024–2026. Opinions exist (e.g., itch.io comments) but no data.
- A Dig, Dig, Die dev anecdote (China about half of wishlists, then harsh Chinese reviews) appeared in search summaries. I could not pin it to a verifiable URL.

---

## Q3. What do cost and turnaround look like for localizing a small, text-light roguelite into Simplified Chinese, Japanese, Korean, Brazilian Portuguese, Russian and German?

### Takeaway
A survivors-like with roughly 2,000–5,000 words of UI, upgrade text and store page costs roughly $200–750 per language for professional translation, at about $0.10–0.15/word. Japanese is the most expensive and Russian the cheapest. LQA adds about 15–20%, and machine translation with post-editing (MTPE) cuts about 40–50%. Turnaround is roughly one to two weeks end to end for all six languages in parallel. Every figure here is a vendor figure; no dev-reported invoices were found.

### Cited Findings (all vendor or marketing-blog sources)
- Alconost (2026) gives these figures. [Alconost](https://alconost.com/en/blog/steam-language-mix-indies)
  - A systems-led game of about 2,500 words costs $80–150 per language for human translation (its example uses European languages).
  - Three European languages cost $240–450, or roughly $280–540 with 15–20% LQA.
  - MTPE cuts cost by 40–50%.
  - Japanese and Nordic languages are the most expensive tier; CIS languages and parts of Central Europe the cheapest; French, Italian, Spanish and German the middle tier.
- Alconost's timing estimate for a 2,000-word game:
  - Translation takes 2–3 business days per round, plus 2–3 days of LQA.
  - End to end is about one week, plus about one week of prep (glossary, item and character descriptions, style guide).
  - Parallel work scales to about 10–15 languages before timezone friction adds days.
  - [Alconost](https://alconost.com/en/blog/steam-language-mix-indies)
- Allcorrect's public rates are $0.11–0.13/word for English to Simplified Chinese and $0.13–0.15/word for English to Japanese and Traditional Chinese. Its example 1,300-word English-to-CJK job is quoted at about €435 or $390, inconsistent across its pages. [Allcorrect pricing](https://allcorrectgames.com/localization-pricing/); [Allcorrect cost article](https://allcorrectgames.com/insights/how-much-does-localization-cost/)
- An industry benchmark puts professional game translation at $0.10–0.18/word, averaging about $0.14. [VoxBooster](https://voxbooster.com/blog/game-localization-statistics-2026)
- LocalizeDirect says proofreading usually costs 50% of the translation rate. [LocalizeDirect](https://localizedirect.com/posts/which-languages)
- A store page alone runs about 500–1,000 words at $100–300 per language. A full mid-size indie game costs about $3,000–5,000 per language. These are marketing-blog estimates. [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/steam-localization-languages)

### Inferences
- These are my calculations from the vendor rates above, not quotes:
  - At 4,000 words and $0.10–0.15/word, each language costs about $400–600. Six languages (Simplified Chinese, Japanese, Korean, Brazilian Portuguese, Russian, German) come to roughly $2.5k–3.6k, plus about 15–20% LQA, for roughly $3k–4.3k.
  - MTPE would bring that to roughly $1.5k–2.2k.
  - Store-page-only localization for six languages costs roughly $600–1,800.
- A practical solo-dev sequence:
  1. Localize the store page plus short description into all six languages, using MTPE reviewed by native speakers.
  2. Fully localize the game and demo into Simplified Chinese with professional translation and LQA.
  3. Add the other languages as wishlist-by-country data justifies them.
- Technical prep (CJK fonts and glyph fallback, text expansion for German and Russian, string externalization) is a fixed one-time cost. It is often the real time sink for solo devs, more than the translation itself.

### Gaps
- No dev-reported invoices or timelines were found for survivors-likes in 2023–2026.
- No Korean-specific per-word rate was found; Allcorrect groups Korean with Japanese for hourly LQA.
- No data was found on the quality and cost of LLM-only translation versus MTPE for games.

---

## Q4. How do indie devs get covered by Bilibili and other Chinese creators and press, and what results are reported? What are the free or organic routes in China, Japan, Korea, Brazil and Russia?

### Takeaway
In China, discovery runs through Bilibili and Douyin video creators, plus Heybox (小黑盒), a Steam companion and shadow-store app. Prerequisites are a Chinese-localized demo and store page, plus your own Bilibili or Heybox presence. Reported wins (tens of thousands of wishlists from one creator series) come mostly from agencies or publishers. In Japan, well-packaged Japanese-language press emails to outlets and their X accounts can generate large organic reach. Evidence for organic routes in Korea, Brazil and Russia is thin.

### Cited Findings: China
- Spiral Up Games' Aldric Chang: "Our main sources of traffic are Bilibili and Douyin." Douyu hosts long-form archived streams.
  - Organic creator coverage is especially valuable when a creator features a game in depth.
  - Wandering Sword's top Bilibili video passed 700k views.
  - Steam China, the ISBN-licensed store, is separate from global Steam. Global Steam is not banned, so most Western indies reach Chinese players without an ISBN.
  - GameDiscoverCo, January 2024. [GameDiscoverCo](https://newsletter.gamediscover.co/p/pc-game-discovery-in-china-how-does)
- The King Is Watching (publisher-reported via GameDiscoverCo, August 2025):
  - Bilibili creator 王老菊 (Wang Laoju) generated more than 750k views.
  - About 20% of the paid media budget went to China, and a local agency selected and managed influencers. This was not purely organic.
  - [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-the-king-is-watching-sold-200k)
- Heybox (GameDiscoverCo, April 2026, paywalled excerpt). [GameDiscoverCo](https://newsletter.gamediscover.co/p/inside-the-chinese-steamconsole-companion)
  - It acts as a "shadow store" for Steam, with "many millions of MAU" and a store section that is likely its second-largest traffic hub.
  - It sells developer-provided Steam keys, with a public best-sellers chart, and runs its own most-wishlisted chart.
  - Partners can enable a wishlist sync to Steam.
  - Games can gain visibility through user posts without any commercial deal, and devs can run official dev channels.
  - GameDiscoverCo speculates that Chinese players wishlist less on Steam because they wishlist on Heybox.
- Huqiao (vendor/agency claims, unverified):
  - Electronic Repair Simulator gained about 50,000 wishlists in one month from one creator's Bilibili/Douyin series.
  - Butterscotch Shenanigans drew 500k video views in a month from organic coverage; Heybox wishlists rose 21% and China became the top wishlist region.
  - Animal Shelter 2 drew 140k views and more than 1,000 wishlists.
  - Clustered creator releases produce wishlist spikes within 48–72 hours.
  - Creator tiers: macro 100k+ followers, mid 20k–100k, micro 5k–20k. Micro creators may accept keys instead of fees.
  - [Huqiao](https://www.huqiaogames.com/insights/bilibili-game-marketing-guide-for-western-aa-studios)
- Huqiao's conference deck (vendor):
  - Its playbook is 3–10 Bilibili and Douyin videos per campaign, paired with Heybox, plus outreach and thank-you posts from the developer's own account.
  - It lists prerequisites: Simplified Chinese localization, at least 15% of wishlists already from China, and a phone-verified Bilibili account.
  - Claimed results: 31% of one client's wishlists came from China, about 45k wishlists came from Heybox alone, and Infection Free Zone got 80% of its Next Fest 2023 traffic from China.
  - [SlideShare – Huqiao/FlashGAMM](https://www.slideshare.net/slideshow/how-to-increase-wishlists-game-sales-from-china-growth-marketing-tactics-case-study-wojciech-jaworski-huqiao/259117225)
- A consultant claims 44.5% of Chinese gamers find new games through short-form video such as Douyin. [Recognizing Patterns](https://recognizingpatterns.substack.com/p/congratulations-you-ignored-the-chinese)
- Industry commentary describes the typical channel mix:
  - Douyin and Xiaohongshu for mass reach.
  - Bilibili and Heybox as core-gamer hubs.
  - Weibo for amplification.
  - A KrASIA piece argues Xiaohongshu has become "harder for game marketers to ignore" (search summary; not read in full). [KrASIA](https://kr-asia.com/why-xiaohongshu-has-become-harder-for-game-marketers-to-ignore)
- Bilibili was also a partner in Dead Cells reaching 5 million Chinese sales, an older example. [PocketGamer.biz](https://www.pocketgamer.biz/bilibili-passes-300m-monthly-users-as-dead-cells-hits-five-million-chinese-sales)

### Cited Findings: Japan
- SIGONO (OPUS: Prism Peak) published a pitching guide in December 2023, dev-reported by its marketing manager. [Game Developer](https://gamedeveloper.com/marketing/tapping-into-top-tier-japanese-media-our-indie-game-s-unprecedented-success)
  - Send formal Japanese-language emails with total attachments under 5MB.
  - Include crop-free vertical and horizontal key art under 1MB each, and a GIF under 1MB that auto-plays in iPhone mail.
  - Attach a Japanese press kit, and call the trailer "PV".
  - Write Steam-length copy that outlets can reuse, and add awards and endorsements.
  - Include Japanese social links in the signature.
  - One Denfaminicogamer GIF post reached 380k views.
  - Japanese language support is "preferred but doesn't strongly affect coverage". If the game lacks it, say so in Japanese.
- Automaton reports that Japanese social-media virality, as in the "Sh***y Dungeon" mistranslation, can drive organic attention. [PC Gamer](https://www.pcgamer.com/games/rpg/a-game-was-unintentionally-listed-as-sh-y-dungeon-on-steam-in-japan-thanks-to-goofed-up-machine-translation)

### Cited Findings: Korea, Russia, Brazil, Germany
- Korea: Automaton reports Shuhei Yoshida saying overseas publishers overlook Korean indies, with Devolver the only international indie publisher at BIC 2025. This is market context, not an outreach tactic. [Automaton](https://automaton-media.com/en/?p=51018) (search summary)
- Korea: Metaps advised finding a local partner for Japan or Korea launches, and said Korean players move on quickly from buggy or stale games. This is an older, mobile-focused source. [PocketGamer.biz](https://www.pocketgamer.biz/looking-to-crack-japan-dont-stress-over-localisation-says-metaps)
- Russia: Valve paused bank payouts to Russia in 2022 and later required intermediary bank details. [Valve press release](https://store.steampowered.com/news/6568/)
  - Russian buyers reportedly use workarounds such as topping up via Kazakhstan; a 2026 report estimates Russians spend about $31M a year bypassing the restrictions. [Mezha](https://mezha.ua/en/news/rosiyani-vitrachayut-31-mln-shchorichno-na-obhid-obmezhen-v-steam-310097/)
- Germany: Halls of Torment's breakout was driven by Twitch streamer Asmongold, per German press. That is an English-language creator mechanism, not a German-specific one. [Mein-MMO](https://mein-mmo.de/asmongold-twitch-steam-hit-aus-stuttgart-halls-of-torment/); [GameStar](https://www.gamestar.de/artikel/halls-of-torment-steam-asmongold,3397299.html)

### Inferences
- A free or low-cost China playbook for a solo dev:
  1. Localize the demo and store page into Simplified Chinese before Next Fest.
  2. Open a phone-verified Bilibili account and an official Heybox dev presence, and post devlogs and GIFs.
  3. Email or DM mid-tier and micro Bilibili/Douyin creators who cover roguelites, offering Steam keys. Huqiao says micro creators may accept keys instead of fees.
  4. Thank creators publicly from the official account.
- Some reported Chinese successes involved agencies or paid budgets. Purely organic Western-indie results in China are under-documented.
- For Japan, the SIGONO packaging checklist is free and actionable: Japanese email, GIFs for X, reusable copy. Automaton, 4Gamer, Famitsu and Denfaminicogamer all run X accounts where GIFs travel.

### Gaps
- I found no first-hand Western-indie accounts of organic coverage by Steam China curators such as 篝火/Gcores, by Xiaohongshu, or by Douyin creators, with measured results.
- No Korean-specific organic outreach data (Naver Cafe, Korean YouTubers) was found.
- No Brazilian creator or outlet outreach data was found.
- Little Russian creator or outlet data was found beyond payment context.
- I could not trace two claims to a verifiable URL: Heybox "50M registered / 5M DAU", and a developer anecdote that Heybox key sales matched Steam sales 1:1 (10k + 10k). Both came only from search summaries.

---

## Q5. What are the regional pricing recommendations for these markets?

### Takeaway
Start from Valve's recommended regional prices, which are well below USD in China, Russia/CIS and Brazil. Evidence suggests setting China at or slightly below Valve's suggestion for an indie, mainly to drive word of mouth. Price cuts alone don't create demand without localization and fit.

### Cited Findings
- The King Is Watching set its China launch price slightly below Steam's suggested regional price, to reflect purchasing power and encourage word of mouth. Base price is €15. [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-the-king-is-watching-sold-200k)
- Valve's recommended CNY prices typically sit 40–60% below USD. This is a third-party marketing blog, not Valve. [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/steam-regional-pricing-guide)
- With regional pricing, revenue per Chinese player is about 47% of a US player's. This is an older source (around 2018–19). [Game Developer – Steam in China](https://www.gamedeveloper.com/business/steam-in-china)
- Valve updated its regional pricing tools in 2026, covering 37 currencies and using exchange rates plus purchasing-power data. The tools are advisory and developers keep control. [PCGamesN](https://www.pcgamesn.com/steam/regional-pricing-tools-2026)
- Counter-example: Forza Motorsport cut its China price 58% on the entry tier and saw no measurable lift, while Stellar Blade sold well at ¥268 against a $60 US price. Price alone didn't decide outcomes. This is a consultant analysis from May 2026. [Recognizing Patterns](https://recognizingpatterns.substack.com/p/congratulations-you-ignored-the-chinese)
- Lost Castle, a Chinese indie, got about 70% of its 200k paid units from China after language and content localization, cheaper pricing and well-timed sales. Older, around 2017; from a search summary. [AList](https://www.alistdaily.com/strategy/lost-castle-publisher-leverages-steam-succeed-china/)

### Inferences
- For a $5–10 survivors-like, use Valve's recommended prices for Russia/CIS, Brazil, Turkey and similar regions. Consider China at or slightly below Valve's suggestion. The genre leader Brotato launched cheap ($4.99), and low price is part of the survivors-like value proposition.
- Russian payment frictions mean Russian-language sales may route through CIS regions such as Kazakhstan. Keep CIS regional prices consistent to avoid arbitrage complaints.

### Gaps
- No survivors-like-specific data was found on price elasticity in China, Brazil or Russia.
- I could not verify the source behind a "21–37% lower than Western benchmarks" China pricing claim from a 2025 industry report.

---

## Q6. Case studies: Western indie roguelites that broke out in China or Asia, and the mechanism

### Takeaway
The best-documented mechanism, from The King Is Watching and supported by Brotato's China share, is: Chinese-localized demo early, then Bilibili creator coverage plus Heybox, then China becoming the top unit market at a slightly-below-recommended price. For the big survivors-likes (Vampire Survivors, Megabonk, Ball x Pit, Halls of Torment, Deep Rock Galactic: Survivor), sales totals are public but China splits and mechanisms are not.

### Cited Findings
- **Brotato:** Gamalytic estimates about 41.6% of its players in China, the single largest country. No developer statement on the mechanism was found. [Gamalytic](https://gamalytic.com/game/1942280)
- **The King Is Watching** (roguelike, 2025):
  - 39% of units came from China.
  - Mechanism: a Chinese demo before Next Fest; a Bilibili video from 王老菊 with more than 750k views; agency-managed influencers; about 20% of the paid budget spent on China; China priced slightly below Valve's suggestion.
  - [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-the-king-is-watching-sold-200k)
- **Vampire Survivors:** added Korean, Chinese, Japanese, German, French and Spanish translations around 2022. Its all-time Steam peak was 77,061 concurrent players in February 2022. No China split was found. [Gamepressure](https://gamepressure.com/newsroom/vampire-survivors-still-popular-creator-thanks-fans/zc3fab); [SteamDB](https://steamdb.info/app/1794680/graphs)
- **Halls of Torment:** an estimated 825.6k Steam copies (third-party estimate). Its breakout was driven by Asmongold's Twitch coverage, with no Asia mechanism documented. [Raijin.gg](https://raijin.gg/app/2218750/Halls_of_Torment); [Mein-MMO](https://mein-mmo.de/asmongold-twitch-steam-hit-aus-stuttgart-halls-of-torment/)
- **Megabonk:** sold 1M copies in two weeks (dev-reported) in 2025. Third-party estimates since range from 1.3M to 5M. No country split was found. [GamesRadar](https://www.gamesradar.com/games/roguelike/out-of-nowhere-roguelike-hit-megabonk-has-sold-1-million-copies-in-2-weeks-solo-creator-says-ill-be-eating-spaghetti-with-extra-sauce-tonight/); [Sensor Tower VGI](https://app.sensortower.com/vgi/game/megabonk)
- **Ball x Pit:** 300k copies in 5 days and 400k in the first week. It passed 1M by December 2025 and 2M by August 2026, across platforms. It ships Simplified Chinese, Traditional Chinese, Japanese, Korean and Thai on PlayStation Asia. No country split was found. [GameSpot](https://www.gamespot.com/articles/ball-x-pit-is-rolling-with-400000-copies-sold-in-first-week/1100-6535686/); [Gematsu](https://www.gematsu.com/2025/12/ball-x-pit-sales-top-one-million-three-free-content-updates-set-for-2026); [GoNintendo](https://gonintendo.com/contents/55474-ball-x-pit-clears-2-million-copies-sold-big-exciting-news-teased-update); [PlayStation HK](https://www.playstation.com/zh-hans-hk/games/ball-x-pit/)
- **Deep Rock Galactic: Survivor:** no sales or regional data was found.
- **Western non-roguelite comparison:** Academia: School Simulator gained +331% Thai revenue after Thai localization (2021, dev-reported). Southeast Asian languages can overperform for cheap indies. [GameDiscoverCo](https://newsletter.gamediscover.co/p/case-study-how-localization-amps)

### Inferences
- The likely shared mechanism for survivors-likes in China:
  - Low price.
  - Little text, so localization is cheap and the game is accessible even partly translated.
  - High "watchability" on Bilibili and Douyin.
  - Steam regional pricing plus Heybox key sales.
- This is consistent with the data above (Brotato about 42% China, roguelikes ranking high for Chinese ownership) but not proven for any single survivors-like.

### Gaps
- No public postmortem from poncle, Blobfish, Chasing Carrots, Vedinad, Kenny Sun or Funday Games breaks down China or Asia sales or describes Chinese marketing.
- Chinese-language trade sources (Gamera, Indienova, Gcores/篝火 talks) were not reached in this pass. A Gcores article (gcores.com/articles/24440), seen only in a search snippet, quotes XD's Brandy Wu saying Chinese players prefer cheap pricing but are increasingly used to buy-to-play on Steam. I did not read the full text or confirm its date.
