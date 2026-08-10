# Scuba Diving — Phase 2 Demand + Competition

> Note on method: the iTunes Search API and the App Store customer-reviews RSS feed were unreachable from this
> environment (all `apple.com` domains are blocked at the network egress proxy — confirmed via curl/WebFetch,
> both returned `EGRESS_BLOCKED`). All data below comes from the `WebSearch` tool only — i.e. search-result
> snippets, cached page summaries, and third-party ASO/review-aggregator sites (AppGrooves, AppAdvice, Apptopia,
> etc.), not a live pull of the App Store page itself. Anything not explicitly stated in a search snippet is
> marked **unverified**.

## Search methodology (WebSearch queries run)

1. `scuba diving log app iphone app store`
2. `site:apps.apple.com scuba dive log`
3. `dive log app ios`
4. `scuba dive planner app ios`
5. `PADI app ios app store`
6. `"Scuba Dive Log by Zentacle" app store rating reviews price`
7. `"Breathe" "Smart Scuba Dive Log" app store rating reviews price`
8. `"Diving Log" app store TABATA rating reviews price iOS`
9. `DiveMate app store ios rating reviews price`
10. `Deepblu app store ios rating reviews price`
11. `"PADI" app store id1490797188 rating reviews price`
12. `"Dive Log" app id301049600 app store rating reviews price "More Mobile Software"`
13. `"Diving Log" app id1091064630 app store rating reviews price`
14. `Zentacle dive log app store rating stars number of ratings id1611242564`
15. `"DiveAtlas" scuba dive logbook app store rating reviews price id6760617577`

## Apps found

| # | App name | Developer | App Store URL | Price | Rating | Rating count | Last updated |
|---|----------|-----------|----------------|-------|--------|---------------|--------------|
| 1 | PADI | PADI Americas, Inc. | https://apps.apple.com/us/app/padi/id1490797188 | Free (in-app purchases for eCards) | **4.85 / 5** — directly sourced from search snippet | **~46,000 ratings** — directly sourced from search snippet | **v1.51.1, June 4, 2026** — directly sourced from search snippet |
| 2 | Scuba Dive Log by Zentacle | Zentacle, Inc | https://apps.apple.com/us/app/scuba-dive-log-by-zentacle/id1611242564 | unverified — pricing not stated in any snippet; app copy claims "20k active users" (usage, not rating) | unverified — not found (searched twice, no star figure surfaced) | unverified — not found | unverified — not found |
| 3 | Breathe – Smart Scuba Dive Log | EPIC APPS UK | https://apps.apple.com/us/app/breathe-smart-scuba-dive-log/id1351691642 | Free with in-app purchase (Pro subscription tier); exact price unverified | 5 / 5 per WebSearch summary, but this appears to be a mis-read of a small sample — third-party aggregator AppGrooves lists the app with **106 reviews** total (across platforms, not confirmed App-Store-only) | ~106 (AppGrooves, not confirmed as App Store native count) — source: https://appgrooves.com/ios/1351691642/breathe-smart-scuba-dive-log/epic-apps-uk | unverified — not found |
| 4 | Dive Log | Greg Mclaughlin / More Mobile Software | https://apps.apple.com/us/app/dive-log/id301049600 | unverified — one snippet referenced "$14.99 with in-app purchases" but the search engine itself flagged this may belong to a different "Dive Log"-named app, so treat as unconfirmed | unverified — not found | unverified — not found | unverified — not found |
| 5 | Diving Log (TUSA Diving LOG) | TABATA CO., LTD | https://apps.apple.com/us/app/diving-log/id1091064630 | Free per one summary — unverified against a primary snippet | unverified — not found | unverified — not found | "Requires iOS 18.0 or later" noted in one snippet, but no update date found — unverified |
| 6 | DiveMate – The Diving Logbook | AppZoo GmbH (ConfiTek) | https://apps.apple.com/iq/app/divemate/id567172778 (an alternate listing under id902359157 also appeared in results — possible duplicate/legacy App Store ID, unverified which is canonical) | Free to download with in-app purchases (backup/restore to Dropbox/iCloud, etc.) — per search summary | Conflicting figures across sources: AppGrooves aggregator cites **3.6 / 5** and **3,675 reviews** (possibly aggregated across Android+iOS, not confirmed App-Store-only); a separate mention says the official Apple App Store page "has not received enough ratings or reviews to display an overview." Treat rating as **unverified / conflicting**. | Conflicting — see above (AppGrooves: ~3,675; Apple listing itself: below display threshold) — sources: https://appgrooves.com/app/divemate-the-diving-logbook-by-appzoo-gmbh/negative | unverified — not found |
| 7 | Scuba Dive Logbook – DiveAtlas | unverified (developer name not stated in any snippet) | https://apps.apple.com/au/app/scuba-dive-logbook-diveatlas/id6760617577 | unverified — not found | "hasn't received enough ratings or reviews to display an overview" — i.e. confirmed **too new/low-volume to have a public rating** | Below Apple's display threshold (implies low count, exact number unverified) | unverified — not found, but feature list (CSV/UDDF export, No-Fly Timer, Gear Service) suggests an actively developed, recent app |
| 8 | Ez Dive Planner | New Vision Promotions LLC | https://apps.apple.com/us/app/ez-dive-planner/id537810707 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |
| 9 | ScubaPlan: Diving Community App | unverified (developer not stated) | https://apps.apple.com/us/app/scuba-diving-plan/id6689517716 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |
| 10 | Diveplanner Tec & Rec | unverified (developer not stated) | https://apps.apple.com/us/app/diveplanner-tec-rec/id1506985833 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |

Additional apps that surfaced in results but were not carried into the table above (to stay at 10 distinct
entries): **Deepblu** (social dive-log app, free, App Store ID not confidently resolved — one candidate
`id6479249855` labeled "DeepBlue Mobile" may be an unrelated/rebranded app, so it was excluded rather than
mismatched), **PADI Trainer Pro** (`id6742450911`), **PADI Training** (`id1471474067`), **PADI Adventures: book
diving** (`id1497105546`), **DiveLogManager** (`id404897036`, Mac-linked companion app), **Diving
logbook-Dive Number** (`id949480835`), **EANx** (`id6505006854`), **DiverLog+** (`id1294460120`).

## Opportunity flags

- **Top apps average <4.0 stars with >200 ratings** — **False / Unclear.** The only app in this research with a
  confirmed rating *and* a confirmed large rating count is PADI itself, at 4.85★ / ~46k ratings — well above the
  4.0 threshold. No other app in the list has both a confirmed star rating and a confirmed rating count over 200
  (Zentacle, Dive Log, Diving Log, DiveAtlas, Ez Dive Planner, ScubaPlan, and Diveplanner Tec & Rec all came back
  with no verifiable rating data at all; DiveMate's numbers are conflicting/unverified; Breathe's ~106-review
  figure is below the 200 threshold anyway). So the flag reads **False** for the one app we can verify, and
  **unclear/not evaluable** for the rest — we cannot confirm any top app is a <4.0-star, >200-rating app.

- **Top apps not updated in >18 months** — **Unclear.** Only one confirmed last-update date exists in this
  dataset: PADI, updated June 4, 2026 (very recent, well under 18 months). No update dates could be confirmed
  for any of the other 9 apps via WebSearch snippets, so this flag cannot be verified either way for most of the
  category. What we *can* say: DiveAtlas's feature description (recent-sounding features like UDDF export,
  Gear Service, No-Fly Timer) and its "not enough ratings yet" status both suggest a recently launched/updated
  app, and several of the smaller dive-log/planner apps (Ez Dive Planner, Diveplanner Tec & Rec, ScubaPlan) look
  like small-developer, low-visibility apps where staleness is plausible but unconfirmed.

- **Top 3 results are all free/ad-supported with no paid alternative** — **False, with caveats.** Based on
  confirmed/likely pricing info: PADI is free (with paid eCard add-ons), Breathe is free-with-IAP/subscription,
  DiveMate is free-with-IAP. So the most prominent 2-3 results skew free/freemium rather than pure paid apps —
  but at least one listing (Dive Log, id301049600) was associated in one snippet with a **$14.99** price point,
  though the search engine itself flagged that this figure may not belong to this specific app, so it's marked
  unverified rather than counted as confirmation of a paid alternative. Net: the pattern looks
  free/freemium-dominated, which is directionally consistent with this flag being **true in spirit** for the
  logging-app subcategory, but strict verification of "no paid alternative exists" was not possible — call it
  **unclear-leaning-true**.

- **Fewer than 5 results that genuinely match the keyword (i.e. the niche is underserved)** — **False.** This
  is the one flag with strong, repeated evidence: WebSearch queries returned well over 10 distinct, real,
  actively-listed apps that directly match "dive log," "dive planner," or "PADI/certification" intents —
  general dive logbooks (Dive Log, Diving Log, DiveMate, Zentacle, DiveAtlas, Deepblu, Diving logbook-Dive
  Number, DiverLog+), dedicated planners (Ez Dive Planner, Diveplanner Tec & Rec, EANx, V-Planner, iDeco Pro),
  a community/social app (ScubaPlan, Deepblu), and PADI's own suite of four separate apps (PADI, PADI Training,
  PADI Trainer Pro, PADI Adventures). The niche is **not underserved** — it is a small but clearly
  established, multi-competitor category with at least one dominant, high-rated incumbent (PADI) plus a long
  tail of smaller logbook/planner apps.

## Overall assessment

This niche looks **crowded, not underserved** — there are 10+ real, distinct, currently-listed iOS apps
covering dive logging, dive planning, and certification/training, and the dominant player (PADI, the official
certifying body's own app) is free, very actively maintained (updated within the last two months of this
research date), and extremely well rated (4.85★ on ~46k ratings) — a very high bar for a new entrant to unseat
on trust and distribution alone. Confidence in this conclusion is **moderate-high for the "crowded / not
underserved" call** (that flag rests on a large, repeated, consistent set of search hits) but **low for any
specific competitor's rating, price, or update-recency numbers** beyond PADI itself, since the iTunes Search API
and App Store RSS feed were unreachable and most other apps' star ratings, rating counts, and update dates
could not be confirmed through WebSearch snippets alone — a live App Store pull would be needed before treating
any of the "unverified" cells above as settled.
