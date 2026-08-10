# Ammo Reloading — Phase 2 Demand + Competition

Research date: 2026-08-10. Method note: the iTunes Search API and the App Store
customer-reviews RSS feed were unreachable in this environment (apple.com egress
blocked, confirmed via curl/WebFetch → EGRESS_BLOCKED). All data below was
gathered via the WebSearch tool only, using Google-style search snippets and
third-party App Store aggregator sites that surfaced in those searches (mwm.ai,
appfollow.io, appbrain.com, gunr.app) — attempts to WebFetch those aggregator
pages directly were ALSO blocked by the egress proxy (EGRESS_BLOCKED on mwm.ai
and apps.appfollow.io specifically), so even the aggregator data is limited to
whatever text appeared in the WebSearch result snippets themselves. No direct
fetch of any apple.com URL was possible, so nothing here was pulled from a live
App Store page — every number is only as reliable as the search snippet that
produced it, and most exact rating counts / update dates could NOT be confirmed.
Fields not directly confirmed are explicitly marked "unverified."

## Search methodology (WebSearch queries run)

1. `reloading app iphone app store ammunition`
2. `site:apps.apple.com reloading ammo`
3. `handload log app ios`
4. `ballistics reloading data app ios app store`
5. `reloading recipe tracker app ios`
6. `"ReLOADeD" ammo app price rating reviews App Store`
7. `"My Armory" app reloading reviews rating App Store`
8. `"Hornady Reloading Guide" app price rating reviews`
9. `"Reloading Assistant" app price rating reviews App Store id1326713458`
10. `"Load Data" reloading app iOS price rating id1197957618`
11. `"Handloader" app id905933887 price rating reviews App Store`
12. `"RCBS Reloading App" price rating reviews App Store id1559610918`
13. `"GUNR" "Cost of Reloading" app price rating reviews id1611169183`
14. `"Gun Shot and Reload" app price rating reviews id1254083079`
15. `"Vihtavuori Reload" app price rating reviews id1071540632`
16. `"Hand-Load" app reloading cost calculator iOS App Store`
17. `"Load Data Suite" app iOS App Store id1553711058 price rating`
18. WebFetch attempts (blocked): `gunr.app/blog/best-reloading-apps-compared`, `mwm.ai/apps/reloaded-ammo/1386315383`, `apps.appfollow.io/ios/vihtavuori-reload/1071540632`

Note on a false positive: query 14 ("Gun Shot and Reload", id1254083079) surfaced
in earlier keyword searches because it contains the word "reload," but its actual
App Store description is a gunshot-sound-effects/soundboard entertainment app
(AVAudioEngine-synthesized weapon sounds for tabletop gaming), not a handloading/
ammunition-reloading utility. It is excluded from the "Apps found" table below as
not a genuine competitor, and a genuine 10th app (Load Data Suite) is used instead.

## Apps found

| # | App name | Developer/seller | App Store URL | Price | Rating | Rating count | Last updated |
|---|---|---|---|---|---|---|---|
| 1 | ReLOADeD (Ammo) | unverified — not confirmed as the App Store "Seller" field; app is referenced consistently under this name only | https://apps.apple.com/us/app/reloaded-ammo/id1386315383 | $3.99 (per search snippet) | 4.1 / 5 (per search snippet, source/region not specified) | unverified — not found | unverified — not found |
| 2 | My Armory | unverified — not found | https://apps.apple.com/us/app/my-armory/id1491569076 | Free (per user-review snippet: "app is free, very customizable") | unverified — snippet explicitly states "not received enough ratings or reviews to display an overall rating overview" | unverified — not found (implied very low/near-zero given above) | unverified — not found |
| 3 | Hornady Reloading Guide | Hornady Manufacturing, Inc. | https://apps.apple.com/us/app/hornady-reloading-guide/id1451643677 | Free to download; à la carte 99¢ per cartridge, $19.99 for full 12th edition, or $19.99/year subscription for full data + updates (per search snippet) | 4.6 / 5 (iOS, per search snippet) | 13,384 ratings (iOS, per search snippet) | unverified — not found (thefirearmblog.com article referencing app pricing changes dated May 2024, not confirmed as "last updated") |
| 4 | Reloading Assistant | Polycompsol LLC (per mwm.ai / appshunter.io snippets) | https://apps.apple.com/us/app/reloading-assistant/id1326713458 | unverified for iOS — not found (features "31,000+ recipes" from Accurate, Alliant, Hodgdon, Somchem, Vihtavuori) | unverified — snippet explicitly states "not enough ratings or reviews to display an overview" | unverified — not found (implied very low/near-zero) | unverified — not found |
| 5 | Load Data | unverified — not found | https://apps.apple.com/us/app/load-data/id1197957618 | $1.99 per a 2021 Sniper's Hide forum post (search result explicitly flagged this may be outdated) | unverified — not found | unverified — not found | unverified — not found |
| 6 | GUNR — Cost of Reloading | SPAZA DOT TECH (PTY) LTD | https://apps.apple.com/us/app/gunr-cost-of-reloading/id1611169183 | Free base calculator; "COR Pro" IAP unlocks advanced features (exact price unverified) | unverified — snippet states "not enough ratings or reviews to display an overview on some app store regions" | unverified — not found | unverified — not found |
| 7 | Handloader | Magzter Inc. | https://apps.apple.com/us/app/handloader/id905933887 | Free download with 7-day trial; $10.99/6mo or $12.99/yr auto-renewing subscription (per search snippet) — note: this is a digital-magazine subscription app (reloading journal/publication), not primarily a load-data database or inventory tracker | unverified — not found | unverified — not found | unverified — not found |
| 8 | RCBS Reloading App | Bushnell Outdoor Products (per search snippet) | https://apps.apple.com/us/app/rcbs-reloading-app/id1559610918 | Free ("Freeware" per search snippet) | unverified — not found | unverified — not found | unverified — not found (an unofficial mirror site listed version "1.37," not confirmed as current or dated) |
| 9 | Vihtavuori Reload | RightSpot Ltd (per search snippet) | https://apps.apple.com/us/app/vihtavuori-reload/id1071540632 | Free (per official vihtavuori.com resources page and search snippet) | 4.0 / 5 (per search snippet, source appears to be apps.appfollow.io aggregator, not the native App Store page itself — WebFetch of that aggregator page was blocked so this could not be directly confirmed) | 15 user reviews (per search snippet, same appfollow.io-sourced caveat as rating above) | unverified — not found |
| 10 | Load Data Suite | Jesse Haskins (per search snippet) | https://apps.apple.com/us/app/load-data-suite/id1553711058 | unverified — not found | unverified — not found | unverified — not found | unverified — not found (search snippet notes "requires iOS 13.0 or later," not a date) |

Two apps surfaced in search results but are excluded from the table above:
**Gun Shot and Reload** (id1254083079) — a gunshot sound-effects/soundboard
entertainment app, not a genuine reloading/handloading utility, despite matching
the keyword "reload." **Guns & Ammo: Point of Impact Reloaded** (id385547941) —
name match appears to be a firearms magazine/media app unrelated to handloading;
not investigated further as it did not recur across multiple queries as a
reloading-specific tool.

Additional ballistics-calculator apps surfaced that include some reloading-data
features as a secondary function, but are not primarily reloading/handload
trackers (name and URL only, not counted toward the 10 above): Ballistic App
(id1150935669, has a "Reloading Data Center" feature), Hornady Ballistics App
(id1183535443), Nimoh Ballistics (URL not captured in snippets).

## Opportunity flags

**1. Top apps average <4.0 stars with >200 ratings — FALSE (based on the only two confirmed data points)**
Only two apps in the set have both a rating AND a rating count directly surfaced
in search snippets: Hornady Reloading Guide at 4.6/5 with 13,384 ratings (well
above 4.0 and well above 200), and Vihtavuori Reload at 4.0/5 with only 15
reviews (meets the rating threshold but not the 200-rating volume threshold, and
that figure came from a third-party aggregator snippet that could not be
independently confirmed since WebFetch to appfollow.io was blocked). ReLOADeD's
4.1/5 rating has no confirmed rating count. Every other app (My Armory, Reloading
Assistant, GUNR, Handloader, RCBS, Load Data, Load Data Suite) explicitly
returned "not enough ratings to display an overview" or had no rating data at
all in search snippets — meaning most of the category may have too few reviews
to register a public average. The one high-volume data point we do have
(Hornady, the category leader) is well above 4.0 stars, so the flag reads FALSE,
but confidence is low given how few apps have any confirmed rating count.

**2. Top apps not updated in >18 months — UNCLEAR**
No confirmed "last updated" or current-version dates were found for any app via
search snippets (App Store version-history pages are not exposed in search
results, and direct fetch of apple.com or the aggregator mirrors was blocked).
The only loosely-dated signal was a thefirearmblog.com article about Hornady's
app pricing model dated May 2024, which is not a confirmation of the app's
current update date. Cannot be verified either way — marked unclear due to
near-total absence of update-date data.

**3. Top 3 results are all free/ad-supported with no paid alternative — FALSE**
The most-recurring, most-relevant apps show a clear mix of monetization models:
Hornady Reloading Guide (free download + $19.99/yr subscription or à la carte
purchases — the highest-rated, highest-review-count app in the set, and it is a
paid/freemium model, not pure free/ad-supported), ReLOADeD ($3.99 flat price),
Handloader ($10.99–$12.99 recurring magazine subscription). Free options also
exist (My Armory, Vihtavuori Reload, RCBS Reloading App, GUNR base calculator),
so the space has both free and paid apps actively competing, including the
category leader by rating volume being a paid/subscription product — the flag
as stated is false.

**4. Fewer than 5 results that genuinely match the keyword (niche underserved) — FALSE**
Search queries surfaced at least 10 distinct, real, non-game apps genuinely
targeting handloaders/reloaders (load-data databases, recipe/inventory trackers,
cost calculators, a reloading-journal subscription, and manufacturer-branded
apps from Hornady, RCBS, and Vihtavuori) — well above 5. Manufacturer-backed
entrants (Hornady, RCBS, Vihtavuori) in particular indicate the niche already
has resourced, brand-name competition, not just hobbyist indie apps. The niche
is not thin on app count.

## Overall assessment

This niche looks moderately-to-fully served rather than wide-open: there are at
least 10 real, distinct apps already targeting handloaders, including
manufacturer-backed entries (Hornady Reloading Guide, RCBS Reloading App,
Vihtavuori Reload) and the category leader (Hornady) has a strong, well-attested
4.6/5 rating across 13,384 ratings with an active paid/subscription model — that
combination argues against both the "underserved" and "no viable paid model"
opportunity flags. Confidence in this assessment is low-to-moderate: only two of
the ten apps have a directly-confirmed star rating, only one has a confirmed
rating count, and zero have a confirmed last-updated date, because the App Store
API, RSS feed, and even several third-party aggregator sites were unreachable in
this environment (all marked unverified throughout) — a follow-up pass with
direct App Store access (iTunes Search API or App Store Connect) is needed
before treating anything beyond the Hornady data point as reliable for a go/no-go
decision.
