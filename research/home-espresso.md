# Home Espresso — Phase 2 Demand + Competition

Research constraint: the iTunes Search API and App Store customer-reviews RSS feed were
unreachable from this environment (apple.com blocked at the egress proxy, confirmed via
curl/WebFetch — both returned EGRESS_BLOCKED). All findings below come from the WebSearch
tool only — i.e. Google-indexed snippets of App Store pages and third-party sites, not
direct API/page reads. Every number is labeled with how it was obtained; anything not
directly stated in a search snippet is marked "unverified."

## Search methodology (WebSearch queries run, in order)

1. `espresso app iphone app store`
2. `site:apps.apple.com espresso`
3. `coffee brewing log app ios`
4. `espresso shot timer app iOS`
5. `coffee dialing in app ios`
6. `"My Espresso" app store rating reviews espresso recipes`
7. `"Good Espresso" app store rating reviews price`
8. `"Dial In Espresso" app store id6752831404 rating price`
9. `"Espresso Journal" app id6743636008 app store rating price`
10. `"Espresso Shot Timer" id6756847065 app store rating price developer`
11. `"Smart Espresso Profiler" app store rating price reviews`
12. `"Simple Espresso Timer" id889735610 app store rating price developer`
13. `"Tmpr" dial in timer app store id6473798369 rating price`
14. `"Dial In Coffee" espresso id6746680844 rating reviews price app store`
15. `"Coffee Journal" "Dialed In" id6740733568 app store rating price`
16. `best espresso dialing in apps 2026 review roundup home barista`
17. `"Espresso Timer" id503961642 app store rating price last updated`
18. `espresso tracking app "4.8 stars" OR "4.9 stars" OR "ratings" app store home barista`
19. `PUCK YEAH espresso tracking app comparison ratings`
20. `"Doppio" "Barista's Book" app store rating reviews price id1209190124`
21. `Beanconqueror iOS app store rating reviews`

## Apps found

Sorted roughly by how much verifiable detail surfaced. All are real listings with real
`apps.apple.com` URLs returned by search — no names were invented.

| # | App name | Developer | App Store URL | Price | Rating | Rating count | Last updated |
|---|----------|-----------|----------------|-------|--------|---------------|--------------|
| 1 | Beanconqueror | open-source community project | https://apps.apple.com/us/app/beanconqueror/id1445297158 | Free, no ads, no paywall (stated in reviews snippet) | ~4.9/5 — stated in a third-party review-aggregator snippet (justuseapp.com), not the App Store page itself | unverified — not found (no count surfaced) | unverified — not found |
| 2 | Doppio – Barista's Book | Appwise GmbH | https://apps.apple.com/us/app/doppio-baristas-book/id1209190124 | unverified — not found (older, established app, some features reportedly paywalled per a comparison blog) | ~4.7/5 — stated directly in search snippet from an app-info aggregator (appadvice/mwm.ai style page), not confirmed on Apple's own page | unverified — not found | unverified — not found |
| 3 | PUCK YEAH! Espresso Tracker | Puck Yeah (puckyeah.app) | https://apps.apple.com/au/app/puck-yeah-espresso-tracker/id6758027038 (also https://apps.apple.com/app/id6758027038) | Free (self-described "free forever, no signup" per developer's own blog) | 5.0/5 — stated in search snippet, sourced from the developer's own blog post, not an independent confirmation | 6 ratings — stated in the same snippet | unverified — not found (App-Store ID pattern suggests a 2025/2026 release) |
| 4 | Smart Espresso Profiler | Kávékalmár / hu.kavekalmar.sep | https://apps.apple.com/us/app/smart-espresso-profiler/id1391707089 | Free (stated) | iOS rating: unverified — not found (App Store page not directly reachable). A cross-listed Android build shows 4.62/5 from 49 ratings per Google Play snippet — NOT the same store, do not treat as iOS confirmation | iOS count: unverified — not found | unverified — not found |
| 5 | Dial In Coffee: Espresso | Samast Varma | https://apps.apple.com/us/app/dial-in-coffee/id6746680844 | Free with in-app purchases ("Dial In Pro" paid tier) — stated in snippet | Search snippet explicitly states the app "hasn't received enough ratings or reviews to display an overview" on at least one storefront | unverified — explicitly below Apple's display threshold | unverified — not found; requires iOS 18.0+ per snippet, implying a recent build |
| 6 | Dial In Espresso | unverified — not found (developer name not surfaced) | https://apps.apple.com/us/app/dial-in-espresso/id6752831404 | Free with in-app purchases — stated in snippet | Search snippet explicitly states "not received enough ratings or reviews to display an overview" | unverified — explicitly below Apple's display threshold | unverified — not found |
| 7 | My Espresso | unverified — not found (also on Google Play as club.myespresso.myespresso_flutter) | https://apps.apple.com/us/app/my-espresso/id6479243211 | unverified — not found; has a "Premium" AI-feedback tier per snippet, implying a paid/subscription upsell | Search snippet: US App Store "hasn't received enough ratings or reviews to display an overview" | unverified — explicitly below Apple's display threshold | unverified — not found |
| 8 | Good Espresso | unverified — not found | https://apps.apple.com/us/app/good-espresso/id6443742140 | unverified — not found | unverified — not found (search explicitly returned no rating/price data) | unverified — not found | unverified — not found |
| 9 | Espresso Journal | Gruffydd Johnston (per one snippet) | https://apps.apple.com/us/app/espresso-journal/id6743636008 | Free — "no subscriptions and no ads" per snippet | Search snippet: "not received enough ratings or reviews to display an overview" | unverified — explicitly below Apple's display threshold | unverified — not found |
| 10 | Espresso Shot Timer | Jan Hartje (per one snippet) | https://apps.apple.com/us/app/espresso-shot-timer/id6756847065 | unverified — not found | Search snippet: "hasn't received enough ratings or reviews to display an overview" | unverified — explicitly below Apple's display threshold | unverified — not found; requires iOS 15.1+ per snippet |

Other real, distinct listings that surfaced in the same searches but were not carried into
the table above (mentioned here for completeness, not fabricated): Simple Espresso Timer
(id889735610, dev. Peter Bodskov), Espresso Timer (id503961642, dev. Nittontjugo AB), Tmpr
(id6473798369, dev. Lorenzo Polato), Coffee Journal | Dialed In (id6740733568, dev. Bart
Jacobs), Dialed-In (id6753701921), Dialed In – Espresso Tracker (id6759168523), Dialled In
(id6480353140), Crema – Espresso Journal (id6743380780), Espresso Notes: Brew Journal
(id6741871815), EspressoLog – Shot tracker (id6753608360), Pucky – AI Espresso Journal
(id6759039944), Home Barista: Brew Like a Pro (id6670609994), Brewprint
(getbrewprint.app, App Store ID not directly captured in a snippet), Coffee Book: Brew
Timer (id1512681263), Timer.Coffee (timer.coffee, App Store ID not captured), iBrewCoffee
(id1523175532). None of these had rating/price data surface in the searches, so they were
excluded from the detail table to avoid guessing.

## Opportunity flags

- **Top apps average <4.0 stars with >200 ratings — UNCLEAR / likely FALSE, but unconfirmed.** None of the searches surfaced any app with a confirmed rating count above single digits. The only two apps with numeric ratings at all were PUCK YEAH! (5.0/5, 6 ratings — sourced from the developer's own blog, not Apple) and a cross-platform Android figure for Smart Espresso Profiler (4.62/5, 49 ratings — wrong store, not usable as iOS evidence). Multiple other listings (Dial In Espresso, Dial In Coffee, My Espresso, Espresso Journal, Espresso Shot Timer) explicitly returned the App Store's own "not enough ratings or reviews to display an overview" message. That phrasing implies each is below Apple's undisclosed display threshold (commonly believed to be under ~5 ratings), which is the opposite of ">200 ratings" — so the flag as stated cannot be true for the apps we found, but I could not directly confirm any exact rating count via the (blocked) API, so I'm not fully confident no such app exists.

- **Top apps not updated in >18 months — UNCLEAR, leaning FALSE.** No exact "last updated" date was confirmed for any app (the App Store's version-history page was unreachable). However, several apps have App Store numeric IDs in the 675xxxxxxx–676xxxxxxx range (Dial In Espresso, Dial In Coffee, Espresso Journal, Espresso Shot Timer, PUCK YEAH!, EspressoLog, Pucky, Dialed In – Espresso Tracker), which is consistent with very recent (2025/2026) app creation, and one snippet stated a minimum iOS 18.0 requirement (Dial In Coffee) — iOS 18 shipped in 2024, so that app cannot be more than about 18 months old. This circumstantially suggests the opposite of the flag: this niche has seen a wave of new entrants very recently, not staleness. Older/legacy apps like Doppio, Simple Espresso Timer, and Espresso Timer (Nittontjugo) may or may not be stale — no update date was recoverable for them either.

- **Top 3 results are all free/ad-supported with no paid alternative — FALSE.** Mixed monetization is evident: Beanconqueror is explicitly free/ad-free/no-paywall; but Dial In Coffee has a "Dial In Pro" paid upgrade tier, My Espresso has a "Premium" AI-feedback tier, and Doppio reportedly paywalls some advanced features per a third-party comparison blog. So the market already contains both free-forever apps and freemium/paid-tier apps — there is a paid alternative pattern, not a free-only market.

- **Fewer than 5 results that genuinely match the keyword (i.e. niche is underserved) — FALSE.** Searches surfaced well over 20 distinct, real, on-topic espresso-dialing/shot-timer/coffee-journal iOS apps with real apps.apple.com URLs (see table plus the "other listings" list above). This is a densely populated micro-niche, not underserved — if anything it looks crowded with many near-identical "log your shot, dial in your grind" journal apps launched in the last 1–2 years.

## Overall assessment

This niche looks saturated rather than underserved: well over 20 distinct, real espresso-journal/shot-timer/dial-in apps were found, several launched in just the last year, spanning free/open-source (Beanconqueror), free-with-tips (PUCK YEAH!), and freemium/subscription models (Dial In Coffee, My Espresso), so a new entrant would be competing against many close functional clones rather than filling a gap. Confidence in this read is moderate, not high — the App Store's own rating/count/update-date data was unreachable in this environment, so the "most apps have very few ratings" signal rests on indirect cues (Apple's own "not enough ratings to display" wording, one directly-sourced 6-rating data point, and a non-comparable Android rating figure) rather than confirmed numbers, and several fields for nearly every app are marked unverified above.
