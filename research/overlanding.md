# Overlanding — Phase 2 Demand + Competition

> Note on method: this session's network egress blocks all apple.com domains, so the iTunes Search API and the App Store customer-reviews RSS feed could not be queried directly (confirmed EGRESS_BLOCKED via curl and WebFetch). All data below was gathered via the WebSearch tool only, relying on Google-indexed snippets of App Store listing pages plus third-party aggregators (AppBrain, SensorTower, grand-screen.com, justuseapp, appviewable) that mirror App Store metadata. Where a number could not be directly confirmed from a source snippet, it is marked "unverified" with the closest source noted. Star ratings and rating counts sourced from third-party aggregators may lag the live App Store value and should be treated as directional, not exact.

## Search methodology (WebSearch queries run)

1. `overlanding app iphone app store`
2. `site:apps.apple.com overlanding`
3. `off-road trail app ios app store`
4. `4x4 trip planner app ios app store`
5. `overland trip planning app offline maps ios`
6. `"Overland Map" app store rating reviews price id6741202903`
7. `"Overland Bound One" app store rating reviews price`
8. `"onX Offroad" app store rating reviews subscription price`
9. `"Trails Offroad" app store rating reviews subscription price`
10. `"Gaia GPS" app store rating reviews subscription price`
11. `"onX Offroad" app store "ratings" number of ratings star rating iphone`
12. `"iOverlander" app store rating reviews price free`
13. `"FunTreks" app store rating reviews price`
14. `"Offroadin" app store rating reviews price subscription`
15. `"Scout Overland" app store rating reviews price`

## Apps found

| App | Developer / Seller | App Store URL | Price | Avg. Rating | Rating Count | Last Updated |
|---|---|---|---|---|---|---|
| onX Offroad: Trail Maps & GPS | onX (Onx Maps, Inc.) | https://apps.apple.com/us/app/onx-offroad-trail-maps-gps/id1475112177 | Free w/ subscription — Premium $34.99/yr, Elite $99.99/yr (7-day free trial), per onXmaps pricing page | 4.39★ | ~8.6K | unverified — not found (no source gave a specific date; product appears actively marketed/updated per onxmaps.com/offroad/app/pricing and 2026-dated third-party reviews) |
| Gaia GPS: Mobile Trail Maps | Gaia GPS / Trailbehind, Inc. | https://apps.apple.com/us/app/gaia-gps-mobile-trail-maps/id1201979492 | Free w/ subscription — Membership ~$17/yr, Premium ~$36/yr (per help.gaiagps.com / pilotplans.com) | unverified — not found (search only surfaced "mixed reviews", no numeric star value) | unverified — not found | unverified — not found |
| iOverlander | community-run (listed as "iOverlander"; app formerly community non-profit project) | https://apps.apple.com/us/app/ioverlander/id1486556203 | Free w/ optional subscription — "Pro"/"Unlimited" tiers, one review-cited price of $129/yr (unverified — sourced from a review snippet on appviewable.com, not the official listing) | 4.2★ | ~6.4K | unverified — not found |
| Overland Bound One: Maps & GPS | Overland Bound | https://apps.apple.com/us/app/overland-bound-one-maps-gps/id1184607277 | Free app; Overland Bound annual membership $39.99/yr unlocks route planning, offline maps, full map layers (per store.overlandbound.com) | Conflicting sources: one WebSearch summary stated "4.7★" on iOS; a third-party aggregator (grand-screen.com) lists "★4.2". Treat as unverified/uncertain — the two sources disagree and neither is the primary App Store page itself. | unverified — not found | unverified — not found |
| Trails Offroad: Offline Maps | Trails Offroad, LLC | https://apps.apple.com/us/app/trails-offroad-offline-maps/id1545278645 | Freemium — Free plan (200 trail guides); All-Access Membership $39.99/yr (per trailsoffroad.com / app description) | unverified — not found (justuseapp.com references "26 reviews" for a review-aggregator page, not an official App Store star rating/count) | unverified — not found (see above; "26" is from justuseapp, not confirmed as the live App Store count) | unverified — not found |
| FunTreks 4x4 Offroad Trails | FunTreks (small Colorado guidebook publisher) | https://apps.apple.com/us/app/funtreks-4x4-offroad-trails/id1051880942 | $59.99 one-time purchase (per AppBrain snippet) | 3.38★ | 29 | unverified — not found |
| Overland Map | unverified developer name — Google Play package `ch.overlandmap.map` suggests a Swiss/CH-based developer, not confirmed | https://apps.apple.com/us/app/overland-map/id6741202903 | Described in search snippet as "free without ads"; not independently confirmed on a pricing page | "hasn't received enough ratings or reviews to display an overview" per WebSearch summary of the App Store page — i.e. confirmed as too-new-to-rate, not a numeric score | unverified — not found (implied very low/near-zero given no rating overview) | unverified — not found |
| Scout Overland | unverified developer name — not found in snippets | https://apps.apple.com/us/app/scout-overland/id6756683492 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |
| Offroadin': Trail Maps & GPS | unverified developer name — not found in snippets | https://apps.apple.com/us/app/offroadin-trail-maps-gps/id1637982270 | Free to download per search snippet; in-app purchase/subscription structure not detailed in any snippet found | unverified — not found | unverified — not found | unverified — not found |
| Overland Navigator | unverified developer name — appears to be a New Zealand-focused niche product | https://apps.apple.com/us/app/overland-navigator/id1451030537 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |

Apps considered but excluded from the table as poor keyword matches or too narrow/regional to represent general competition: **NXTLEVEL 4X4** (single desert-trip-club app, Mexico-region specific), **Overland GPS Tracker** (single-purpose location-logging utility, not a trip-planning/trail app), **Utah Overland Community** (single-state community app), and general road-trip planners (Roadtrippers, TripIt, Wanderlog, Roadie, Road Trip Planner) which surfaced under the "4x4 trip planner" query but are not overlanding/off-road-specific.

## Opportunity flags

- **Top apps average <4.0 stars with >200 ratings:** **FALSE.** The two apps with confirmed, sizeable rating counts — onX Offroad (4.39★, ~8.6K ratings) and iOverlander (4.2★, ~6.4K ratings) — both sit above 4.0 with well over 200 ratings. The only sub-4.0 app found (FunTreks, 3.38★) has just 29 ratings, far short of the >200 threshold, so it doesn't trigger this flag either. Reasoning: the category leaders are well-reviewed and well-established, not weak/underperforming products.

- **Top apps not updated in >18 months:** **Unclear / unverified.** No source (blocked from the live App Store listing pages) gave an explicit "last updated" date for any app. Indirect signals — onX Offroad and Gaia GPS both have active, dated 2026 marketing/pricing pages and are referenced in 2025-2026-dated third-party comparison articles — suggest the market leaders are actively maintained, but this is circumstantial, not a confirmed release-date check. Cannot confidently mark this true or false.

- **Top 3 results are all free/ad-supported with no paid alternative:** **FALSE.** Every well-documented app in the table monetizes via paid subscriptions or memberships: onX Offroad ($34.99-$99.99/yr), Trails Offroad ($39.99/yr All-Access), Overland Bound One ($39.99/yr membership), Gaia GPS ($17-$36/yr), and iOverlander (subscription tiers referenced, one review citing $129/yr). These are freemium models with a substantial paid tier, not simple free/ad-supported products. Reasoning: there is clear, established evidence that overlanders already pay annual subscriptions in this category.

- **Fewer than 5 results that genuinely match the keyword (niche underserved):** **FALSE.** At least 9-10 distinct, genuinely on-topic apps were found across five separate search queries (Overland Map, Overland Bound One, Scout Overland, Overland Navigator, iOverlander, Gaia GPS, onX Offroad, Trails Offroad, FunTreks, Offroadin'), several with meaningful traction (onX Offroad ~8.6K ratings, iOverlander ~6.4K ratings). Reasoning: this is a populated, competitive niche with at least one dominant, well-capitalized incumbent (onX), not a gap in the market.

## Overall assessment

The overlanding/off-road niche looks like an **established, moderately crowded competitive market rather than a clear whitespace opportunity** — it has a dominant, well-rated, actively monetized incumbent (onX Offroad, ~8.6K ratings at 4.39★, tiered $35-100/yr subscriptions) plus several other credible, revenue-generating competitors (Gaia GPS, Trails Offroad, Overland Bound, iOverlander), all charging $17-$130/yr, which does at least validate that users in this niche pay for premium mapping/trip-planning features. **Confidence in this read is low-to-moderate**: because the iTunes Search API and App Store pages were unreachable, nearly every rating count, exact price tier, and every single "last updated" date in this report is either sourced from third-party aggregator snippets (which can be stale or approximate) rather than the live listing, or is explicitly marked unverified — a follow-up pass with direct App Store/iTunes API access is needed before treating any of these numbers as decision-grade.
