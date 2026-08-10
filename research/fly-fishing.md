# Fly Fishing — Phase 2 Demand + Competition

**Research date:** 2026-08-10
**Method note:** The iTunes Search API (`itunes.apple.com/search`) and the App Store customer-reviews RSS feed were unreachable this session (apple.com egress blocked — confirmed via curl/WebFetch, both returned EGRESS_BLOCKED). All findings below come from the `WebSearch` tool only — i.e., third-party blog posts, aggregator sites (justuseapp.com, marlvel.ai, appgrooves.com, appbrain.com), developer marketing pages, and the text snippets Google/Bing surface for `apps.apple.com` result pages themselves. **No number in this document was read directly off an Apple-served page.** Every rating, rating count, price, and update date is either sourced to a specific secondary URL or marked "unverified."

## Search methodology (WebSearch queries run)

1. `fly fishing app iphone app store`
2. `site:apps.apple.com fly fishing`
3. `best fly fishing log app ios`
4. `fly fishing knot tying app ios`
5. `fly identification app ios`
6. `FlyFishFinder app store rating reviews price developer`
7. `TroutRoutes app store rating reviews price onX`
8. `Orvis Fly Fishing app store rating reviews`
9. `FishAngler app store rating reviews price`
10. `IdentaFly app store rating reviews price subscription`
11. `SnapHatch fly fishing app rating reviews`
12. `"The Catch and The Hatch" app rating reviews price developer`
13. `"DIY Fly Fishing" app rating reviews price update`
14. `FishAngler app store iOS rating number of ratings 2026`
15. `"Fly Fishing & Fly Tying" app store magazine rating price`
16. `FlyFishFinder app update version 2026 last updated`
17. `Orvis Fly Fishing app store apps.apple.com id`
18. `TroutRoutes app store number of ratings star rating iOS`
19. `IdentaFly app store number of ratings star rating iOS reviews count`

## Apps found

| # | App | Developer / Seller | App Store URL | Price | Rating | Rating count | Last updated |
|---|-----|--------------------|----------------|-------|--------|---------------|--------------|
| 1 | FlyFishFinder: Fly Fishing App | unverified — contact email `andrew@flyfishfinder.com` surfaced on flyfishfinder.com, not confirmed as the App Store seller name | https://apps.apple.com/us/app/flyfishfinder-fly-fishing-app/id6446231902 | Freemium — free download, premium "Live Gages" / catch-logging tier mentioned; exact price unverified — not found | unverified — not found (no numeric rating surfaced in any snippet) | unverified — not found | unverified — flyfishfinder.com blog claims a "Prime Waters" feature shipped "in 2026" and mentions recent payment/UI updates, but no exact date (query 16) |
| 2 | IdentaFly: Fly Fishing Smarts | unverified — not found | https://apps.apple.com/us/app/identafly-fly-fishing-smarts/id6470413594 | Free with IAP — $5.99/mo or $29.99/yr subscription (sourced: query 10 snippet) | unverified — not found | unverified — not found (query 19 returned no numeric data) | unverified — not found |
| 3 | SnapHatch – Fly Fishing Guide | unverified — not found | https://apps.apple.com/us/app/snaphatch-fly-fishing-guide/id6504807770 | Free with in-app purchases (query 11) | 4.9/5 claimed in one snippet, but the same search also surfaced an unrelated Shopify-app reviews page ("Reviews 1,757", apps.shopify.com/reviews/1513070) for a different SnapHatch product — **rating likely conflated/misattributed, treat as unverified** | unverified — not found | unverified — not found |
| 4 | TroutRoutes: Fly Fishing App (by onX) | onX (per query 7 snippet "TroutRoutes by onX") | https://apps.apple.com/us/app/troutroutes-fly-fishing-app/id1423989574 | Tiered — Basic free / Single-State $19.99/yr / PRO $39.99/yr or $9.99/mo, 7-day free trial (query 7) | 4.5/5 (query 18, sourced to justuseapp.com aggregator, not Apple directly) | 3,774 ratings (query 18, same aggregator source) | unverified — not found |
| 5 | DIY Fly Fishing V3 | unverified — likely "DIY Fly Fishing" company, name not confirmed on App Store listing itself | https://apps.apple.com/us/app/diy-fly-fishing-v3/id1556251731 | Conflicting signals — one snippet says $2.99, another compares it to apps costing "twice as much" implying ~$29.99 elsewhere; **price unverified due to conflict** (query 13) | 4.5/5 (75% five-star per breakdown) — source ambiguous, likely diyflyfishing.com's own marketing page rather than raw Apple data (query 13) | unverified — not found | unverified — snippet mentions "recent updates" (new graphics, sign-out bug fix) but no date |
| 6 | The Catch and The Hatch | Lucas Gardner (query 12 snippet) | https://apps.apple.com/us/app/the-catch-and-the-hatch/id1487346869 | Free with IAP — $200 "Entomology Course" IAP, seen discounted to $50 (query 12) | ~4/5 stars per snippet — source ambiguous (appgrooves.com aggregator, not confirmed as live Apple rating) | unverified — not found | unverified — not found |
| 7 | FishAngler: Fishing App | FishAngler, LLC (confirmed via `apps.apple.com/us/developer/fishangler-llc/id1073941117` result title in query 14) | https://apps.apple.com/us/app/fishangler-fishing-app/id1073941118 | Free with VIP subscription; exact price unverified — not found | 4.6/5 (query 14, sourced to marlvel.ai third-party "intel report," not Apple directly) | 28.4K reviews (query 14, same third-party source, "as of April 2026") | unverified — not found. **Note:** general fishing app (species/spots agnostic), not fly-fishing-specific, though it has fish-ID and fly-relevant social features |
| 8 | Fly Fishing & Fly Tying (magazine) | unverified — not found; magazine described as established in 1990, publisher not confirmed in snippets | https://apps.apple.com/us/app/fly-fishing-fly-tying/id531347592 | unverified — not found (a comparable title, Fly Tyer Magazine, was found at $2.99/issue or $19.99/yr, but that is a different app) | unverified — not found | unverified — not found | unverified — not found. Numeric App Store ID (531347592) is old relative to the other apps in this list, consistent with an older/legacy listing, but no update date confirmed |
| 9 | Orvis Fly Fishing – The Ultimate Fly-Fishing Guide | Orvis | App Store URL unverified — not found in any search result; only third-party mirror/download pages (appstor.io, apps112.com) surfaced (query 17) | Reported free (query 17 snippet), not directly confirmed | 3.58/5 based on 390 ratings — **this figure is explicitly for the Android/Google Play listing (via AppBrain), not iOS** (query 8); iOS rating unverified | unverified for iOS — not found | **Significant finding:** query 17 snippet states Orvis "decided to focus resources on their mobile website rather than the app version and no longer maintains and supports the app" — i.e., likely abandoned/discontinued. Exact last-update date not found |
| 10 | i Fishing Fly Fishing Edition | unverified — not found (fishing-game series, publisher not confirmed) | https://apps.apple.com/us/app/i-fishing-fly-fishing-edition/id389027275 | unverified — not found | unverified — not found | unverified — not found | unverified — not found. **Note:** this is a fishing simulation/game, not a utility/log/ID tool — different category from the rest of this list |

Additional apps that surfaced but were not carried into the table above (lower confidence they're distinct/current, or off-niche): **Fishing Knots & Rigs** (id1548905260) and **Fishing Knots FishPlanet** (id681286803) — general fishing-knot references that claim fly-fishing coverage but are not fly-fishing-specific; **Fly Tyer Magazine** (id448326791) and **Fly Fisherman Magazine** (id582712299) — sibling magazine apps to #8; **Fly Fishing Simulator HD** (id1187773953) and **i Fishing Fly Fishing Lite** (id438036256) — additional game variants.

## Opportunity flags

**1. Top apps average <4.0 stars with >200 ratings — FALSE**
Where a rating *and* a count were both found (TroutRoutes: 4.5/5 at 3,774 ratings; FishAngler: 4.6/5 at 28.4K ratings — though FishAngler is general-fishing, not fly-specific), both are comfortably above 4.0. DIY Fly Fishing's self-reported breakdown also implies ~4.5/5. The one sub-4.0 figure found (Orvis, 3.58/5) is explicitly an Android number for an app that appears discontinued, so it doesn't represent current top competition. Confidence is low-moderate since none of these numbers came from Apple directly — they're aggregator/marketing-site citations.

**2. Top apps not updated in >18 months — FALSE, with one notable exception**
FlyFishFinder and DIY Fly Fishing both show snippet evidence of 2026 feature work (a "Prime Waters" feature and UI/sign-out-bug updates respectively), suggesting active maintenance among the newer, geo/mapping-focused leaders. However, **Orvis Fly Fishing — a legacy, brand-name incumbent — appears to be abandoned** per an explicit statement that Orvis "no longer maintains and supports the app." So the flag is false for the current top apps overall, but there is a real precedent of an established competitor going stale, which a new entrant could exploit. No exact update timestamps were obtainable (Apple blocked), so this is directional, not precise.

**3. Top 3 results are all free/ad-supported with no paid alternative — FALSE**
Clear paid/subscription tiers exist among the leaders: TroutRoutes ($19.99–$39.99/yr or $9.99/mo), IdentaFly ($5.99/mo or $29.99/yr), and DIY Fly Fishing (reported one-time price, ~$2.99 though conflicting). All of the top apps found use a freemium model with a real paid tier rather than pure ad-support — paid willingness-to-pay is already demonstrated in this niche.

**4. Fewer than 5 results that genuinely match the keyword (niche underserved) — FALSE**
At least 9 distinct, genuinely fly-fishing-focused apps were found with real App Store URLs (FlyFishFinder, IdentaFly, SnapHatch, TroutRoutes, DIY Fly Fishing V3, The Catch and The Hatch, Fly Fishing & Fly Tying magazine, Orvis Fly Fishing, i Fishing Fly Fishing Edition), plus several more adjacent/sibling titles (Fly Tyer Magazine, Fly Fisherman Magazine, fishing-knot apps, additional fishing-game variants) and a strong general-fishing app (FishAngler) with fly-relevant features. This is well above the 5-result underserved threshold — the niche has multiple specialized incumbents across mapping/log, insect-ID, and instructional sub-niches.

## Overall assessment

This niche looks **moderately-to-well served rather than a clear open opportunity**: there are at least three actively-maintained, subscription-monetized incumbents (TroutRoutes/onX, IdentaFly, FlyFishFinder) plus several more specialized or legacy players, and the ones with confirmed rating data score well above 4.0 stars — so a new entrant would need real differentiation (not just "a fly fishing app") to break in, though the apparent abandonment of the once-dominant Orvis app hints at an underserved sub-slot for a polished instructional/guide product. **Confidence in this read is low-to-moderate**: because Apple's iTunes Search API and reviews RSS were unreachable this session, every rating, rating count, and update date above is a third-party citation (aggregator sites, developer blogs, or search-snippet paraphrases) rather than data confirmed directly against apps.apple.com, and several figures (SnapHatch's 4.9/5, DIY Fly Fishing's price) carry explicit source-conflict caveats above.
