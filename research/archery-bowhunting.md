# Archery / Bowhunting — Phase 2 Demand + Competition

Research date: 2026-08-10. Method note: the iTunes Search API and the App Store
customer-reviews RSS feed were unreachable in this environment (apple.com egress
blocked, confirmed via curl/WebFetch → EGRESS_BLOCKED). All data below was gathered
via the WebSearch tool only, using Google-style search snippets and third-party
App Store aggregator sites (appfollow.io, mwm.ai, appbrain.com) that surfaced in
those searches. No direct WebFetch of any apple.com URL was possible, so nothing
here was pulled from a live App Store page — every number is only as reliable as
the search snippet that produced it, and most exact rating counts / update dates
could NOT be confirmed. Fields not directly confirmed are explicitly marked
"unverified."

## Search methodology (WebSearch queries run)

1. `bowhunting app iphone app store`
2. `archery sight tape calculator app ios`
3. `bow tuning app ios App Store`
4. `hunting log app ios bowhunter App Store`
5. `site:apps.apple.com archery`
6. `"CapTarget Archery" app store rating reviews`
7. `"Bow Shop Bible" app store rating reviews subscription price`
8. `"Smart Sights" archery app rating reviews price`
9. `"The Bowhunting App" Grant Richardson app store rating reviews`
10. `"AccuBow" app store rating reviews price`
11. `"ArcherSense" archery coach app store rating reviews price`
12. `"PRO Archery Ballistics" app store rating reviews`
13. `"Hunting Log" Clint Tustison app store rating reviews`
14. `"BowSmith" archery tuning app store rating reviews price`

## Apps found

Only non-game, archer/bowhunter-utility-relevant apps are prioritized (pure
target-practice/arcade games like Archery Pro, Archery Elite, Archery Champ,
Archery Master, Archery Clash, Pheasant Bow Hunting Safari, Bow Hunter 2017 are
listed at the bottom for completeness but are not real competitors for a
utility/tool-style app).

| # | App name | Developer/seller | App Store URL | Price | Rating | Rating count | Last updated |
|---|---|---|---|---|---|---|---|
| 1 | AccuBow (AccuBow 2025) | unverified — search results show both "AccuBow" and "AccuBow 2025" listing titles; company likely Green Mantis (maker of AccuBow hardware), not confirmed as App Store "Seller" field | https://apps.apple.com/us/app/accubow/id1448656716 (also listed as https://apps.apple.com/us/app/accubow-2025/id1448656716) | Free to download; $30/year subscription added later per user complaints (source: search snippet, not App Store price field) | 3.70 / 5 (iOS, per search snippet) | 890 ratings (iOS, per search snippet) | unverified — not found |
| 2 | PRO Archery Ballistics | Lucas Palmer | https://apps.apple.com/us/app/pro-archery-ballistics/id6503086578 | $4.99/year or $0.59/month (per one query) — a later query described it as "monthly or yearly subscription," version 7.7.5 mentioned | 4.8 / 5 (per search snippet, source unclear — may be an aggregator average, not confirmed App Store field) | unverified — snippet explicitly said "not enough ratings to display an overview" in some regions | unverified — only version number "7.7.5" surfaced, no date |
| 3 | Bow Shop Bible (Lifetime + Subscription listed separately) | unverified — likely "STsportsllc" per Android package name `com.stsportsllc.BowShopBible` seen in search results, not confirmed as iOS Seller name | Lifetime: https://apps.apple.com/us/app/bow-shop-bible/id1492396052 ; Subscription: https://apps.apple.com/ca/app/bow-shop-bible-subscription/id1584051239 | Subscription $3.99/month (per search snippet); Lifetime ~$30 (per search snippet) | unverified — not found (forum posts describe general sentiment as positive, no star figure) | unverified — not found | unverified — not found |
| 4 | CapTarget Archery | Appli Magine | https://apps.apple.com/us/app/captarget-archery/id1584542210 | Free, "80%+ features free" per snippet; no confirmed paid tier price | unverified for iOS specifically — snippet cites "5.00/5 based on 1.1k ratings" and separately "4.9/5, 10k+ downloads," but these figures were attributed to Android/Google Play and an aggregator site (mwm.ai), not confirmed as the iOS App Store rating | unverified for iOS — the "25,000 archers" figure is a marketing claim (total users, not App Store rating count) | unverified — not found |
| 5 | ArcherSense (Archery Coach / AI Archery Coach) | Carlos Farias | https://apps.apple.com/us/app/archersense-archery-coach/id6748324853 | Subscription-based ("a little pricey" per forum comment); exact price unverified | 5.0/5 per mwm.ai (third-party tracker, not confirmed as native App Store rating) | unverified — not found | unverified — not found |
| 6 | BowSmith (Archery & Tuning) | Michal Buczko | https://apps.apple.com/in/app/bowsmith-archery-tuning/id6742581730 | Freemium; Advanced $79.99/yr or $249 lifetime, Professional $179.99/yr or $499 lifetime (per bowsmith.app pricing page, not App Store listing itself) | unverified — not found | unverified — not found | unverified — not found |
| 7 | Smart Sights | unverified — developer name not surfaced | https://apps.apple.com/us/app/smart-sights/id1515003679 | 28-day free trial, then one-time "permanent unlock" purchase; exact price unverified | unverified — search snippet explicitly states "hasn't received enough ratings or reviews to display an overview" | unverified — implied very low/near-zero | unverified — not found |
| 8 | The Bowhunting App | Grant Richardson | https://apps.apple.com/us/app/the-bowhunting-app/id6471345117 | Free per snippet ("download is free of charge") | unverified — not found | unverified — not found | unverified — not found |
| 9 | Hunting Log | Clint Tustison | https://apps.apple.com/us/app/hunting-log/id6744321718 | Free, "no hidden costs" per snippet | unverified — not found | unverified — not found | unverified — not found |
| 10 | Bowhunter Magazine | unverified — publisher likely InterMedia Outdoors / Outdoor Sportsman Group, not confirmed via search | https://apps.apple.com/us/app/bowhunter-magazine/id582697170 | unverified — likely free with in-app magazine purchases, not confirmed | unverified — not found | unverified — not found | unverified — not found |

Additional apps surfaced but excluded from the main table as they are arcade/game
titles rather than archer/bowhunter tools (name, URL only, no further data gathered):
Bow Hunt Simulator (https://apps.apple.com/us/app/bow-hunt-simulator/id1090757314),
Bow Hunter 2017 (https://apps.apple.com/us/app/bow-hunter-2017/id1140933619),
Pheasant Bow Hunting Pro (https://apps.apple.com/us/app/pheasant-bow-hunting-pro/id1401772023),
Pheasant Bow Hunting Safari (https://apps.apple.com/us/app/pheasant-bow-hunting-safari/id1397692241),
Archery Hunting Bow Shooting (https://apps.apple.com/us/app/archery-hunting-bow-shooting/id6474125849),
Archery Pro - Bow & Arrow (https://apps.apple.com/us/app/archery-pro-bow-arrow/id1450578727),
Archery Elite - Shooting King (https://apps.apple.com/us/app/archery-elite-shooting-king/id1340807472),
Archery Champ (https://apps.apple.com/us/app/archery-champ-arrow-bow/id6754099294),
Archery Master (https://apps.apple.com/us/app/archery-master-shooting-game/id1324438655),
Archery Clash (https://apps.apple.com/us/app/archery-clash/id6458097001).

## Opportunity flags

**1. Top apps average <4.0 stars with >200 ratings — TRUE (partially confirmed, weak evidence)**
Only one app in the set has both a rating AND a rating count that were actually
found in search snippets: AccuBow at 3.70/5 with 890 ratings (iOS). That single
data point satisfies the flag on its own (below 4.0, well above 200 ratings).
However, every other utility app in the list (CapTarget, ArcherSense, PRO Archery
Ballistics, Bow Shop Bible, Smart Sights, BowSmith) either has no confirmed iOS
rating count or explicitly returned "not enough ratings to display an overview"
in search snippets — meaning most of the category may have too few reviews to
even register a public average. Verdict should be read as "true for the one app
with enough volume to matter, unclear for the rest." Confidence: low, since it
rests on one confirmed data point plus several "not enough ratings" signals.

**2. Top apps not updated in >18 months — UNCLEAR**
No last-updated / current-version dates were confirmed for any app via search
snippets (App Store version-history pages are not exposed in search results, and
direct WebFetch of apple.com was blocked). The only version signal found was
PRO Archery Ballistics being on "version 7.7.5" with a recently-added AI feature
("Shot Doctor"), which suggests active development but gives no date. Cannot be
verified either way — marked unclear due to total absence of update-date data.

**3. Top 3 results are all free/ad-supported with no paid alternative — FALSE**
The search results show a clear mix of monetization models among the top,
most-relevant utility apps: AccuBow (free download, $30/yr subscription added
later), PRO Archery Ballistics ($4.99/yr or $0.59/mo subscription), Bow Shop
Bible ($3.99/mo subscription or ~$30 lifetime), BowSmith ($79.99–$499/yr or
lifetime tiers), and ArcherSense (paid subscription, described as "pricey").
Free options also exist (CapTarget, The Bowhunting App, Hunting Log, Smart
Sights' base tier), so the space has both free and paid apps, actively including
apps charging real subscription/lifetime prices — the flag as stated is false.

**4. Fewer than 5 results that genuinely match the keyword (niche underserved) — FALSE**
Search queries surfaced at least 10 distinct, real, non-game apps that
specifically target archers/bowhunters as tools (sight-tape calculators, bow
tuning, scoring, coaching, hunting logs, magazines) — well above 5. The niche is
not thin on app count; if anything it looks moderately crowded with several
niche-specific tools (Smart Sights, PRO Archery Ballistics, Bow Shop Bible,
BowSmith, CapTarget, ArcherSense) already competing on sight tapes/tuning/coaching
specifically.

## Overall assessment

This niche looks moderately, not obviously, competitive: there are at least 6-7
real, actively-monetized utility apps already serving bow tuning, sight-tape
calculation, scoring, and coaching (with real subscription/lifetime price points
up to $499), plus several free hunting-log/magazine apps, so flags 3 and 4 argue
against an "underserved, wide-open" opportunity. The one flag with real evidence
of weakness (AccuBow's 3.70-star / 890-rating gap, plus user complaints about a
paywall retrofit) hints at possible dissatisfaction with existing options, but
it's a single data point, not a category-wide pattern. Confidence in this
assessment is low-to-moderate: most rating counts, developer names, and update
dates could not be confirmed at all (marked unverified throughout) because the
App Store API and RSS feed were unreachable in this environment — a follow-up
pass with direct App Store access (iTunes Search API / App Store Connect) is
needed before treating any of these numbers as reliable for a go/no-go decision.
