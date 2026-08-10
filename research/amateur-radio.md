# Amateur Radio — Phase 2 Demand + Competition

**Note on method:** The iTunes Search API and App Store customer-reviews RSS feed were unreachable this session (all apple.com domains blocked at the network egress proxy — confirmed via curl/WebFetch, both returned EGRESS_BLOCKED). All data below comes from WebSearch snippets (search-result summaries, third-party App Store mirror/analytics sites like AppBrain, and blog posts), not from direct App Store pages. Anything not explicitly stated in a search snippet is marked "unverified."

## Search methodology (WebSearch queries run)

1. `ham radio app iphone app store`
2. `site:apps.apple.com ham radio`
3. `amateur radio license exam prep app ios`
4. `ham radio logging app ios App Store`
5. `technician license practice test app ios App Store`
6. `"HamStudy.org" app store reviews rating price`
7. `"Ham Radio Prep" app store rating reviews price subscription`
8. `"HAM Test Prep" Technician app store rating reviews price`
9. `"Ham Radio Toolbox" app store rating reviews price`
10. `"QRV" ham radio multitool app store rating reviews price`
11. `"HamLog" app store rating reviews price ham radio logbook`
12. `"Ham Logger" BioRust app store rating reviews price`
13. `"POTAontheGO" app store rating reviews price`

## Apps found

All URLs below appeared directly in WebSearch results (apps.apple.com links); app IDs are taken verbatim from the returned URLs.

| # | App name | Developer/Seller | App Store URL | Price | Rating (stars) | Rating count | Last updated |
|---|----------|-------------------|----------------|-------|-----------------|---------------|--------------|
| 1 | HamStudy.org (exam prep) | HamStudy.org (org unverified — not confirmed by name in snippets) | https://apps.apple.com/us/app/hamstudy-org/id1371288324 | $3.99 (per search snippet; could not confirm if this is upfront price or if IAP also exists) | unverified for iOS — only a Google Play figure (4.98★) was found, not attributable to the iOS listing | unverified — Google Play snippet cited "1.3 thousand ratings" but that is Android, not iOS; iOS count not found | unverified — not found |
| 2 | Ham Radio Prep | Critical Communications Media (inferred from Android package `com.criticalcommunicationsmedia.hamradioprep3`; not explicitly confirmed as the iOS seller name) | https://apps.apple.com/us/app/ham-radio-prep/id1525090989 | Free to download; in-app purchases found: Technician course $34.99, General+Technician $55.00, Full Course Access (all levels) $79.99, Video Bundle $49.99 | unverified for iOS — 4.67★ figure found was explicitly for Android; Trustpilot (a separate, non-App-Store source) shows 5★ from 1,431 reviews, but that's for the company/site, not the iOS app listing | unverified — not found for the iOS listing specifically | unverified — not found |
| 3 | HAM Test Prep: Technician | Patrick J Maloney LLC (named explicitly in one snippet) | https://apps.apple.com/us/app/ham-test-prep-technician/id297951496 | unverified — snippet found a $99.00 price for the separate "General" version; Technician-specific price not stated | unverified — not found | unverified — not found | Question pool described as "effective July 1, 2026" / "valid through June 30, 2026," implying an active, recently-updated question set, but the actual app-binary update date is unverified |
| 4 | HAM Test Prep Lite: Technician | Patrick J Maloney LLC (inferred, same series as #3) | https://apps.apple.com/us/app/amateur-radio-exam-prep-free-technician/id303413588 | Free (Lite version, limited to 2 of 10 subelements per snippet) | unverified — not found | unverified — not found | unverified — not found |
| 5 | Ham Radio Toolbox | Nuno Facha (named explicitly in one snippet, distinct from HAM-Toolbox below) | https://apps.apple.com/us/app/ham-radio-toolbox/id6745102884 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |
| 6 | HAM-Toolbox | Marcus Roskosch (named explicitly in one snippet) | https://apps.apple.com/us/app/ham-toolbox/id1630108109 | £9.99 (per snippet; USD equivalent not separately confirmed) | unverified — not found | unverified — not found | unverified — not found |
| 7 | QRV - Ham Radio Multitool | unverified (developer name not stated in snippets; getqrv.com is the product site) | https://apps.apple.com/us/app/qrv-ham-radio-multitool/id6754951380 | Free to download; "QRV Premium" available as subscription or lifetime IAP (exact price unverified) | 4.89★ (per AppBrain-sourced snippet, appears iOS-specific) | 65 ratings (per same snippet) | Actively updated — companion blog posts show versions 1.13 (Mar 2026), 1.17 (May 2026), 1.18 (May 2026), 1.24 (Jul 2026), i.e. updated within the last month as of this research date (2026-08-10) |
| 8 | HamLog | N3WG (developer credited in an eham.net review link, "Reviews For: HamLog by N3WG") | https://apps.apple.com/us/app/hamlog/id308437400 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |
| 9 | Ham Logger: Ham Radio Logbook | BioRust Studios, LLC (named explicitly) | https://apps.apple.com/us/app/ham-logger-ham-radio-logbook/id6766154018 | Free (contains ads and in-app purchases per snippet) | iOS: snippet explicitly states "hasn't received enough ratings or reviews to display an overview" (i.e., iOS rating unverified/too new); a related Google Play listing under the same studio shows 4.0★ but that is Android, not this iOS app | iOS: unverified — not found (too few to display, per snippet); Android sibling cited "139 reviews" but is a different platform listing | unverified — not found (app ID suggests a newer listing) |
| 10 | POTAontheGO - POTA Ham Radio | unverified (developer name not stated) | https://apps.apple.com/us/app/potaonthego-pota-ham-radio/id6761618786 | Free with in-app purchases | iOS: snippet explicitly states "not received enough ratings or reviews to display an overview" | unverified — not found; AppBrain cites "1.2 thousand downloads, 310 in the last 30 days" but that is a download estimate, not a rating count | unverified — not found; described as "relatively new" |

Additional real apps that surfaced in searches but were not deep-dived (name/URL only, all other fields unverified — not found): **Ham Radio Reference** (apps.apple.com/us/app/ham-radio-reference/id521128828), **ECHOCAT - Ham Radio Remote** (id6766321194), **HAMQ: Ham Radio Tools** (id6754198942), **Ham Extra** (id368585383), **Ham Radio Exam - General** (id604697509), **HamRadar** (id6755948672), **Ham2K Portable Logger** (id6478713938).

## Opportunity flags

1. **Top apps average <4.0 stars with >200 ratings — UNCLEAR / leans FALSE.** No iOS-specific data point found meets the ">200 ratings" bar at all — the only iOS-attributable rating figure we could confirm is QRV at 4.89★/65 ratings (well above 4.0, but under 200 ratings). Two other prominent apps (Ham Logger, POTAontheGO) explicitly have "not enough ratings to display" on iOS. The only >1,000-rating figures found (HamStudy.org 4.98★/1.3k, Ham Radio Prep 4.67★/1.2k) are Android-side, not iOS, and both are high, not low. So on the evidence available, there is no sign of a widely-rated-but-poor-quality leader; if anything the visible ratings are strong. Confidence is low because true iOS rating counts could not be pulled directly (proxy block).

2. **Top apps not updated in >18 months — FALSE.** QRV shows a clear, frequent update cadence with dated blog posts through v1.24 in July 2026 (within the last month of this research date, 2026-08-10). The HAM Test Prep exam-prep apps reference question pools "effective July 1, 2026," implying content is being refreshed on an ongoing basis tied to FCC question-pool cycles. No evidence of stale/abandoned leaders was found.

3. **Top 3 results are all free/ad-supported with no paid alternative — FALSE.** Clear paid alternatives exist across categories: HamStudy.org ($3.99 flat), HAM-Toolbox (£9.99), and Ham Radio Prep (freemium with $34.99–$79.99 course IAPs). The category is a mix of paid, freemium/IAP, and free/ad-supported apps, not a free-only field.

4. **Fewer than 5 results genuinely match the keyword (niche underserved) — FALSE.** At least 10 distinct, real, currently-listed apps were found directly matching ham-radio-related search terms, spanning three sub-categories: exam prep (HamStudy.org, Ham Radio Prep, HAM Test Prep + Lite), logging (HamLog, Ham Logger, POTAontheGO), and toolbox/reference (Ham Radio Toolbox, HAM-Toolbox, QRV, Ham Radio Reference). The niche is not underserved — it has multiple established, category-spanning competitors.

## Overall assessment

The amateur-radio niche on iOS looks competitive rather than underserved: there are established, actively-updated, reasonably well-rated apps in each obvious sub-niche (exam prep, contact logging, operating toolbox/reference), including at least one (QRV) with a visibly strong rating and a fast, ongoing update cadence, and at least one paid, long-standing incumbent in exam prep (HamStudy.org). Confidence in this read is moderate-to-low, however, because the App Store's own rating counts and update timestamps could not be fetched directly this session (iTunes Search API and the reviews RSS feed were blocked) — the figures above are drawn from search snippets and third-party trackers (AppBrain, Trustpilot, Google Play) that don't always map 1:1 onto the actual iOS listing, so several key cells (iOS rating counts, iOS last-updated dates, exact prices) remain explicitly unverified.
