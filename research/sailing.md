# Sailing / Cruising — Phase 2 Demand + Competition

**Research date:** 2026-08-10
**Method note:** This session's egress proxy blocks all apple.com domains, so the iTunes Search API and the App Store customer-reviews RSS feed were unreachable (confirmed via curl and WebFetch — both returned EGRESS_BLOCKED). All data below was gathered via the WebSearch tool only, which surfaces Apple App Store URLs and third-party aggregator snippets (AppFollow, JustUseApp, AppBrain, MWM, casualnavigation.com, etc.) rather than live App Store page data. Every figure is attributed to the query/source that produced it and marked "unverified" where no source gave a hard number.

## Search methodology (queries run)

1. `sailing app iphone app store`
2. `site:apps.apple.com sailing`
3. `marine navigation app ios app store`
4. `sailing logbook app ios`
5. `ASA sailing certification app ios`
6. `iNavX marine navigation app store rating reviews price`
7. `SeaNav app store rating reviews price subscription`
8. `SailFlow app store rating reviews price`
9. `Navionics Boating app store rating reviews price ios`
10. `PredictWind app store ios rating reviews price`
11. `Sail Racer app store rating reviews last updated`
12. `SailTies logbook app store rating reviews price`
13. `"Marine Navigation" app id528948720 rating reviews last updated version`

## Apps found

All entries below have a real, working `apps.apple.com` URL returned directly by WebSearch. Fields not confirmed by a specific source snippet are marked "unverified."

| # | App name | Developer / seller | App Store URL | Price | Rating | Rating count | Last updated |
|---|----------|--------------------|--------------------|-------|--------|---------------|---------------|
| 1 | iNavX: Marine Navigation | iNavX / Rite-Size (per aggregator pages; developer name unverified from a first-party source) | https://apps.apple.com/us/app/inavx-marine-navigation/id286616280 | $4.99 one-time + chart subscriptions $9.99–$199.99/yr (per casualnavigation.com / aggregator snippets) | 4.76–4.8 / 5 (two different sources gave 4.76 and 4.8; treated as consistent, high) | 19.4K (per justuseapp.com aggregator, not first-party) | unverified — not found |
| 2 | SeaNav (US) | SeaNav Ltd (per app description text, not independently confirmed) | https://apps.apple.com/us/app/seanav-us/id632635827 | Free app; chart subscription $9.99/yr (per casualnavigation.com) | unverified — not found | unverified — not found | unverified — not found |
| 3 | SailFlow: Sailing Forecasts | WeatherFlow (per appgrooves.com listing "SailFlow by WeatherFlow") | https://apps.apple.com/us/app/sailflow-sailing-forecasts/id555309964 | Free + tiers: Plus $3.99/mo or $44.99/yr, Pro $9.99/mo or $119.99/yr, Gold $14.99/mo or $179.99/yr (per appfollow.io / justuseapp.com) | 4.7 / 5 (per appfollow.io) | unverified — not found (appgrooves.com mentions "2,462 reviews" but that figure's platform/scope is unclear, so not trusted as an App Store count) | unverified — not found |
| 4 | Navionics® Boating | Navionics (self-named in listing) | https://apps.apple.com/us/app/navionics-boating/id744920098 | Free with 2-week Navionics+ trial, then $9.99/yr subscription (per appbrain.com/yachtingworld.com snippets) | 2.9 / 5 | 2.3K ratings | unverified — not found |
| 5 | PredictWind — Marine Forecasts | PredictWind Limited (per amazon.com listing "PredictWind Limited") | https://apps.apple.com/us/app/predictwind-marine-forecasts/id477048487 | Free download; paid Standard/Professional plans ~$190–$330/yr (per moneyformangos.com review) | 4.80 / 5 | 32.1K reviews | unverified — not found (requires iOS 15.5+, per aggregator) |
| 6 | ASA's Sailing Challenge | American Sailing Association (ASA) | https://apps.apple.com/us/app/asas-sailing-challenge/id1109489005 | $3.99 with in-app purchases | 4.8 / 5 | 2.8K ratings | unverified — not found (requires iOS 11.0+) |
| 7 | Sail Racer | Sailracer.net (inferred from Google Play package name `sailracer.net`; not confirmed for iOS listing) | https://apps.apple.com/us/app/sail-racer/id473901816 | unverified — not found | unverified — not found (Aptoide, a non-App-Store source, showed 5-star, not usable as App Store rating) | unverified — not found | unverified — user complaints in reviews reportedly say "not updated in 7 years"; no confirmed date found. Treat as anecdotal, not verified. |
| 8 | SailTies: Logbook & Sailing CV | SailTies (self-named in listing) | https://apps.apple.com/gb/app/sailties-logbook-sailing-cv/id1507376381 | Free (per appbrain.com) | 4.95 / 5 (iOS, per appbrain.com aggregator) | 150 ratings (iOS, per appbrain.com aggregator) — below the 200-rating threshold used in flag #1 below | unverified — not found |
| 9 | Marine Navigation | Marco Palaferri (per app description snippet: "Since 2009...") | https://apps.apple.com/us/app/marine-navigation/id528948720 | One-time purchase full version, or PRO subscription option (exact price unverified — not found) | 2.9 / 5 | 2,000+ reviews (approximate, per aggregator snippet) | unverified — not found |
| 10 | i-Boating: Marine Charts & GPS | unverified — not found | https://apps.apple.com/us/app/i-boating-marine-charts-gps/id994992062 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |

Other real apps that surfaced in search but were not deep-dived (URL confirmed, all other fields unverified): Vantage Sailing (`id6544807723`), Sail Routing (`id6756657427`), KWINDOO Tracking for sailing (`id974955770`), SailSim – Sailing Simulator (`id6464166885`), Go Sailing (`id622198686`), 2Sail Sailing Simulator (`id1536527598`), Sailing World Tour Adventures (`id6618158512`), Argo Navigation: Boat GPS, Map (`id1463869636`), Boating Logbook: Skipper (`id671764434`), Ship's Log Book for Captains (`id533244045`), LogBook — Digital Yacht Log (`id6762569859`), Saillogger (web app with dedicated iOS app, per saillogger.com — App Store URL not directly surfaced).

## Opportunity flags

- **Top apps average <4.0 stars with >200 ratings: MIXED / UNCLEAR (leans False for the category leaders).**
  The two highest-visibility apps with large, confirmed rating counts are strong: PredictWind (4.80/5, 32.1K ratings) and iNavX (4.76–4.8/5, ~19.4K ratings, aggregator-sourced). ASA's Sailing Challenge (4.8/5, 2.8K ratings) and SailFlow (4.7/5, count unverified) are also well above 4.0. However, two general marine-navigation apps that surfaced prominently — Navionics® Boating (2.9/5, 2.3K ratings) and Marine Navigation (2.9/5, ~2,000+ reviews) — are both below 4.0 with >200 ratings, driven by reported technical/reliability complaints. So the flag is true for a subset of well-known apps but false for the category leaders by rating count (PredictWind, iNavX). Net verdict: does not indicate broad, uniform under-satisfaction — mixed.

- **Top apps not updated in >18 months: UNCLEAR — insufficient data.**
  No source returned a confirmed "last updated" date or version-history timestamp for any of the 10 apps (this is exactly the data iTunes Search API would normally supply, and it was unreachable). The only signal was an anecdotal, unverified claim in review snippets that Sail Racer "has not been updated in 7 years." That is a single, unconfirmed data point for one minor app, not evidence about the category leaders. Cannot be assessed reliably without App Store access.

- **Top 3 results are all free/ad-supported with no paid alternative: FALSE.**
  The category has clear paid options: iNavX is a $4.99 one-time purchase plus paid chart subscriptions up to $199.99/yr; Marine Navigation offers a one-time-purchase full version; ASA's Sailing Challenge is a flat $3.99 paid app; PredictWind's core value (departure planning, weather routing) sits behind $190–330/yr paid plans; SailFlow gates features behind $3.99–$14.99/mo tiers. Free-with-IAP/subscription is the dominant model, but genuine free-only, ad-supported apps were not the norm among the higher-profile results.

- **Fewer than 5 genuinely matching results (niche underserved): FALSE.**
  WebSearch surfaced well over 10 distinct, real, sailing/marine-relevant iOS apps across multiple sub-categories: navigation/chartplotting (iNavX, SeaNav, Navionics, Marine Navigation, i-Boating, Argo Navigation), weather/routing (SailFlow, PredictWind), logbooks (SailTies, Boating Logbook: Skipper, Ship's Log Book for Captains, LogBook, Saillogger), racing/tactics (Sail Racer, Sailrace, KWINDOO), and education/certification (ASA's Sailing Challenge). The niche is not underserved in raw count — it has established, long-running incumbents (iNavX since ~2009-era, PredictWind, Navionics) with large review bases (19.4K–32.1K ratings for the leaders), which is a sign of real, proven demand but also of high competitive/incumbency barriers.

## Overall assessment

The sailing/cruising niche shows genuine, proven demand (multiple incumbents with tens of thousands of ratings and years of operation) but is not underserved — navigation and weather-routing are dominated by entrenched, well-rated, well-monetized players (PredictWind, iNavX, Navionics) that would be hard to displace, while a few adjacent sub-niches (digital logbooks, ASA-style certification prep) look thinner and less saturated, with SailTies as a notable example of a small, highly-rated (4.95/5) but low-volume (150 iOS ratings) app that suggests room for a better-executed logbook or cert-prep product. Confidence in this assessment is low-to-moderate: rating counts, prices, and especially "last updated" dates could not be verified against a first-party source (iTunes Search API was blocked for this session) and instead rely on third-party aggregator snippets that may be stale or inconsistent with the live App Store.

---

## Phase 3 — Pain Mining

**Research date:** 2026-08-10
**Method note:** Same egress restriction as Phase 2 — `apple.com` domains confirmed blocked. This phase additionally attempted `WebFetch` on ~9 non-Apple domains (pissedconsumer, justuseapp, YBW forum, iFish forum, marlvel.ai) to pull full review text; **every one returned `EGRESS_BLOCKED`**, not just apple.com. So this entire phase relies on `WebSearch` result snippets only — i.e., Claude's search tool summarizing/paraphrasing what it saw on those pages, not raw page content Claude read directly. Any "quote" below is a short phrase that appeared verbatim inside a WebSearch snippet and is attributed to the source page; none of it was independently confirmed by opening the source page itself. Treat quotes as likely-real-but-unverified, and treat all counts as floors (minimum distinct mentions found), not exhaustive tallies.

### Incumbents reviewed

- **Navionics® Boating** (id744920098) — per Phase 2, 2.9★/2.3K ratings (one aggregator this phase gave 2.8★/49.8K reviews, another gave 2.9★/2,079 reviews — figures are inconsistent across aggregators and unverified against a first-party source, but all agree the app sits well under 3★ despite huge volume). Chosen per task instructions as one of the two weakest-rated incumbents with real review volume.
- **Marine Navigation** (id528948720, dev: Marco Palaferri) — per Phase 2, 2.9★/2,000+ reviews. Chosen per task instructions as the second weakest-rated incumbent with real review volume.

No substitution was made — WebSearch did surface some review-adjacent content for iNavX and PredictWind, but both are 4.7-4.8★ and searches for their complaints returned mostly praise, confirming Phase 2's read that they are the strong category leaders rather than pain sources.

### Complaint themes

**Navionics® Boating**

| Theme | Distinct mentions found | Quotes / paraphrase | Source(s) |
|---|---|---|---|
| Subscription pricing anger / billing errors | 6 | "150-400% price hikes and loss of legacy access" driving what one aggregator calls a "crisis of user trust"; reports of denied refunds and double charges; one user says the app "cancels those services after a short period and leaves users without the service they already paid for, with no way to get money back"; a "subscription verification loop" bug where the app "fails to recognize an active purchase" and, after paying again, "wouldn't allow them to use the app" — discovering they'd been billed twice. Separately, a concrete price-hike data point: the US & Canada chart package rose from $24.99 to $49.99 (a ~66% jump per one forum poster, "150-400%" per the aggregator across different regions/tiers) | [justuseapp.com](https://justuseapp.com/en/app/744920098/boating-marine-lakes/reviews), [marlvel.ai](https://marlvel.ai/intel-report/navigation/navionics-boating), [PissedConsumer](https://navionics.pissedconsumer.com/review.html), [cruisersforum.com](https://www.cruisersforum.com/forums/f121/navionics-price-increase-10-to-50-a-280870.html), [forums.sailboatowners.com](https://forums.sailboatowners.com/threads/navionics-price-increasing.1249938013/), [jetboaters.net](https://jetboaters.net/threads/navionics-price-increase.38632/), [thehulltruth.com](https://www.thehulltruth.com/marine-electronics-forum/1296910-navionics-app-price-increase.html), [yachtforums.com](https://www.yachtforums.com/threads/navionics-boating-app-subscription-price-increase.37861/) |
| App freezes / hangs / crashes | 3 | "software graphing routine problems causing the app to randomly hang during map graphing updates"; navigation freezes described by users as making the app a "danger to safe navigation"; a long-time (3-year) user says they "can't depend on the app working" because it "often loses track of location or fails to start tracking" | [justuseapp.com](https://justuseapp.com/en/app/744920098/boating-marine-lakes/reviews), [marlvel.ai](https://marlvel.ai/intel-report/navigation/navionics-boating), [PissedConsumer](https://navionics.pissedconsumer.com/review.html) |
| GPS / location accuracy | 4 | reports of position showing "100-200ft north of where they actually are"; boat shown "at 200'" on chart vs "350'" on a real sounder; app showing the boat "approaching a mark" it had already passed; a dedicated Apple Support Communities thread titled "NO GPS with iPad in Navionics Boating App" | [forums.ybw.com](https://forums.ybw.com/threads/using-only-navionics-app-for-navigation-accuracy-and-dependency.499066/), [iceshanty.com](https://www.iceshanty.com/threads/issues-with-navionics-app-gps-accuracy.342184/), [sportfishingbc.com](https://sportfishingbc.com/threads/navionics-apps-not-accurate-issue.73667/), [discussions.apple.com](https://discussions.apple.com/thread/255074557) |
| Feature regressions / limitations | 2 | users "unable to follow created routes"; app reportedly can't be used on planned routes "longer than 20 miles," limiting its use as a route-planning tool | [justuseapp.com](https://justuseapp.com/en/app/744920098/boating-marine-lakes/reviews) |
| Fuel-usage calculation bug (post-update) | 1 | an update reportedly broke fuel projection, showing "71.7 gallons instead of 19.5 gallons" for the same 45-minute trip | [justuseapp.com](https://justuseapp.com/en/app/744920098/boating-marine-lakes/reviews) |
| Poor customer support | 2 | "poor customer service response times"; "difficulty with app activation, syncing, and chip updates" | [justuseapp.com](https://justuseapp.com/en/app/744920098/boating-marine-lakes/reviews), [PissedConsumer](https://navionics.pissedconsumer.com/review.html) |

**Marine Navigation (Marco Palaferri)**

| Theme | Distinct mentions found | Quotes / paraphrase | Source(s) |
|---|---|---|---|
| "Scam" / refund refusal | 3 | "I hate getting ripped off and this is a total scam! Multiple emails with no response. Requested a refund twice with no response."; "don't download this app, it's a scam, especially the paid version"; a user who paid "$9" for the Australia charts said the app "just frustrates me more. And the maps for Australia are a real joke" | WebSearch snippets citing Marine Navigation reviews (page URLs not individually resolvable — aggregated via [apps.apple.com/us/app/marine-navigation/id528948720](https://apps.apple.com/us/app/marine-navigation/id528948720) review excerpts surfaced in search) |
| GPS location wildly off | 1 | "Don't waste your money" — location pin "can be up to 10 miles away from the actual point" | same as above |
| Crashes / maps fail to download | 1 (aggregate, not individually countable) | "GPS not working, maps failing to download or display correctly, and frequent crashes" reported as a common pattern | same as above |
| Free "Lite" version non-functional (blocks evaluation before purchase) | 1 | "How are you suppose to evaluate a program when the functions in the Lite version don't work?" | [appgrooves.com](https://appgrooves.com/app/marine-navigation-lite-by-marco-palaferri) |

**Explicit honesty note:** no full raw review text (username, date, star count, full body) was directly readable in this session — every quote above came through a WebSearch-generated summary of a third-party review-aggregator page, not a page Claude opened and read itself. The underlying reviews are very likely real (the phrasing is idiosyncratic and specific, not generic), but they should be treated as "probably real, unverified provenance" rather than confirmed primary-source quotes.

### Forum/reddit signal

Reddit-specific searches came up **empty** — `site:reddit.com` queries for "Navionics app store review," "r/sailing app recommendation navigation," "sailing is there an app that," "r/boating Navionics complaint," and "wish there was an app" all returned zero Reddit URLs (Google/Bing indexing of r/sailing and r/boating app-recommendation threads appears thin, or WebSearch's Reddit coverage is limited for this niche). Stating this plainly rather than fabricating thread links.

Non-Reddit forum threads that **were** found (boating/sailing forums function as this niche's "Reddit" — much more active than actual Reddit for this topic):

- [cruisersforum.com — "Navionics Price increase...$10 to $50?"](https://www.cruisersforum.com/forums/f121/navionics-price-increase-10-to-50-a-280870.html) — cruisers reacting to a large Navionics subscription price jump; mixed anger/resignation.
- [forums.sailboatowners.com — "Navionics price increasing"](https://forums.sailboatowners.com/threads/navionics-price-increasing.1249938013/) — same price-increase controversy, sailboat-owner audience.
- [jetboaters.net — "Navionics price increase"](https://jetboaters.net/threads/navionics-price-increase.38632/) — same topic, powerboat audience (signal that pricing anger spans boating sub-niches, not sailing-specific).
- [thehulltruth.com — "Navionics App Price Increase"](https://www.thehulltruth.com/marine-electronics-forum/1296910-navionics-app-price-increase.html) — same topic.
- [yachtforums.com — "Navionics Boating App Subscription Price Increase"](https://www.yachtforums.com/threads/navionics-boating-app-subscription-price-increase.37861/) — same topic, yacht-owner audience.
- [forums.ybw.com — "Navionics boating app subscription"](https://forums.ybw.com/threads/navionics-boating-app-subscription.613070/) — UK forum, subscription-model complaints.
- [forums.ybw.com — "Using only Navionics (app) for navigation - accuracy and dependency?"](https://forums.ybw.com/threads/using-only-navionics-app-for-navigation-accuracy-and-dependency.499066/) — sailors debating whether the app's GPS accuracy is trustworthy enough as a sole navigation source.
- [ifish.net — "More Navionics / Boating App changes - for the bad in my opinion"](https://www.ifish.net/threads/more-navionics-boating-app-changes-for-the-bad-in-my-opinion.1699262/) — user-perceived regression after an app update.
- [iceshanty.com — "Issues with Navionics App GPS Accuracy"](https://www.iceshanty.com/threads/issues-with-navionics-app-gps-accuracy.342184/) — GPS accuracy complaints.
- [sportfishingbc.com — "Navionics apps not Accurate issue"](https://sportfishingbc.com/threads/navionics-apps-not-accurate-issue.73667/) — same theme.
- [discussions.apple.com — "NO GPS with IPAD in Navionics Boating App (08/2023)"](https://discussions.apple.com/thread/255074557) — official Apple support-community thread, GPS not functioning at all.
- [cruisersforum.com — "iPhone App for Vessel Log Book?"](https://www.cruisersforum.com/forums/f13/iphone-app-for-vessel-log-book-219748.html) — a cruiser explicitly **asking the community for an iOS logbook app** because they hadn't found one they liked — direct unmet-demand signal for the logbook sub-niche.
- [cruisersforum.com — "Log Book and Anchor Apps for Android"](https://www.cruisersforum.com/forums/f2/log-book-and-anchor-apps-for-android-204228.html) — same ask, Android.
- [cruisersforum.com — "Best Apps for Navigation"](https://www.cruisersforum.com/forums/f121/best-apps-for-navigation-252544.html) — general navigation-app recommendation thread.
- [cruisersforum.com — "Logbook / Maintenance Software"](https://www.cruisersforum.com/forums/f90/logbook-maintenance-software-234143.html) — recurring ask for combined logbook + maintenance tracking, a gap none of the Phase 2 logbook apps appear to fill.
- [cruisersforum.com — "Advice requested re: navigation apps"](https://www.cruisersforum.com/forums/f121/advice-requested-re-navigation-apps-246798.html) — another navigation-app recommendation ask.
- [cruisersforum.com — "SailLogger, a self-made system & app for logbook"](https://www.cruisersforum.com/forums/f121/saillogger-a-self-made-system-and-app-for-logbook-222256.html) — notable: a user built their **own** logbook system/app rather than use an existing one — strong signal that available logbook apps weren't good enough.
- [cruisersforum.com — "Digital Logbook software"](https://www.cruisersforum.com/forums/f121/digital-logbook-software-265807.html) — another logbook-software ask.
- [cruisersforum.com — "Sailing log apps"](https://www.cruisersforum.com/forums/f71/sailing-log-apps-177555.html) — another logbook-app ask/discussion.
- [cruisersforum.com — "Digital Log Books"](https://www.cruisersforum.com/forums/f129/digital-log-books-246257.html) — another logbook-app discussion.
- [forums.sailinganarchy.com — "Accuracy and timeliness of navigation apps"](https://forums.sailinganarchy.com/threads/accuracy-and-timeliness-of-navigation-apps.246078/) — racers/sailors comparing navigation-app accuracy/reliability.

Note: none of these forum URLs were opened directly (WebFetch blocked on every one tried); the descriptions above are WebSearch's summary of thread titles/snippets, not confirmed by reading full thread content.

### Feature spec implied

Based on the clustered complaints above, a new sailing/marine app would differentiate by:

- **Transparent, stable pricing with no forced re-subscription friction** — the single loudest and most consistent complaint (6 distinct mentions + 6 separate forum threads) is Navionics' large price hikes, billing errors, double charges, and a subscription-verification bug that locks out users who already paid. A flat/one-time price or a clearly-communicated, capped-increase subscription would directly counter this.
- **Reliable, offline-first GPS tracking that doesn't freeze or drop position** — GPS drift, "danger to safe navigation" freeze reports, and total GPS failures (up to a dedicated Apple Support thread) recur across both incumbents. A new app should invest disproportionately in position-tracking robustness and make offline behavior a headline feature, not an afterthought.
- **A working free/trial tier that actually lets users evaluate the product** — Marine Navigation's Lite version reportedly has broken functions, undermining trust before purchase; the eventual full-version "scam" complaints likely trace back to this. A trustworthy free tier with genuinely functional (if limited) features would reduce refund-driven anger.
- **Honest, tested route-planning limits** — Navionics' reported inability to follow routes over ~20 miles or to reliably follow created routes at all is a core-workflow failure for cruisers doing multi-day passages; a new app should not silently degrade on long routes.
- **A dedicated, well-executed digital logbook** — independent of the incumbent complaint mining, the Cruisers Forum thread signal is the strongest organic demand evidence found this session: at least 8 separate threads across years where users ask for (or, in one case, build their own) a logbook app, suggesting the logbook sub-niche flagged as "thinner" in Phase 2 has real, repeated, unmet demand rather than just low competition.
- **Responsive customer support with real refund handling** — both incumbents draw specific complaints about unanswered support emails and denied refunds; even a small, well-staffed support process would be a differentiator against two apps whose users describe support as unresponsive.

---

## Phase 4 — Distribution Channel Check

**Research date:** 2026-08-10
**Method note:** `apple.com` domains remain blocked. `reddit.com` (and privacy-frontend/mirror attempts) were not directly fetchable this session either — no `WebFetch` call was even attempted against reddit.com per task instructions, since prior phases already confirmed it fails. Subscriber/member figures below come from `WebSearch` result summaries of third-party aggregator sites (gummysearch.com, subbed.org, etc.); several of those aggregator sites (subredditstats.com, gummysearch.com) also returned `EGRESS_BLOCKED` when `WebFetch` was tried directly, so even the numbers reported here are WebSearch's paraphrase of a snippet, not a page Claude opened and read itself — same evidentiary caveat as Phase 3. Where no source gave a hard number, the row says "size unverified" rather than guessing.

A critical, load-bearing gap: **no subreddit's actual self-promotion rule text could be retrieved this session.** Every attempt to find r/sailing's, r/boating's, or r/liveaboard's specific rule wording (via WebSearch, via third-party "Reddit self-promo rules" databases, via `site:reddit.com` search) came back empty or generic. This is a real hole in the distribution picture, not a rounding error, and is called out explicitly in the verdict below.

### Channels found

| Name | Type | Size | Source | Self-promo / app-announcement policy |
|---|---|---|---|---|
| r/sailing | Subreddit | 826K members | [gummysearch.com/r/sailing](https://gummysearch.com/r/sailing/) (via WebSearch summary; not independently opened — WebFetch to gummysearch.com returned EGRESS_BLOCKED) | **Unverified.** Could not retrieve r/sailing's specific rule text — reddit.com unreachable, and no third-party "subreddit self-promo rules" database (oneup.today, redship.io) covers this subreddit. General Reddit-wide norm applies by default: most hobby subs restrict or ban outright product-announcement posts (≥61% of a 49-subreddit sample banned self-promo per [oneup.today's study](https://oneup.today/blogs/reddit-selfpromo-rules-study-2026)), so treat as **likely restricted until confirmed**, not open. |
| r/boating | Subreddit | 79K members | [gummysearch.com/r/boating](https://gummysearch.com/r/boating/) (via WebSearch summary) | **Unverified**, same caveat as above. |
| r/liveaboard | Subreddit | 10,546 members | [subbed.org/r/liveaboard](https://subbed.org/r/liveaboard) (via WebSearch summary) | **Unverified**, same caveat as above. Smallest of the three but most directly on-target for a cruising/liveaboard logbook app. |
| Cruisers Forum (cruisersforum.com) | Forum (vBulletin) | Size unverified as registered-member count. Traffic estimate only: ~185K–295K monthly visits per third-party traffic-estimation tools ([statshow.com](https://www.statshow.com/www/cruisersforum.com), similarweb data cited in search) — **this is site traffic, not a member/community-size figure, and should not be read as one.** | [statshow.com](https://www.statshow.com/www/cruisersforum.com), [similarweb.com](https://www.similarweb.com/website/cruisersforum.com/) | **Partially verified, ambiguous.** The forum has dedicated **"Commercial Posts"** and **"Vendor Spotlight"** sections in its structure (confirmed present via WebSearch of the live site's forum index), implying an official, sanctioned path exists for a company/app to post — but the specific entry rules (minimum post count, mod approval, fee) could not be retrieved. This is also the forum with the strongest organic demand signal from Phase 3 (8+ threads asking for a logbook app). |
| Sailing Anarchy Forums (forums.sailinganarchy.com) | Forum (XenForo) | ~52,278 total registered members as of June 2013 (stale — no current figure found; likely larger today but unverifiable) | [forums.sailinganarchy.com](https://forums.sailinganarchy.com/) (member count via WebSearch summary of an old figure) | **Confirmed NO.** Per the forum's own [Terms and Rules page](https://forums.sailinganarchy.com/help/terms/), "selling and self-promotion postings are verboten on the Forum" — users are explicitly redirected to the paid Classifieds section or a Google Adwords account to advertise. Two strangers posting an app announcement here would be against the forum's written rules. |
| SailNet Community (sailnet.com) | Forum | Size unverified — no subscriber/member figure found in any source; described only qualitatively ("extremely popular," "great member base") | [sailnet.com/forums](https://www.sailnet.com/forums/) | Unverified — no rules text retrieved. |
| Sailboat Owners Forums (forums.sailboatowners.com) | Forum | Size unverified | [forums.sailboatowners.com](https://forums.sailboatowners.com/) | Unverified — no rules text retrieved. Noted (per Phase 3) as an active venue for the Navionics price-hike backlash thread, so it is a real, active forum even without a hard member count. |
| Seven Seas Cruising Association (SSCA) | Trade / membership org | ~2,000 member boats | [ssca.org](https://www.ssca.org/) / [Wikipedia](https://en.wikipedia.org/wiki/Seven_Seas_Cruising_Association) (self-described as "the oldest and largest worldwide organization supporting the liveaboard cruising lifestyle," founded 1952) | N/A as a self-serve post-an-announcement channel — it's a paid membership org, not an open forum. Relevant only as a potential partnership/newsletter-sponsorship target, not a place two strangers can drop a post. |
| US Sailing | Trade org | Size unverified — no total membership count found (only fee tiers: Individual $85, Family $135, College $125, Youth $45 for 2026) | [ussailing.org/membership](https://www.ussailing.org/membership/) | N/A as a distribution channel — national governing body, not a community board. |
| American Sailing Association (ASA) | Trade / certification org | 500,000+ sailors certified — but this is a **cumulative lifetime count since 1983**, not a current active community size | [americansailing.com — "500,000+ sailors certified"](https://americansailing.com/articles/500000-certified-sailors/) | N/A as a distribution channel — a certification body, not a forum a stranger can post on. |
| Sailing La Vagabonde | YouTube channel | ~1.99M subscribers (July 2026) | [socialblade.com](https://socialblade.com/youtube/handle/sailinglavagabonde), [speakrj.com](https://www.speakrj.com/audit/report/UCZdQjaSoLjIzFnWsDQOv4ww/youtube) | N/A as a "post here" channel — it's a creator-owned channel; a stranger cannot post to it, only comment or pitch the creator for a paid/organic mention. Listed to size the audience, not as a place to self-announce. |
| Sailing SV Delos | YouTube channel | ~979K–994K subscribers (Feb 2026, sources vary slightly) | [socialblade.com](https://socialblade.com/youtube/handle/svdelos), [speakrj.com](https://www.speakrj.com/audit/report/svdelos/youtube) | Same as above — audience-sizing only, not a self-serve channel. |
| Gone with the Wynns | YouTube channel | 711K subscribers | [speakrj.com](https://www.speakrj.com/audit/report/UCBo9TLJiZ5HI5CXFsCxOhmA/youtube) | Same as above. |
| "SAILORS COMMUNITY" / "Marine Academy" Discord servers | Discord | Size unverified — surfaced by name via WebSearch but no member count or independent confirmation of authenticity/activity found | WebSearch summary only, no direct source URL resolvable | Unverified on every axis (size, activity, rules). Cannot be relied on as a distribution channel without direct verification. |
| Sailing/boating-themed gaming Discords (Black Desert Online "Sailing," OSRS "Sailing," AC Sailing Community, SAIL VR) | Discord | Real, sourced member counts (23,109 / 14,567 / 1,318 / 88,183 respectively) per [discordbotlist.com](https://discordbotlist.com/servers/bdo-sailing) / [DISBOARD](https://disboard.org/servers/tag/sailing) listings | see above | **Not relevant** — these are video-game communities (Black Desert Online, Old School RuneScape, Assassin's Creed, VR sailing sim), not real-world sailors/cruisers. Listed only to show they were checked and excluded, not as candidates. |

### Verdict

**GO, with a hard condition — do not treat this as launch-ready distribution.**

What is genuinely clear and specific:
- Two large, real, sourced Reddit communities sit directly on-topic — r/sailing (826K) and r/boating (79K) — plus a smaller, more precisely-targeted one, r/liveaboard (10.5K), which is the best-fit audience for a logbook/cruising app specifically.
- Cruisers Forum, the single richest source of organic demand signal in this whole research project (8+ Phase-3 threads explicitly asking for a logbook app), has a structurally sanctioned "Vendor Spotlight" / "Commercial Posts" section — i.e., there is a real, named door to knock on, not a guess.
- We got one unambiguous, sourced answer to the "would they ban us" question: **Sailing Anarchy Forums explicitly prohibits self-promotion in its own written Terms and Rules**, confirming that at least one high-signal community is closed to a cold app-announcement post and would require paid advertising instead.

What keeps this from being a clean GO:
- For every channel that actually matters most (r/sailing, r/boating, r/liveaboard, and Cruisers Forum's exact vendor-section entry requirements), the specific "can two strangers post an app announcement without being banned" question is **unverified**, not answered — this session's reddit.com blackout (consistent with Phases 2 and 3) means we know the audience sizes but not the gatekeeping rules for the two biggest candidate channels.
- No sailing-specific Discord community of meaningful, verified size and real (non-gaming) relevance was found — this potential channel is empty-handed.
- YouTube reach is large (Sailing La Vagabonde alone is ~2M) but is not a "post an announcement" channel for two unknown strangers — it would require a creator partnership/sponsorship, which is a different (harder, paid) distribution motion than the task is checking for.

Net call: the niche has **real, named, sized communities** (this clears the bar in the task instructions — several channels have hard, sourced numbers), so this is not a blind KILL. But distribution is not "clear and specific" enough to greenlight spending dev time on the assumption that free organic posting will work — one of the best channels (Sailing Anarchy) is confirmed closed, and the two largest (r/sailing, r/boating) have unverified gatekeeping. **Before committing build time, manually open r/sailing, r/boating, r/liveaboard, and the Cruisers Forum Vendor Spotlight rules in a browser (this session cannot) and confirm self-promotion is permitted in some form** (megathread, flaired post, vendor section, or organic 90/10-rule participation). If those come back closed too, the realistic distribution plan shifts from "post an announcement" to "build karma/reputation over months by participating genuinely, then mention the app," which is a much slower and less certain path for a small indie team with no existing audience.
