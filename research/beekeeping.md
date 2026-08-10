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

---

## Phase 3 — Pain Mining

> Methodology note: as in Phase 2, `itunes.apple.com` / `apps.apple.com` remained unreachable this
> session (`EGRESS_BLOCKED`, re-confirmed). This session's WebFetch tool was also attempted against
> several non-Apple domains that surfaced strong candidate content — `beekeepingforum.co.uk` (two
> different threads), `mwm.ai`, and `www.reddit.com` — and **all of them failed** (the
> `beekeepingforum.co.uk` and `mwm.ai` calls returned `EGRESS_BLOCKED` explicitly; the
> `reddit.com` call failed with a generic "unable to fetch" error). So, per the task instructions,
> everything below comes exclusively from WebSearch result snippets/AI-summaries — no page was
> read directly, and no review text below was invented; all quoted fragments are copied verbatim
> from what WebSearch's summarizer surfaced, attributed to the source URL it cited.

### Incumbents reviewed (and why)

Of the four candidates named for this phase (Apiarist, BeePlus, ApiNote, HiveHelp.AI), I ran
identical footprint-probing searches for all four before choosing. Results:

- **Apiarist – Beekeeper Assistant**: WebSearch's own summary reported a rating directly sourced
  from `apps.apple.com` (4.7★ / 134 ratings), plus a separate third-party aggregator figure (mwm.ai:
  4.6★, "1K+ downloads"). Multiple distinct complaint/praise threads surfaced across several query
  variants (crash-on-launch report, local-storage-only limitation, interface comparison to
  competitors).
- **BeePlus Beekeeping Manager**: Highest rating-count figure found for any app in this whole
  research (AppRecs.com: 4.7★ / **852 ratings**, "~1% 1-star"). Uniquely, it has **two dedicated
  discussion threads on a real beekeeping community forum** (beekeepingforum.co.uk), each of which
  WebSearch's summarizer was able to pull direct user quotes from, plus repeated independent
  complaint hits (sync issues, inventory, pollen records, photo-deletion behavior) across four
  separate query variants. This is the single richest complaint-and-praise footprint of any app
  found in Phase 2 or 3.
- **ApiNote (Apiary Book)**: Some real signal (3.5–3.83★, 110 Android ratings, one freeze/save-bug
  quote, one multi-user feature request) but consistently thinner than Apiarist or BeePlus, and one
  listing explicitly noted "not enough ratings or reviews to display an overview" — a low-volume
  signal.
- **HiveHelp.AI**: Produced the most *dramatic* complaints found (app abandonment, non-functional
  AI, unanswered support emails) but no confirmed rating-count figure surfaced anywhere, and one
  snippet suggests it may itself have too few ratings to display an aggregate — so despite juicy
  complaint content, its indexed volume looks lower than BeePlus or Apiarist.

**Chosen for deep-dive: Apiarist and BeePlus** — both had directly-sourced App Store rating+count
pairs (a proxy for real review volume) and both surfaced multiple independent complaint mentions
across different search phrasings, which is the strongest indicator of "actually indexed by search
engines" among the four candidates.

### Complaint themes

Only WebSearch snippets/summaries were available (no direct page reads succeeded), so the "quotes"
below are fragments WebSearch's own summarizer extracted and attributed to a source — treat them as
lower-confidence than a hand-verified quote, and note explicitly that in several cases only a
paraphrase (no exact fragment) was returned by the search summarizer.

**Apiarist — Beekeeper Assistant**

| Theme | # of distinct mentions found | Quote / paraphrase | Source |
|---|---|---|---|
| No cloud sync / local-only storage | 1 | Paraphrase only — data stored on-device, "inconvenient if you want to share information between different devices" (no verbatim fragment surfaced) | mwm.ai via WebSearch summary |
| Crash on launch (paid tier) | 1 | Paraphrase — "a user who paid for the pro version reported that the app crashes immediately and cannot be opened"; developer reportedly replied it worked fine on their end and shipped v1.18.1 | search snippet, no single named page cited |
| Interface/design feels dated vs. competitors | 1 | Paraphrase — "the interface isn't quite as slick as BeePlus or HiveBloom" | comparative listicle summary (source page not individually named) |

Total distinct complaint mentions found for Apiarist: **3**, all paraphrased — no exact quoted
review text (in quotation marks, attributed to a specific unnamed reviewer) survived into the
WebSearch summaries for this app.

**BeePlus Beekeeping Manager**

| Theme | # of distinct mentions found | Quote / paraphrase | Source |
|---|---|---|---|
| Cross-device sync doesn't work / is manual only | 3 | "I have not been able to synch between iOS devices" · "my only wish is that it would automatically sync between iPhone and iPad" · a third independent mention in a forum-thread summary that "some users tried BeePlus but experienced problematic syncing between devices" | beekeepingforum.co.uk threads (`beeplus-record-keeping-app.37127` incl. page 2, and `best-beekeeping-record-app-on-iphone.46332`) via WebSearch summary |
| Inventory/equipment-catalog feature is weak | 1 | "except for the inventory function" ... "it would be really nice for the application to have a stored database of common beekeeping equipment found in any of the supply company catalogs" | beekeepingforum.co.uk thread via WebSearch summary |
| Missing pollen-record tracking | 1 | "It has everything I need, except for pollen records. Please add this." | beekeepingforum.co.uk thread via WebSearch summary |
| iOS-only (no Android) | 1 | Paraphrase — "It is only available for iOS devices" cited as a downside | search snippet |
| Deleting a photo in the Photos app also deletes it from the hive record | 1 | Paraphrase — "if you delete photos from the photo app, they are also deleted from hive records," described as "a minor flaw" | search snippet |

Total distinct complaint mentions found for BeePlus: **7**, spanning 5 themes — of which 2 are
exact quoted fragments (sync-wish, pollen-records) and the rest paraphrased summaries.

Overall: no 1-star-specific review bodies (i.e. a full review text explicitly labeled "1 star")
were recoverable for either app — WebSearch could not surface individually-dated, star-rated
review text for either Apiarist or BeePlus, only forum-quote fragments and rating aggregates. This
should be stated plainly rather than treated as "no complaints exist."

**Other apps — complaint signal found opportunistically (not part of the chosen 2, noted for
context only):** HiveTracks (not in the Phase 2 list, but surfaced repeatedly in Phase 3 searches)
had by far the richest complaint set of any app touched in this research — crash-on-setup reports,
poor offline functionality "problematic since apiaries often have no cellular signal," and
subscription-cost pushback ("$50/year... hard to justify for someone with two backyard hives when
free tools exist") — flagged here only as a signal for the feature spec below, not scored into the
two-app comparison since it wasn't one of the four named candidates.

### Forum/reddit signal

No genuine `reddit.com` thread URLs were returned by any query variant tried, including
`site:reddit.com r/beekeeping is there an app that`, `site:reddit.com r/beekeeping app
recommendation`, `reddit beekeeping app recommendation hive tracking`, `reddit beekeeping "is
there an app" hive log`, and `"r/beekeeping" app recommendations iphone` — every one of these
returned `apps.apple.com` listings or third-party listicles instead of actual Reddit pages, and the
one direct `WebFetch` attempt against `www.reddit.com` failed outright. **Reddit signal: none
found** — stated plainly per instructions, not fabricated.

However, real, non-Reddit community-forum threads did surface with genuine URLs and were not
invented:

- https://beekeepingforum.co.uk/threads/beeplus-record-keeping-app.37127/ (and its page 2) —
  dedicated thread specifically about the BeePlus app; this is where the sync-complaint and
  inventory/pollen-feature-request quotes above came from.
- https://beekeepingforum.co.uk/threads/beekeeping-apps.44510/ — general "which app do you use"
  discussion thread.
- https://beekeepingforum.co.uk/threads/best-beekeeping-record-app-on-iphone.46332/ — iPhone-specific
  "what's the best record app" thread; mentions BeePlus's sync problems and several alternatives.
- https://beekeepingforum.co.uk/threads/iphone-ipad-apps-for-beekeeping.25556/ — another
  iOS-specific app-recommendation thread (title surfaced, content not independently pulled beyond
  the title in this session).
- https://www.beesource.com/threads/any-good-beekeeping-apps.309209/ — thread where the original
  poster asked for "a simple, easy to use app to keep notes and records on my hives" and reported
  the 3-4 apps they'd already tried "were too complicated or didnt make any sense the way they are
  laid out"; another user asked semi-rhetorically "what on earth do you need an APP for... How
  about a spiral-bound notebook?" (i.e. some of the audience is skeptical apps add value over paper
  at all); a third wanted "an app that can store pictures of frames for comparison over time, and
  also allow note entry by voice recognition."
- https://www.beesource.com/threads/what-are-the-useful-apps-for-beekeeping.367821/ — app-recommendation
  thread (title surfaced; content not independently pulled beyond title/aggregate summary).
- https://www.beesource.com/threads/using-apps-for-beekeeping.375714/ — app-recommendation thread
  (title surfaced only).
- https://www.beesource.com/threads/bee-apps.336496/ — app-recommendation thread (title surfaced
  only).
- https://www.beesource.com/threads/hive-management-app-for-android.366541/ — Android-specific
  app-recommendation thread (title surfaced only).

### Feature spec implied

Based on the complaint themes actually found above (not speculation beyond them):

- **Reliable, automatic multi-device sync must work out of the box.** This is the single most
  repeated complaint found (3 independent mentions for BeePlus alone) — any new app should default
  to real-time cloud sync between a user's own devices, not a manual/"tap Sync and choose an
  option" flow.
- **True offline-first operation.** Surfaced independently for HiveTracks ("useless in a remote
  apiary" without connectivity) and echoed in general listicle commentary about apps that "require
  constant internet access" — apiaries are frequently in low/no-signal locations, so local-first
  data entry with background sync (not sync-blocking data entry) is a baseline requirement, not a
  nice-to-have.
- **Don't silently couple hive-record photos to the system Photos library.** BeePlus's
  photo-deletion-cascade complaint suggests inspection photos should be stored independently
  (app-owned storage / copy-on-import), so a user cleaning up their camera roll doesn't
  accidentally destroy hive records.
- **Cover the specific record types beekeepers keep asking for and not finding**: pollen records
  (explicit BeePlus request), an actual equipment/inventory catalog tied to supply-company SKUs
  (explicit BeePlus request), and multi-user/shared-account access to one apiary's data (explicit
  ApiNote request, e.g. a beekeeping couple sharing one set of hives).
- **Price for the backyard/hobbyist majority, not the commercial operator.** The HiveTracks
  subscription-cost complaint ("$50/year... hard to justify for someone with two backyard hives")
  suggests a free or low-cost tier for small apiaries (the segment most forum posters describe
  themselves as) is important, with any premium tier reserved for larger/commercial functionality.
- **Keep the inspection-logging flow field-usable with gloves on.** Not a direct quoted complaint,
  but a repeated theme across the general listicle/blog commentary found ("ease of use in the field
  with gloves on" as a top stated priority) — large touch targets, minimal typing, and voice or
  photo-first note entry (explicitly requested in one Beesource thread) over dense text forms.
- **Don't assume an app is self-evidently worth it.** At least one forum voice pushed back on
  needing an app at all versus a paper notebook — onboarding/marketing should make the sync,
  reminder, and multi-apiary value proposition concrete rather than assuming beekeepers already
  want a digital tool.
- **Support responsiveness matters at small scale.** HiveHelp.AI's abandonment complaints (AI
  broken, support emails unanswered) suggest that for a niche this size, visible ongoing
  maintenance and responsive support may be a differentiator in itself, independent of feature set.
