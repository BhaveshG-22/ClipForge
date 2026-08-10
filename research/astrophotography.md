# Astrophotography — Phase 2 Demand + Competition

**Research date:** 2026-08-10
**Method note:** The iTunes Search API and App Store customer-reviews RSS feed were unreachable from this environment (network egress to all apple.com domains is blocked and confirmed via curl/WebFetch as EGRESS_BLOCKED). All data below comes from the WebSearch tool only — search-result snippets, third-party App Store tracker sites (AppBrain, Appshunter, JustUseApp, Apptail), and app review blogs. No data was pulled directly from apps.apple.com pages themselves; App Store URLs are reported because they appeared as literal links in search results, not because the pages were fetched. Anything not explicitly stated in a search snippet is marked "unverified."

## Search methodology (WebSearch queries run)

1. `astrophotography app iphone app store`
2. `site:apps.apple.com astrophotography`
3. `telescope planning app ios app store`
4. `night sky imaging planner app ios app store`
5. `astrophotography exposure calculator app ios app store`
6. `PhotoPills app store price rating reviews iOS`
7. `Telescopius app store rating reviews price`
8. `NightCap Camera app store rating reviews price`
9. `Stardust Astrophotography app store rating reviews price`
10. `"Astrophotography Planner" app store rating reviews developer`
11. `AstroEdit app store rating reviews price developer`
12. `"Dark Skies" astrophotography app store rating reviews price`
13. `Nightlog Milky Way Planner app store rating price`
14. `AstroShader app store rating reviews price update`

## Apps found

All 10 are real apps with App Store URLs that appeared directly in WebSearch results (link title + URL pairs, not fabricated). Ratings/prices are as reported in search snippets or from third-party tracker sites cited inline; every unconfirmed cell is marked "unverified."

| # | App name | Developer | App Store URL | Price | Rating | Rating count | Last updated |
|---|----------|-----------|----------------|-------|--------|---------------|--------------|
| 1 | PhotoPills | PhotoPills SL (unverified — not directly confirmed, only inferred from listing) | https://apps.apple.com/us/app/photopills/id596026805 | $10.99 (search snippet; another blog cites $9.99, so treat exact figure as approximate) | 4.70 / 5 | ~1,500 ("1.5 thousand ratings" per search snippet — approximate, not exact) | unverified — not found |
| 2 | NightCap Camera | RTD (per search snippet) | https://apps.apple.com/us/app/nightcap-camera/id754105884 | $2.99 (one source says $1.99, likely an older price) | 4.41 / 5 (one source says 4.38 / 5) | ~2.6K (one source says 2.9K — sources disagree, so treat as approximate) | unverified — not found |
| 3 | Telescopius | unverified — not found | https://apps.apple.com/us/app/telescopius/id6479415751 | Free | 3.6 / 5 (iOS, per search snippet) | unverified — not found (only Android count found: 72 ratings on Google Play, not iOS) | unverified — not found |
| 4 | Stardust: Astrophotography | Steve Urrego (per search snippet) | https://apps.apple.com/us/app/stardust-astrophotography/id1540350025 | Free | unverified — not found (search snippet notes rating "not enough ratings to display" in some regions; a case-study title mentions "2.8 to 4 stars" but that referenced a different Stardust app — period tracker — and should not be attributed here) | unverified — not found | unverified — not found |
| 5 | Astrophotography Planner | Ryan Sponzilli (per search snippet) | https://apps.apple.com/us/app/astrophotography-planner/id1661476234 | unverified — not found | unverified — not found | unverified — not found | unverified — not found (requires iOS 17.0+, so built/updated relatively recently, but no explicit update date found) |
| 6 | AstroEdit - Simple and Quick | yong chong loh (per search snippet) | https://apps.apple.com/us/app/astroedit-simple-and-quick/id6478158736 | $1.99 one-time (one source says $2.99); optional monthly subscription also mentioned | 4.14 / 5 | 7 ratings (explicitly low — per search snippet) | Last update July 31, 2025 (available since Feb 2024) |
| 7 | AstroShader | unverified — not found | https://apps.apple.com/us/app/astroshader/id6444631986 | Free | 4.20 / 5 per one source; 4.5 / 5 per another (sources disagree) | 80 ratings per one source; "over 64" per another (sources disagree, treat as approximate low count) | Last update January 11, 2026 |
| 8 | Dark Skies: Astrophotography | Nathan Stryker (per search snippet) | https://apps.apple.com/gb/app/dark-skies-astrophotography/id843351673 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |
| 9 | Nightlog: Milky Way Planner | Groth Galleries, LLC (per search snippet) | https://apps.apple.com/us/app/nightlog-milky-way-planner/id6780690283 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |
| 10 | Astro Stacker: Star Images | unverified — not found | https://apps.apple.com/us/app/astro-stacker-star-images/id6753679598 | Free / no subscription per search snippet ("no subscription required, unlimited stacking") | unverified — not found | unverified — not found | unverified — not found |

Other apps that surfaced in search but were not included in the table above (either lower relevance to core astrophotography imaging, or duplicates/near-duplicates of the above): AstroGuide - Astrophotography, Astro Planner: Night Sky Photo, SkyPlanner, Telescope Assist, Star Exposure Calculator, Astro Max Calculator, Exposure Pro Calc, Halide (general manual-camera app, not astro-specific), Stellarium Mobile, Star Walk 2, Sky Guide, SkySafari Pro, Scope Nights (these last several are general astronomy/planetarium apps rather than astrophotography-specific, so were deliberately excluded from the primary 10 to keep the niche focused).

## Opportunity flags

**1. Top apps average <4.0 stars with >200 ratings — FALSE / unclear (leaning false)**
Reasoning: Of the apps where a rating AND a rating count above ~200 were both found, PhotoPills (4.70/5, ~1,500 ratings) and NightCap Camera (4.41/5, ~2.6K ratings) are the only two that clear the >200-rating bar, and both are well above 4.0 stars. Telescopius has a rating below 4.0 (3.6/5) but no rating count was found, so it cannot be confirmed to have >200 ratings. Verdict: false for the apps we could verify, but overall confidence is low since most apps in the table have no confirmed rating count at all.

**2. Top apps not updated in >18 months — FALSE / unclear (leaning false)**
Reasoning: The two apps with confirmed recent update dates (AstroEdit: July 31, 2025; AstroShader: January 11, 2026) are both well within 18 months of the research date (2026-08-10). No app in the table was confirmed to be stale/abandoned. However, 8 of 10 apps have no confirmed update date, so this flag is not fully verifiable across the set — treat as false based on partial evidence, not full evidence.

**3. Top 3 results are all free/ad-supported with no paid alternative — FALSE**
Reasoning: Clearly false. PhotoPills ($10.99, one-time/premium unlock) and NightCap Camera ($2.99) are both paid apps and both surfaced at or near the top of the first general query ("astrophotography app iphone app store"). AstroEdit is also a paid app ($1.99–$2.99) with an optional subscription. There is a real mix of free (Stardust, Telescopius, AstroShader, Astro Stacker) and paid (PhotoPills, NightCap Camera, AstroEdit) apps in the niche, so a paid alternative clearly exists and appears prominently.

**4. Fewer than 5 results that genuinely match the keyword (i.e. niche is underserved) — FALSE**
Reasoning: Search turned up well over 10 distinct, genuinely on-topic apps across capture/stacking (AstroShader, NightCap Camera, Astro Stacker, AstroEdit), planning (PhotoPills, Astrophotography Planner, Dark Skies, Astro Planner, SkyPlanner, Nightlog, Telescopius, AstroGuide, Telescope Assist), and exposure calculation (Star Exposure Calculator, Astro Max Calculator, Exposure Pro Calc) sub-niches — comfortably more than 5 genuine matches. The niche is not underserved in terms of raw app count; if anything it looks moderately crowded with many small/low-download entrants alongside a couple of established leaders (PhotoPills, NightCap Camera).

## Overall assessment

The astrophotography niche has a real, moderately crowded competitive set — at least two well-established, well-rated, monetized incumbents (PhotoPills at 4.70/5 with ~1,500 ratings, and NightCap Camera at ~4.4/5 with ~2.6K ratings) alongside a long tail of small, recently-updated, low-review-count apps (AstroEdit: 7 ratings; AstroShader: ~80 ratings) — suggesting demand exists but the top slots are already reasonably well served, so a new entrant would need meaningful differentiation rather than relying on an underserved-niche argument. Confidence in this assessment is low-to-moderate: exact rating counts, prices, and update dates could not be independently confirmed for the majority of apps (Telescopius, Stardust, Astrophotography Planner, Dark Skies, Nightlog, Astro Stacker) because the iTunes Search API and App Store review feeds were unreachable, and several numeric figures found via WebSearch conflicted between sources (e.g., NightCap Camera's rating count, AstroShader's rating), so all figures above should be treated as directional rather than authoritative pending direct App Store verification.
