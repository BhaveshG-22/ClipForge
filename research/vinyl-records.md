# Vinyl Records — Phase 2 Demand + Competition

*Research date: 2026-08-10. Note on method: the iTunes Search API and the App Store customer-reviews RSS feed were unreachable from this environment (apple.com egress blocked, confirmed via curl/WebFetch). All data below comes from Google WebSearch snippets — search-engine caches, aggregator sites (JustUseApp, AppBrain, blog roundups), and Apple App Store page titles/snippets surfaced by the search engine, not from directly querying Apple's API or fetching apps.apple.com. Every field not directly confirmed by a source is marked "unverified."*

## Search methodology (queries run, in order)

1. `vinyl record collection app iphone app store`
2. `site:apps.apple.com vinyl records`
3. `record collection catalog app ios`
4. `vinyl collection tracker app ios`
5. `turntable app ios`
6. `"Discogs" app store iphone rating reviews price`
7. `"Vinyl Record App" app store rating reviews price subscription`
8. `"My Vinyl Record Collection" app store rating reviews price`
9. `"Music Tracker" vinyl catalog app store rating reviews price`
10. `"VinylBox" app store rating reviews price`
11. `VinylBox justuseapp rating reviews number`
12. `"Vinylo" vinyl collection app store rating price subscription`
13. `"iCollect Music" OR "iCollectEverything" app store rating price`
14. `"My Vinyl+" app store rating reviews price discogs sync`
15. `"vinylover" collection tracker app store rating reviews price`
16. `"Vinyls: Manage your collection" app store rating price reviews`
17. `"Vinyl Record App" id1114331735 last updated version date`
18. `Discogs app iphone last updated version 2026`

## Apps found

| # | App name | Developer/seller | App Store URL | Price | Rating | Rating count | Last updated / version |
|---|---|---|---|---|---|---|---|
| 1 | Discogs | Discogs / Zink Media (seller name unverified — not found in snippets) | https://apps.apple.com/us/app/discogs/id1036449551 | Free | 4.81 ★ (source: AppBrain-derived snippet) | ~67,000 ("67 thousand ratings" — source: AppBrain/search snippet, exact figure unverified) | Two conflicting figures surfaced: v3.0.10 / Feb 4, 2026 (one source) and v3.0.19 / Jul 11, 2026 (another); Google Play sibling updated Jul 7, 2026. Treat exact date as unverified but app is clearly actively maintained in 2026. |
| 2 | Vinyl Record App | Noah Tovares (indie dev, per mwm.ai snippet) | https://apps.apple.com/us/app/vinyl-record-app/id1114331735 | Free with "Vinyl Premium" subscription at $3.99/month | unverified — not found (no star figure surfaced in any query) | unverified — not found | unverified — one source references "updated for iOS 26" and version 1.9.4 (via UpdateStar mirror), no confirmed date; another source snapshot dated Apr 30, 2026 |
| 3 | My Vinyl Record Collection | unverified — not found (seller name not surfaced) | https://apps.apple.com/us/app/my-vinyl-record-collection/id1527609727 | $0.99, no ads/IAP (per snippet) | 4.2 ★ | 6 ratings | unverified — not found |
| 4 | VinylBox: Collect & Sell Vinyl | unverified — not found (seller name not surfaced; app also lists under aliases "VinylBox - Scan Vinyl" / "VinylBox - Vinyl Collector", same id 1212071750) | https://apps.apple.com/us/app/vinylbox-collect-sell-vinyl/id1212071750 | Subscription $1.99/mo, plus a $3 "Pro" IAP for bulk-adding albums | unverified — not found (a JustUseApp mirror mentions "2,534 reviews" but does not state a star rating; described qualitatively as "mixed reviews") | ~2,534 (JustUseApp aggregate, not confirmed as the actual App Store count) | unverified — not found |
| 5 | Vinylo: Vinyl Collection | unverified — not found | https://apps.apple.com/us/app/vinylo-vinyl-collection/id6768346985 | Freemium (10 records/30 journal entries free) + Premium lifetime one-time purchase (price unverified) | unverified — App Store snippet explicitly states "hasn't received enough ratings or reviews to display an overview" | 0 / below Apple's reporting threshold | unverified — not found (new-looking app, high numeric App ID suggests a recent 2025/2026 listing) |
| 6 | Music Tracker: Vinyl Catalog | Simone Montalto (indie dev, per snippet) | https://apps.apple.com/us/app/music-tracker-vinyl-catalog/id6450698274 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |
| 7 | vinylover: collection tracker | Kirill Konovalov | https://apps.apple.com/us/app/vinylover-collection-tracker/id6477580879 | Free with in-app purchases / subscription (exact tiers unverified) | Conflicting: most App Store mirrors say "not enough ratings to display an overview"; one unnamed source claims "3 out of 5 stars" — treat as unverified | unverified — not found | unverified — not found |
| 8 | My Vinyl+ (Scanner for Discogs) | unverified — not found | https://apps.apple.com/app/apple-store/id1547173908 | Free with IAP: $0.99/mo, $12.99/yr, or $39.99 lifetime ("Platinum") | 4.6 ★ | 100 ratings | unverified — not found |
| 9 | iCollect Music: Vinyl Discogs | iCollect Everything, LLC | https://apps.apple.com/nz/app/icollect-music-vinyl-discogs/id476622260 | Free with IAP (unlocks unspecified in snippet) | 3.9 ★ — NOTE: this figure is confirmed only for the Google Play listing, not the iOS App Store; iOS rating is unverified — not found | unverified — not found for iOS specifically | unverified — not found |
| 10 | Vinyls: Manage your collection | Frazao Costa | https://apps.apple.com/us/app/vinyls-manage-your-collection/id1589128395 | unverified — not found (reviewer note: "wished there was a one-time payment option," implying it may currently be subscription-based, but not confirmed) | unverified — not found | unverified — not found | unverified — not found |

Other real, distinct apps that surfaced in search but were not profiled in depth (confirming the niche is not thin): Vinyls - Record Player (id1556054655, playback/visual app rather than cataloging), Vinyl Record (id6448477385, playback emulator), Vinyl Widget (id1624683273), CLZ Music (clz.com, cross-platform catalog app with iOS client), CatalogIt (id1332161425, general collectibles catalog, not vinyl-specific), several single-purpose turntable-speed/calibration utilities (Turntable Speed id1604670976, Turntable RPM & W/F Tools, Grooved: Turntable Calibration id6479003866), and several very recent (2025/2026-vintage App IDs) record-value-scanning apps (Vinyl Record Value Scanner: IQ id6760042848, Vinyl Scanner - Record Prices id6759502933, VinylSnap id6748595105, Vinyl Catalog id6759412038, Vinyl & CD Collection Manager id6474089598) — the volume of these newer entrants suggests active, ongoing developer interest in the niche as of 2026.

## Opportunity flags

- **Top apps average <4.0 stars with >200 ratings:** **False / not supported by data found.** The only app with both a confirmed star rating and a confirmed rating count over 200 is Discogs, at 4.81★ / ~67,000 ratings — well above the 4.0 threshold. No app in the list has a confirmed rating count above 200 that is also below 4.0★. Most of the smaller, more directly comparable "vinyl collection tracker" apps (My Vinyl Record Collection, My Vinyl+, Vinylo, vinylover) have ratings either above 4.0★ or too few ratings to register at all, so this flag does not indicate an opening for a better-reviewed competitor.

- **Top apps not updated in >18 months:** **False, with caveats.** Discogs (the dominant, highest-volume app) shows credible evidence of being updated within the last month (July 2026) relative to the research date (Aug 2026). Several niche competitors (Vinylo, the value-scanner apps, Vinyl Catalog) have very recently issued App IDs, implying 2025–2026 launches. However, exact "last updated" dates for most of the smaller apps (Vinyl Record App, My Vinyl Record Collection, Music Tracker, VinylBox, Vinyls: Manage your collection, My Vinyl+, iCollect Music) are unverified — not found, so staleness cannot be ruled out app-by-app. Overall the category shows visible signs of active development (new entrants appearing throughout 2025–2026), so this flag reads as false rather than unclear.

- **Top 3 results are all free/ad-supported with no paid alternative:** **False.** Discogs is free (no ads mentioned, ad-supported status unverified but described as free-with-marketplace-model), but Vinyl Record App charges a $3.99/mo subscription, My Vinyl Record Collection is a $0.99 flat paid app with no ads/IAP, VinylBox charges $1.99/mo + $3 IAP, and My Vinyl+ has paid tiers up to $39.99 lifetime. Paid and freemium alternatives clearly coexist alongside the free Discogs app, so there is no absence of monetized options — if anything the space already has multiple competing pricing models (flat-fee, subscription, freemium-with-lifetime-unlock).

- **Fewer than 5 results that genuinely match the keyword (i.e., the niche is underserved):** **False — the niche is well-served, not underserved.** Search turned up well over 10 distinct, real, on-topic apps across cataloging (Discogs, Vinyl Record App, My Vinyl Record Collection, VinylBox, Vinylo, Music Tracker, vinylover, My Vinyl+, iCollect Music, Vinyls: Manage your collection, CLZ Music, CatalogIt), playback/aesthetic apps (Vinyls - Record Player, Vinyl Record, Vinyl Widget), and hardware-diagnostic tools (Turntable Speed, Turntable RPM & W/F Tools, Grooved: Turntable Calibration), plus a fresh wave of 2025/2026-launched record-value-scanner apps. This is a saturated, actively contested niche by app-count, not a gap.

## Overall assessment

Based on what search could surface, "vinyl record collecting" looks like a **crowded, actively competed niche dominated by one very strong incumbent (Discogs, free, ~4.8★, ~67k ratings, updated within the last month)**, surrounded by a long tail of small indie cataloging apps (mostly under a few hundred ratings, several with no visible rating yet) using varied monetization (flat fee, subscription, freemium) and a steady stream of new 2025–2026 entrants — none of which found a discoverable data gap (low ratings + high volume + staleness) to exploit. Confidence in this assessment is **low-to-moderate**: most granular fields (exact rating counts, last-update dates, and iOS-specific ratings for several apps) could not be directly confirmed because the App Store API and reviews RSS were unreachable, so this reflects search-engine-surfaced snippets and aggregator mirrors rather than verified Apple data — a direct API check (from an unblocked environment) would be needed before treating any single number here as authoritative.
