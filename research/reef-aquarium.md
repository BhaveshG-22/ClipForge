# Reef Aquarium — Phase 2 Demand + Competition

Research date: 2026-08-10.

**Access note:** This session's egress proxy blocks all apple.com domains, so the iTunes Search API and the App Store customer-reviews RSS feed were unreachable (confirmed via curl/WebFetch — both returned EGRESS_BLOCKED). All data below was gathered exclusively via the WebSearch tool, using snippets from Google-indexed App Store pages and third-party sites that quote App Store data (AppGrooves, AppBrain, developer sites, forum threads). No App Store page was fetched directly, so every number is only as reliable as the search snippet that produced it — anything not explicitly stated in a snippet is marked "unverified."

## Search methodology (queries run, in order)

1. `reef aquarium app iphone app store`
2. `site:apps.apple.com reef tank`
3. `saltwater aquarium dosing app ios`
4. `reef tank water testing log app`
5. `aquarium livestock tracker app ios`
6. `"ReefBay" app store rating reviews price`
7. `"Reef Buddy" app store rating reviews price aquarium`
8. `"Aquarimate" app store rating reviews price`
9. `"AquaCalculator" app store rating reviews subscription price`
10. `"Reefability" app store rating reviews price`
11. `"Reef2Reef" app store app rating reviews id6745577135`
12. `"ReefDoser" app store rating reviews price`
13. `"Reef Trak" app rating price reeftrak.com`
14. `"Aquarium Keeper" app store rating reviews price livestock`
15. `"TankTracker" aquarium app rating price ios`
16. `"tanktracker.app" apps.apple.com ios app store link`
17. `"Aquarium Tracker: Tank Manager" app store rating reviews price id6755304265`
18. `"Reefi" aquarium tracker app store rating price id6756351188`

## Apps found

All 10 apps below have a real, confirmed `apps.apple.com` URL that appeared directly in search results (not invented). Fields not stated in any search snippet are marked unverified.

| # | App name | Developer / seller | App Store URL | Price | Avg. rating | Rating count | Last updated / version |
|---|---|---|---|---|---|---|---|
| 1 | Aquarimate | WiseLogic, Inc. | https://apps.apple.com/us/app/aquarimate/id587215055 | $9.99 one-time (+ optional $9.99/yr cloud storage upgrade) | **4.46–4.48 / 5** (worldwide 4.46, US 4.48 — two slightly different figures appeared across sources) | **~595–620 ratings** (worldwide 620; US 595, per AppGrooves/WorldsApps snippets) | unverified — not found in snippets |
| 2 | AquaCalculator | Alexander Karkossa | https://apps.apple.com/us/app/aquacalculator/id1449511522 | Subscription — free 2-week trial then paid annual (exact iOS price not shown; Android sibling app is $8.99 one-time) | iOS: "not enough ratings to display" per App Store snippet (i.e., very few). Android sibling: 4.60/5 | iOS: unverified — not found. Android sibling: 280 ratings (not the iOS number) | unverified — not found |
| 3 | Reefability | (Reefability, launched late 2024 per reeftrak.com blog) | https://apps.apple.com/us/app/reefability/id6636472070 | $5.99/mo or $24.99/yr (also a $25/12-mo plan mentioned) | iOS rating: unverified — not found. Android: 3.83/5 (also cited as "4.0★ on Google Play") | iOS: unverified — not found. Android: 18 ratings | unverified — not found. Forum snippet indicates it's a 2024-launch app |
| 4 | ReefBay | Toolit Media LLC | https://apps.apple.com/us/app/reefbay/id6478054386 | unverified — not found (has an in-app marketplace; likely free + IAP but not confirmed) | unverified — not found (search explicitly returned no rating number) | unverified — not found | unverified — not found |
| 5 | Reef Buddy (Reef Tank Tracker / Saltwater Tracker — listing title varies by region) | maxime marinel | https://apps.apple.com/us/app/reef-buddy-reef-tank-tracker/id1593580822 | Free base app + "Shrimpy Premium" subscription (monthly/yearly, exact price not shown) | unverified — not found | unverified — not found | unverified — not found |
| 6 | Reef2Reef (forum companion app) | Total Web Systems Limited | https://apps.apple.com/us/app/reef2reef/id6745577135 | Free (community/forum app) | **4.67 / 5** (also cited as 4.6★ on both App Store and Google Play) | **42 ratings** | **Sept 5, 2025**, version 1.2.0 (per AppBrain snippet) — this is the one app with a directly-sourced update date |
| 7 | ReefDoser | Pixelwand Ltd | https://apps.apple.com/us/app/reefdoser/id353011315 | unverified — not found | "Not enough ratings or reviews to display an overview" (i.e., very few/none) | unverified — not found | unverified — one summarized source implied it's stale/old (low numeric app ID, no fresh mentions), but no explicit date was found in any snippet, so treated as unconfirmed |
| 8 | Reef Trak – Reef Manager | (reeftrak.com; developer name not shown in snippets) | https://apps.apple.com/us/app/reef-trak-reef-manager/id6741099733 | **$9.99 one-time, no subscription** (per reeftrak.com) | unverified — Reef Trak's own blog states ratings are too new/low to be meaningful; no number found | unverified — not found | unverified — not found (app appears to be a 2025-era launch based on ID and blog content dated "2026") |
| 9 | Aquarium Tracker: Tank Manager | Szymon Niemiec | https://apps.apple.com/us/app/aquarium-tracker-tank-manager/id6755304265 | Free (app description says "free aquarium tracking app," IAP not confirmed) | unverified — not found | unverified — not found | unverified — not found |
| 10 | Reefi: Aquarium Tracker | (developer name not shown in snippets; reefi-app.com) | https://apps.apple.com/us/app/reefi-aquarium-tracker/id6756351188 | unverified — not found | "Not enough ratings or reviews to display an overview" | unverified — not found | unverified — not found |

Other genuine, real apps that surfaced repeatedly but were not put in the top-10 table (to avoid padding with near-duplicates/general fishkeeping apps): AI Reef Cam (id1599324535), Smart Reef (id1480355166), MyReef 3D Aquarium 2 HD (id496555672), Reef Aquarium 2D/3D (id740403013 — a screensaver-style video app, not a tank-management tool), Aquarium Keeper (id1548192731, price/rating unverified — one snippet mentioned "someone would rate it 3.5 stars" but this reads like a review quote, not a confirmed aggregate score, so not used as a data point), ReefDeck (reefdecks.com — no confirmed apps.apple.com URL found in snippets), ReefToolkit (id6753037682), Aquarium Log – Tank Manager (id1621042664), Reef Book (id6740756140), Reef Tracker (id1639391565), AquaTrack (two different IDs appeared across searches — id6743827936 and id6757683461 — which could not be reconciled from snippets, so this app was excluded from the scored table rather than risk misattributing data). TankTracker (tanktracker.app) could not be matched to a confirmed apps.apple.com URL despite a dedicated search, so it was excluded per the "real App Store URL required" rule.

## Opportunity flags

**1. Top apps average <4.0 stars with >200 ratings — FALSE**
The only app in this research with a confirmed rating count above 200 is Aquarimate (595–620 ratings), and its rating is 4.46–4.48/5, well above 4.0. Reef2Reef and AquaCalculator's Android sibling also score above 4.0 but with far fewer than 200 ratings. No app was found with both a sub-4.0 average AND >200 ratings. Data is thin (most apps have unverified or near-zero rating counts), but on the one data point solid enough to judge, the flag is false.

**2. Top apps not updated in >18 months — UNCLEAR**
Only one app (Reef2Reef, updated Sept 5, 2025 — well under 18 months old as of Aug 2026) had a directly-sourced last-update date. Most other apps in the table carry high/recent-looking App Store numeric IDs (e.g., Reef Trak, Reefi, ReefBay, Reefability were all referenced in "2026" blog content or described as 2024/2025 launches), suggesting the visible competitive set skews toward apps launched or actively promoted within the last 1–2 years — which argues against widespread staleness. ReefDoser is the one app that reads as older/dormant, but no explicit update date could be confirmed for it. Given only one hard data point and everything else inferential, this flag cannot be confidently called true or false.

**3. Top 3 results are all free/ad-supported with no paid alternative — FALSE**
The apps with the clearest pricing data are paid or subscription-based: Aquarimate ($9.99 one-time), AquaCalculator (paid annual subscription), Reefability ($5.99/mo or $24.99/yr), Reef Trak ($9.99 one-time), and Reef Buddy (free base app + "Shrimpy Premium" subscription). Reef2Reef is the clearest free app (it's a community/forum companion, not a tank-management tool). This shows the niche already has multiple validated paid products, not just free/ad-supported ones — flag is false.

**4. Fewer than 5 results that genuinely match the keyword (niche underserved) — FALSE**
Search turned up well over 10 distinct, real, currently-listed apps that genuinely match "reef/saltwater tank management" (water-parameter logging, dosing calculators, livestock tracking): ReefBay, Reef Buddy, Reefability, AquaCalculator, Aquarimate, ReefDoser, Reef Trak, Reef2Reef, Aquarium Tracker: Tank Manager, Reefi, plus ReefToolkit, ReefDeck, Aquarium Log – Tank Manager, Reef Book, Reef Tracker, and Aquarium Keeper as further candidates. The niche is not thin by count — if anything, several of these (Reef Trak, Reefi, ReefBay, Reefability) look like recent (2024–2025) entrants, suggesting other builders currently see the same opportunity.

## Overall assessment

This niche shows real, pre-existing demand — a many-way field of at least 10 real, currently-listed apps, several charging real money ($9.99 one-time up to $24.99/yr subscriptions) with at least one (Aquarimate) showing strong satisfaction signals (4.46+/5 across ~600 ratings) — but it is a moderately crowded, actively-contested space rather than an underserved blue ocean, with multiple close competitors (Reef Trak, Reefi, ReefBay, Reefability) appearing to have launched within the last one to two years. Confidence in this read is low-to-moderate: only two apps (Aquarimate, Reef2Reef) had rating/count/date figures directly confirmed in search snippets, and the great majority of price, rating, and update-recency fields for the other eight apps are marked unverified — a follow-up pass with direct App Store access (once the egress block is lifted) is needed before sizing this opportunity with confidence.
