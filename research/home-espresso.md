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

---

## Phase 3 — Pain Mining

Environment constraints for this phase (confirmed live, not assumed): the App Store customer-reviews
RSS feed and all `apple.com`/`apps.apple.com` URLs are unreachable (`EGRESS_BLOCKED`), as in Phase 2.
Beyond that, `WebFetch` was tested against a wide range of **non**-Apple domains this phase, and
almost all of them also returned `EGRESS_BLOCKED`: `justuseapp.com`, `play.google.com`, `mwm.ai`,
`alternativeto.net`, `www.coffeegeek.com`, `www.home-barista.com`, `www.kaffee-netz.de`,
`www.puckyeah.app`, and `www.reddit.com` were all blocked when fetched directly. The one domain that
did work was `github.com` — several Beanconqueror GitHub issue pages were fetched successfully and
are quoted directly below. Everything else in this section is a WebSearch snippet, not a direct page
read, and is labeled as such. No review text, usernames, or forum posts were invented — where a
thread exists only as a title+URL from a search snippet with no recoverable body text, that limitation
is stated explicitly rather than filled in.

### Incumbents reviewed (name which 2 apps and why)

1. **Beanconqueror** — chosen because it is the only app in the Phase 2 list with a genuine
   independent footprint outside the App Store: it is open-source (github.com/graphefruit/Beanconqueror)
   with an active public issue tracker (issues numbered past #1150, i.e. well over a thousand
   filed over its lifetime), it is also distributed on Google Play with its own review stream, and
   it surfaced in more third-party aggregator/blog mentions than any other app in the list. GitHub
   issues were directly fetchable in this environment, making it the single best source of concrete,
   attributable pain points available to this research.
2. **Doppio – Barista's Book** — chosen over PUCK YEAH! Espresso Tracker as the second pick because
   Doppio's App Store ID (`id1209190124`) is far lower/older than the 675xxxxxxx–676xxxxxxx-range IDs
   that dominate the rest of the Phase 2 list, consistent with it being a long-established app (also
   referenced as "long-established" in a WebSearch-synthesized comparison snippet), and multiple
   independent review-aggregator snippets returned actual **numeric rating-breakdown percentages**
   for it (see below) — a level of quantified signal no other app besides Beanconqueror produced.
   PUCK YEAH! by contrast had only a single self-reported data point (5.0/5 from 6 ratings, sourced
   from the developer's own blog, not an independent aggregator), so it was judged to have less
   independently-indexed review volume than Doppio despite being more prominent in raw search-result
   frequency.

### Complaint themes

All Beanconqueror items below are corroborated by at least one directly-fetched GitHub issue page;
items marked "(WebSearch synthesis only)" come from a search engine's summarized answer over
third-party review-aggregator pages (chiefly justuseapp.com) that could not be fetched directly, so
the underlying review text could not be independently re-verified — treat those as lower-confidence
than the GitHub-sourced items.

**Theme: Data loss / backup reliability (Beanconqueror) — 4 distinct mentions found**
- GitHub issue #355, "Data loss with Version 6.1 - Android" (opened Apr 26, 2022, directly fetched)
  — a filed bug report about data loss on that release.
- GitHub issue #284, "Enhancement: Automatic backup" (directly fetched) — describes that if a user
  doesn't open the app for an extended period (e.g. a month), the backup routine "will immediately
  delete all accumulated backups" on next launch, i.e. the auto-backup logic itself causes loss for
  infrequent users.
- A home-barista.com forum thread exists specifically titled "Beanconqueror - data loss" at
  https://www.home-barista.com/brewing/beanconqueror-data-loss-t95136.html (title/URL confirmed via
  WebSearch; body not fetchable — `EGRESS_BLOCKED`). A WebSearch summary of that page's content
  states users "report opening the app to find that about a month's worth of data has been lost."
- (WebSearch synthesis only) One aggregator-review paraphrase: a user reported "all their data was
  suddenly lost, with only statistics remaining," and after reinstalling recovered some data but
  lost "three weeks of records." No verbatim review text or username was recoverable — this is a
  paraphrase from a search-engine summary of justuseapp.com, not a quote from the original review.

**Theme: Missing/limited brew-workflow detail (Beanconqueror) — 6 distinct mentions found (all open GitHub feature requests, directly fetched)**
- #1157 "Make it possible to show the values of the graph in detail view"
- #1156 "Make it possible to cut the graph"
- #1153 "Export baristamode brews also on junksizes and reimport them again"
- #1144 "feat: audio alerts for brewing"
- #1125 "feat: Espresso dial-in assistant" — a feature request for the app to actively help with
  dialing in, implying the current app is a passive logger rather than an active dial-in aid.
- (WebSearch synthesis only) A paraphrased complaint that the app "doesn't allow users to record
  weight and start/finish time of each pour for a given brew," which the reviewer called "the most
  important information for brewing consistently."

**Theme: Device/hardware integration gaps (Beanconqueror) — 3 distinct mentions found**
- GitHub #1136 "feat: add INKBIRD thermometers to supported device list" (directly fetched)
- GitHub #1127 "Save used profile when listening to a shot / meticulous" (directly fetched)
- (WebSearch synthesis only) A paraphrased complaint about scale pairing: "success with Decent scale
  but not with Skale."

**Theme: Cross-device sync (Beanconqueror) — 1 mention found**
- (WebSearch synthesis only) A paraphrased wish that "data would share between phone and iPad,"
  compared to how some cooking apps sync automatically.

**Theme: Doppio – Barista's Book — no individual review text recoverable; only aggregate rating splits**
No actual review text, quotes, or usernames were found for Doppio anywhere in this research — every
Doppio-related search returned only App Store/aggregator listing metadata. Two different third-party
aggregator snippets did surface numeric star-breakdowns, and they disagree with each other, which is
itself worth flagging:
- One aggregator: 95% 5-star / 2% 1-star (out of an unstated total count).
- A different aggregator: 74% 5-star / 12% 1-star (out of an unstated total count).
Neither snippet stated the total number of ratings behind these percentages, so absolute complaint
volume for Doppio could not be estimated — only that a non-trivial minority of raters (2–12%,
depending on source) gave it the lowest score, with no theme recoverable for why. A German-language
coffee forum thread specifically about this app was located (kaffee-netz.de) but its body was not
fetchable (`EGRESS_BLOCKED`); see forum signal below.

### Forum/reddit signal

Every `site:reddit.com r/espresso ...` query attempted (multiple phrasings: "is there an app that",
"app recommendation", "dial in tracking") returned **zero actual Reddit threads** — results were
entirely App Store listings and unrelated pages. Direct fetch of reddit.com was also refused
("Claude Code is unable to fetch from www.reddit.com"). **No Reddit/r-espresso threads were found in
this research; none are being cited or invented.**

Real (non-Apple, non-Reddit) forum threads that did surface, all snippet-only (bodies unreachable):

- https://www.home-barista.com/brewing/beanconqueror-data-loss-t95136.html — dedicated Home-Barista
  forum thread specifically about Beanconqueror losing user data. Directly relevant pain signal, but
  full thread text could not be fetched to extract verbatim quotes.
- https://www.kaffee-netz.de/threads/doppio-baristas-book.137421/ — German coffee-forum thread
  specifically discussing Doppio – Barista's Book. A WebSearch summary characterized the tone as
  broadly positive ("users can configure what they want to input and what they don't"), but the
  thread body could not be fetched to confirm or find any negative comments.
- http://www.coffeegeek.com/forums/espresso/general/530528?Page=1 — CoffeeGeek thread "Espresso Apps
  for phones?" from February 2011. Old and generic (asks what espresso apps exist at all); not a
  complaint about any specific current app, included for completeness only.
- https://www.home-barista.com/news/ios-app-for-hb-t51783.html — Home-Barista thread titled "IOS app
  for HB." On inspection via WebSearch summary this is about whether the *forum itself* should adopt
  a Tapatalk-style mobile browsing app, not about espresso-tracking/dial-in apps — tangential, not
  counted as niche-app demand signal.
- http://coffeegeek.com/forums/espresso/general/414952 — CoffeeGeek thread "Barista app for iPhone"
  from March 2009, asking about a specific (unrelated, generic) "Barista" iPhone app of that era —
  too old and off-target to be current signal, included for completeness only.

Net read: no current, on-target "people are actively begging for a better espresso app" reddit/forum
thread was located. The clearest actual demand/pain signal found in this phase is the Home-Barista
thread title about Beanconqueror data loss, plus Beanconqueror's own GitHub issue backlog — not
community-forum complaint threads about the space in general.

### Feature spec implied

Based only on the complaint themes actually found above (not aspirational feature-brainstorming):

- **Backup that survives infrequent use.** Beanconqueror's own filed issue (#284) shows its
  auto-backup routine purges older backups based on a fixed retention window, so a user who doesn't
  open the app for a while can lose everything on next launch — a new app should retain backups on a
  rolling basis regardless of how long since last open, and/or push backups to cloud storage rather
  than only local rotation.
- **Explicit data-loss recovery path, communicated in-app.** Multiple distinct sources (GitHub #355,
  the home-barista.com thread title, and the aggregator paraphrase) independently point at data loss
  as a recurring fear/event for Beanconqueror users — a new app should treat "never silently lose a
  logged shot" as a core reliability bar, not an afterthought.
- **True cross-device sync** (phone ↔ tablet ↔ web), not just per-device local storage — named
  directly as a wish in the Beanconqueror findings.
- **Pour-level granularity**, not just per-shot summary data: weight and start/finish timestamp for
  each individual pour within a brew, which one paraphrased complaint called the most important data
  for consistency and which Beanconqueror's own open feature requests (detailed graph values, ability
  to trim graphs) echo.
- **Active dial-in guidance, not just passive logging** — Beanconqueror's own community is requesting
  a "dial-in assistant" (#1125) as a feature that doesn't yet exist even in the most mature open-source
  app in the space; a new entrant differentiating on active recommendations rather than a manual log
  book would be addressing a gap incumbents themselves acknowledge.
- **Broader, named multi-brand hardware support** (Bluetooth scales beyond one or two named brands,
  smart thermometers, e.g. INKBIRD) called out explicitly as missing/wanted integrations.
- **Audio/attention cues during brewing** (requested directly, #1144) — a small but concrete UX gap
  in the incumbent most people would otherwise recommend as the default.

Caveat: this feature list is built almost entirely from one app's (Beanconqueror's) GitHub issue
backlog, because it was the only source in this environment that yielded verifiable, attributable
complaint text. Doppio — the second incumbent — yielded no usable complaint text at all in this
environment (only conflicting aggregate star-percentages), so none of the above should be read as
confirmed to apply to Doppio specifically, only to the open-source segment of this niche.
