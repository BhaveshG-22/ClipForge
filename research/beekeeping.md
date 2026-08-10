# Beekeeping — Phase 2 Demand + Competition

> Note on methodology: the iTunes Search API and App Store customer-reviews RSS feed were
> unreachable this session (network egress to all apple.com domains is blocked — confirmed via
> curl and WebFetch, both returned `EGRESS_BLOCKED`). WebFetch also failed on non-Apple domains
> attempted for this research (e.g. beekeeping-diary.eu, ecopeanut.com — both returned
> `EGRESS_BLOCKED` as well). All findings below come exclusively from WebSearch result snippets
> and the AI-generated summaries WebSearch returned alongside them. No live App Store page was
> opened or scraped directly. Star ratings and rating counts, in particular, should be treated as
> low-confidence unless a specific source is cited — many search snippets could not surface a
> hard rating number at all.

## Search methodology (WebSearch queries run)

1. `beekeeping app iphone app store`
2. `site:apps.apple.com beekeeping`
3. `hive inspection log app ios`
4. `beekeeper app ios apiary management`
5. `"Beekeeper App" app store reviews rating id1517686137`
6. `"Apiarist" "Beekeeper Assistant" app store rating reviews price`
7. `BeePlus beekeeping app store rating price reviews`
8. `"Beehive: Beekeeping Manager" app store rating reviews price`
9. `"HiveHelp.AI" beekeeper app store rating price`
10. `"Apiary Book" ApiNote beekeeping app store rating price`
11. `"HIVESOUND" beekeeping assistant app store rating`
12. `"BeeKeepPal" app store rating reviews`

Two follow-up WebFetch attempts (on beekeeping-diary.eu and ecopeanut.com listicle articles, to
try to cross-reference aggregate rating data) both failed with `EGRESS_BLOCKED`, so those sources
could not be read directly — only WebSearch's own snippet/summary of them was available, and in
practice those two sites did not surface further in the WebSearch summaries used below.

## Apps found

All 10 apps below have a real, distinct App Store URL that appeared directly in WebSearch results
(numeric App Store ID confirmed in the URL). None were invented.

| # | App name | Developer/seller | App Store URL | Price | Avg. rating | Rating count | Last updated |
|---|----------|-------------------|----------------|-------|-------------|---------------|--------------|
| 1 | Beekeeper App | unverified — not found | https://apps.apple.com/us/app/beekeeper-app/id1517686137 | Subscription: $14.99/mo or $149.99/yr (per WebSearch summary of app description) | unverified — not found | unverified — not found | unverified — not found |
| 2 | HiveHelp.AI: Beekeeper's App | unverified — not found | https://apps.apple.com/us/app/hivehelp-ai-beekeepers-app/id6469013696 | unverified — not found (free w/ IAP per one snippet, no $ figure given) | ~3.7★ — **caveat: this figure was reported for the Google Play/Android listing** (via chrome-stats.com search snippet), not confirmed for the iOS App Store listing | unverified — not found (Android snippet said "5,000+ downloads," not a rating count) | unverified — not found |
| 3 | Apiary Book Beekeeping ApiNote | Petr Drabek (per mwm.ai snippet) | https://apps.apple.com/us/app/apiary-book-beekeeping-apinote/id6752503587 | Free (tracks up to 5 hives) with Pro at ~€2.99/mo (per WebSearch summary) | 3.83★ — **caveat: this figure came from AppBrain, which was describing the Android build**, not confirmed for iOS | 110 ratings — **same Android-only caveat as above** | unverified — not found |
| 4 | HiveBook - Beekeeping Tracker | unverified — not found | https://apps.apple.com/us/app/hivebook-beekeeping-tracker/id6759789680 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |
| 5 | Apiarist - Beekeeper Assistant | Oleg Soloviev (per mwm.ai snippet) | https://apps.apple.com/us/app/apiarist-beekeeper-assistant/id1436515928 | Free (per WebSearch summary; unlimited apiaries/hives) | 4.6★ — sourced from mwm.ai third-party app-data aggregator snippet, not Apple's own page | "1K+ downloads" reported by mwm.ai — this is a download-volume bucket, not an actual rating count, so treat the rating-count cell as unverified — not found | unverified — not found (mwm.ai snippet mentioned "recent updates include cloud sync," implying active maintenance, but no date given) |
| 6 | Beehive: Beekeeping Manager | Moonbeam Catcher LLC (per WebSearch summary of App Store description) | https://apps.apple.com/us/app/beehive-beekeeping-manager/id6759832883 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |
| 7 | BeePlus Beekeeping Manager | OmniChrome | https://apps.apple.com/us/app/beeplus-beekeeping-manager/id1018655661 (also seen at id .../beeplus/id1018655661) | Free with ads, or ~€1.99 one-time unlock (per WebSearch summary) | "5.0" reported on AppRecs.com (third-party aggregator, not Apple's own page — sample size unknown) | unverified — not found | unverified — not found |
| 8 | HIVESOUND Beekeeping Assistant | HIVESOUND GmbH | https://apps.apple.com/us/app/hivesound-beekeeping-assistant/id6673906958 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |
| 9 | Hive Logger: Beekeeping Hub (also listed as "Hive Trackr: Beekeeping Log" — same numeric App Store ID 6670728627 appeared under both titles, so this is very likely one app that was renamed/re-titled between search results) | unverified — not found | https://apps.apple.com/us/app/hive-logger-beekeeping-hub/id6670728627 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |
| 10 | BeeKeepPal | Akeem Murray (per WebSearch summary of App Store listing) | https://apps.apple.com/us/app/beekeeppal/id1598404588 | unverified — not found | unverified — not found. Note: WebSearch summary explicitly states the Belgian App Store listing "has not received enough ratings or reviews to display an overview" — i.e. this is a low/near-zero-review app, not just an unknown number | unverified — not found (same near-zero-review signal as above) | unverified — not found |

Additional distinct apps that surfaced in the same searches but were not carried into the table
above (to keep the list to 10; listed here for completeness, none verified beyond
name+URL): Beekeeping - Hive Inspections ("Beesly", id6748213481), Beekeeping Tracker - Hive
(id6759574093), Beehive Inspection Log (id6759952378), Hive Inspect (id6737940474), HiveHelper
(id6760438195), AI BeeKeeper Voice Assistant (id1669773506), ApiManager (id1489101606),
HiveBloom (id1490920620), "Beekeepings" (id6476917281, region-specific listing, name unclear).
This brings the total count of genuinely distinct real App Store beekeeping apps surfaced across
all queries to at least 19.

## Opportunity flags

- **Top apps average <4.0 stars with >200 ratings — UNCLEAR / cannot verify.**
  No app in this research had a rating count from the iOS App Store itself confirmed at all, let
  alone above 200. The only numeric rating+count pair found (ApiNote: 3.83★ / 110 ratings) is
  sourced from an Android-focused aggregator (AppBrain), not the iOS App Store, and its count
  (110) is below the 200 threshold anyway. Apiarist's "4.6★" and BeePlus's "5.0" both come from
  third-party app-data sites with no disclosed sample size. Given the blocked iTunes API, this
  flag cannot be confirmed true or false — treat as unresolved pending direct App Store access.

- **Top apps not updated in >18 months — UNCLEAR / cannot verify.**
  No search result surfaced a specific "last updated" date or version-history date for any app.
  Indirect signals point the other way: several App Store IDs (Beehive: Beekeeping Manager,
  Beekeeping Tracker - Hive, HiveBook, Apiary Book ApiNote, Beehive Inspection Log — all with IDs
  in the 675x–676x range, which Apple assigns sequentially at submission time) look like very
  recent 2025/2026 submissions, and the Apiarist summary mentioned "recent updates include cloud
  sync and route optimization." This suggests active, recent development across much of the
  category rather than staleness, but no field is directly confirmed — this flag should not be
  marked true.

- **Top 3 results are all free/ad-supported with no paid alternative — FALSE.**
  The most repeatedly-surfacing / most established-looking apps show a real mix of business
  models: Beekeeper App is subscription-priced ($14.99/mo or $149.99/yr per its own description),
  ApiNote is freemium (~€2.99/mo Pro tier), and BeePlus offers a paid one-time unlock (~€1.99) as
  an alternative to its free/ad-supported tier. Paid and freemium options clearly exist alongside
  free apps, so this flag is false.

- **Fewer than 5 results that genuinely match the keyword (niche is underserved) — FALSE.**
  At least 19 distinct, real, beekeeping-specific App Store listings surfaced across four broad
  discovery queries (hive inspection loggers, apiary managers, AI-assisted hive tools, etc.), with
  10 carried into the detail table above. This is a well-populated, actively-developed niche by
  app count — not an empty/underserved keyword space.

## Overall assessment

By sheer count and apparent submission recency, the beekeeping/apiary-management niche looks
crowded rather than underserved — at least 19 distinct real iOS apps were found, spanning free,
freemium, and subscription pricing, with several apps that look like recent (2025/2026) launches
still actively iterating (AI hive-inspection features, QR-code logging, BLE sensor integration).
However, confidence in this being a genuine "avoid, it's saturated" signal is **low**, because the
one metric that matters most for a Phase 2 competition read — actual App Store rating counts and
review volume — could not be verified for a single app in this session (the iTunes Search API and
review RSS feed were both blocked). The apparent volume of apps could reflect either a validated,
healthy market or a graveyard of low-traction hobby apps with near-zero real ratings (BeeKeepPal's
"not enough ratings to display" note is a hint toward the latter for at least one entry) — this
distinction requires direct App Store API access to resolve and should be re-run once that egress
path is available.
