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

## Phase 3 — Pain Mining

Research date: 2026-08-10. Method note: as in Phase 2, this environment's egress
proxy blocks all apple.com domains (confirmed EGRESS_BLOCKED again this pass),
so the App Store customer-reviews RSS feed and native review pages were never
reachable. WebFetch was additionally attempted against several *non*-Apple
domains that turned up in search results (longrangehunting.com, snipershide.com,
forum.nosler.com, complaintsboard.com, play.google.com, reddit.com) specifically
to try to pull full review/thread text — every one of them returned
EGRESS_BLOCKED (reddit.com returned a distinct "Claude Code is unable to fetch"
error rather than the proxy's EGRESS_BLOCKED message, but the practical effect
was the same: no content). **Everything below therefore comes only from
WebSearch result snippets** — short excerpts Google/Bing-style search surfaced
from App Store review pages, third-party review aggregators, and public forum
threads. Where a snippet appears to reproduce actual review text in quotation
marks, it is quoted verbatim and short (a few words); everything else is
paraphrased from the snippet's summary. No review text, usernames, or forum
threads were invented — where a query came back empty or generic, that is
stated plainly instead of being filled in.

### Incumbents reviewed (name which 2 apps and why)

1. **Hornady Reloading Guide** (id1451643677) — chosen per task instructions as
   the only app in the Phase 2 dataset with a high-volume, directly-confirmed
   rating (4.6/5, 13,384 ratings) and clear category-leader status.
2. **RCBS Reloading App** (id1559610918) — chosen over the other Phase 2
   candidates (My Armory, Reloading Assistant) because those two explicitly
   returned "not enough ratings or reviews to display an overview" in Phase 2
   and continued to surface almost no complaint-specific content in this pass's
   searches (My Armory searches returned only generic positive summary text and
   one feature request; Reloading Assistant searches mostly returned changelog
   "bug fixes" copy, not user complaints). RCBS, by contrast, is manufacturer
   (Bushnell/Vista Outdoor)-backed like Hornady, and searches surfaced a
   specific, repeated complaint pattern (see below) plus a distinct rating
   distribution snippet, meaning it had by far the most searchable review
   content of the remaining candidates.

### Complaint themes

**Hornady Reloading Guide**

1. **Pay-to-access / re-paying for content you already own — 4 distinct
   complaints found**
   - A user said the app is useless if they "can't pay for the load data"
     (payment/Subscribe button unresponsive).
   - A user who owns the 11th-edition printed book objected that they'd have to
     pay $20 more to get the same info in-app, calling it — per snippet — "a
     rip off."
   - A quoted snippet: **"It's a rip off to have to pay for something that
     doesn't work."**
   - A quoted snippet from a user who spent $28 on the app after an Apple
     password change locked them out: **"So now, I've spent $28 on this app
     and it's totally worthless. Big waste."**
   - Source: [Hornady Reloading Guide app reviews complaints — search
     summary](https://apps.apple.com/us/app/hornady-reloading-guide/id1451643677?see-all=reviews&platform=undefined)
     (aggregated from WebSearch snippets, page itself unreachable).

2. **App won't open / crashes on launch — at least 5 distinct complaint
   phrasings found**
   - "doesn't even open and just crashes" (tablets).
   - App won't open, shows a message to "try again later or contact support."
   - "The app no longer works and comes up with an error saying to try again or
     contact support."
   - "fails to open about 40% of the time unless you repeatedly try."
   - "a horrible habit of crashing all the time."
   - Source thread referenced in snippets: [Hornady Reloading Guide App Crash
     IOS? — Long Range Hunting
     Forum](https://www.longrangehunting.com/threads/hornady-reloading-guide-app-crash-ios.274548/)
     (thread content itself not directly fetchable — EGRESS_BLOCKED; summary is
     from the WebSearch snippet only, not the raw thread text).

3. **Purchased data disappearing / account resets — 2 distinct complaints
   found**
   - "previously purchased calibers disappearing with new updates."
   - A separate report that after an error/log-out cycle, "all of their
     purchased cartridges had been deleted" from the account.

4. **Garbled/broken data display — 1 complaint found**
   - iOS users reported trouble pulling up load data, with "garbled text
     appearing when selecting bullet weights."

5. **Brand lock-in (content limited to Hornady-brand components) — 1 mention
   found** (not a bug complaint, but a repeated limitation noted in summaries):
   the app's load data only covers Hornady-brand bullets/components.

Positive counter-signal found in the same searches (noted for balance, not a
complaint): multiple snippets mention Hornady customer service resolving
payment/access issues within "a couple of days" after users emailed support,
and one snippet says the app "finally works very well" after "many months."

**RCBS Reloading App**

1. **Forced reinstall / app breaks on repeat use — 1 specific complaint, but
   described as long-running ("years")**
   - Quoted snippet: **"Each time I want to load I delete the app and
     download again. This is an issue that's happened for years even though
     the reviews disappear with each update."**
   - Source: surfaced via
     [ComplaintsBoard — RCBS Reloading
     complaints](https://www.complaintsboard.com/rcbs-reloading-b132230) and
     repeated in general RCBS app-review search snippets (page itself
     unreachable — EGRESS_BLOCKED).

2. **Data sync / account-info loss — 2 distinct complaint phrasings found**
   - "constant issues with syncing data."
   - App "keeps erasing account info," requiring users to "uninstall and
     reinstall the app every time they want to use the scale" (i.e. to pair
     with RCBS's ChargeMaster/MatchMaster hardware).

3. **Crash on startup — 1 complaint found, noted as later fixed**
   - Snippet describes "app crashing on start up, though a new update was
     released that fixed this issue."

4. **Rating distribution is more polarized than the headline average
   suggests — 1 aggregator data point found**
   - One search snippet (not independently confirmed against the live App
     Store) broke down ratings as roughly 53% 5-star, 0% 4-star, 7% 3-star, 0%
     2-star, and 40% 1-star — i.e. a bimodal love-it/hate-it distribution
     rather than a smooth 4.7-average curve, even though a separate snippet
     also cited an overall "4.7 out of 5... over 1,000 ratings" figure. Both
     figures are aggregator-sourced and unverified against the live page; they
     are flagged here as an internal inconsistency worth confirming, not a
     settled fact.

**Reloading Assistant and My Armory — no usable complaint text found.**
Searches for both returned only changelog-style "bug fixes" copy (label
misalignment, decimal-key display issues, calculator crash-on-save — all
described as already fixed) and generic positive summaries ("easy to learn,"
"developers continue adding features"). Consistent with Phase 2's finding that
both apps had too few App Store ratings to display an aggregate score, this
pass found essentially no negative review text to mine for either app. Not
using either as an incumbent for this reason, per the task's own guidance.

### Forum/reddit signal

Site-restricted reddit searches (`site:reddit.com r/reloading is there an app
that`, `site:reddit.com r/reloading app recommendation load data`) returned
**no actual Reddit thread results** — every hit was an apps.apple.com listing
page that happened to rank for the keywords, not a Reddit discussion. This is
stated plainly per the task instructions rather than substituted with
plausible-sounding Reddit content. However, other gun/reloading forums (which
are reddit-adjacent, English-language hobbyist communities) surfaced real,
on-topic threads:

- [Best Option for Reloading Data App — Long Range Hunting
  Forum](https://www.longrangehunting.com/threads/best-option-for-reloading-data-app.341897/)
  — OP asks for a mobile app to keep reload data accessible without a computer
  or paper notebook; replies mention QuickLoad, the Hornady app, a
  cloud-hosted spreadsheet, Vihtavuori's app, and ReLOADeD (praised for
  storing recipes/inventory/rifles and printing recipes onto name-tag
  stickers) — i.e. no single reply names one app as sufficient on its own.

- [Recommendation for best iphone App for storing reloading data, rifle dope,
  shot log, etc? — Sniper's Hide
  Forum](https://www.snipershide.com/shooting/threads/recommendation-for-best-iphone-app-for-storing-reloading-data-rifle-dope-shot-log-etc.7089636/)
  — thread title itself is a direct feature-gap signal (wanting reload data +
  rifle dope + shot log combined in one app); replies scatter across GUNR,
  Load Data, Reloading Assistant, Gun Log SPC, "Reloading All Day," and
  FileMaker-based DIY databases — again no consensus single answer, and one
  reply notes FileMaker "does not run on Android."

- [Anyone else tired of bouncing between 3–5+ apps just to manage
  rifle/shooting data? — Rokslide
  Forum](https://rokslide.com/forums/threads/anyone-else-tired-of-bouncing-between-3-5-apps-just-to-manage-rifle-shooting-data.444811/)
  (and its [page
  2](https://rokslide.com/forums/threads/anyone-else-tired-of-bouncing-between-3-5-apps-just-to-manage-rifle-shooting-data.444811/page-2))
  — the single strongest pain signal found in this pass. OP frustration is
  explicitly about app fragmentation: bouncing between 1-2 ballistic-solver
  apps, a separate group-analysis app, a chrono-vendor app, a rangefinder app,
  Word docs for dope cards, and spreadsheets for gear/rifle info, with "none
  of it connects — it's all siloed in each individual app." Replies confirm
  the root cause (hardware-vendor lock-in: each device ties you to its own
  app) and note at least one competitor (GUNR) is explicitly marketing itself
  as the unified-solution answer to this exact complaint.

- [Software for Reloading Inventory — Rokslide
  Forum](https://rokslide.com/forums/threads/software-for-reloading-inventory.345581/)
  and [Software for reloading inventory — Long Range Hunting
  Forum](https://www.longrangehunting.com/threads/software-for-reloading-inventory.351515/)
  — both threads show reloaders improvising with Excel/Google Sheets or
  desktop tools (Gordon's Reloading Tool/GRT, GRtools.de) for inventory
  tracking rather than using a dedicated mobile inventory app, with one
  Google Sheets reply specifically valuing "saves to the cloud for access at
  the range" — i.e. cloud sync/access-anywhere is a value people are seeking
  outside the purpose-built apps.

- [Best reloading log app? — Nosler Reloading
  Forum](https://forum.nosler.com/threads/best-reloading-log-app.44103/) —
  surfaced by title match on "best reloading log app," confirming the
  question itself is a recurring, named thread topic across at least three
  separate forums (Nosler, Sniper's Hide, Long Range Hunting), though thread
  content could not be fetched directly (EGRESS_BLOCKED) so only the
  search-indexed title/topic is confirmed, not the replies.

- A general (non-reddit) query — "why is there no good app for reloading
  log" — returned a synthesized-from-snippets answer rather than one named
  thread, but the underlying theme it distilled is consistent with the
  Rokslide fragmentation thread above: "That integrated bench-to-range
  workflow is the gap no single app has fully closed... you look up data in
  one app, calculate trajectory in the other, and record results somewhere
  else entirely," plus a reliability worry that "specialist apps tend to come
  and go" causing data loss when small developers abandon apps. This is a
  paraphrase of a WebSearch-synthesized summary, not a quoted single source —
  flagged accordingly.

No genuine `reddit.com` thread URLs were recovered in this pass (WebFetch to
reddit.com failed outright, and site-restricted WebSearch queries returned
only Apple-appstore pages, not Reddit posts) — this is stated as a plain gap,
not filled with invented Reddit content.

### Feature spec implied

Based only on the complaint themes and forum signal actually found above:

- **Reliable offline-first data storage that survives app updates and
  reinstalls.** Both incumbents have named, repeated complaints about data
  vanishing (Hornady: purchased cartridges deleted after errors/updates; RCBS:
  "erasing account info," forced delete-and-reinstall cycles). A new app
  should treat local persistence + cloud backup as a core reliability
  requirement, not an afterthought.
- **No pay-to-re-access content a user already owns.** Hornady's most quoted
  complaints are specifically about re-paying for data already purchased in
  print or in a prior app edition ("rip off," "$28... totally worthless").
  A new entrant's monetization model should avoid this specific trap —
  e.g. one-time purchase or a subscription that's clearly communicated,
  not edition-gated re-purchases.
- **Launch reliability / crash-free startup.** Both incumbents show
  crash-on-launch complaints (Hornady: "fails to open about 40% of the time,"
  "crashing all the time"; RCBS: "crashing on start up"). This is a baseline
  quality bar incumbents are visibly missing, not a differentiator to build
  toward — it's table stakes to get right from day one.
- **Unify the fragmented workflow instead of adding another silo.** The
  strongest single piece of forum evidence (Rokslide's "bouncing between 3-5+
  apps" thread) says the real unmet need isn't another single-purpose load-data
  lookup app — it's one app that connects load-data reference, a personal
  reload/inventory log, rifle/firearm profiles, and range-session/chrono
  results, because today reloaders manually re-key the same information across
  4-5 separate apps and spreadsheets. GUNR is already explicitly positioning
  toward this; a new entrant should treat "unify bench-to-range workflow" as
  the core wedge, not a nice-to-have.
- **Don't be brand-locked.** A recurring soft complaint about Hornady's app is
  that its data only covers Hornady-brand components. Forum threads
  consistently value tools that span multiple powder/bullet manufacturers
  (Accurate, Alliant, Hodgdon, Vihtavuori, etc., as Reloading Assistant does)
  over single-manufacturer apps — a cross-brand data model is a real
  preference, not just a hypothesis.
- **True cross-platform + cloud sync, not device-vendor lock-in.** Multiple
  threads (Sniper's Hide, Rokslide, Long Range Hunting) show people falling
  back to Google Sheets/Excel specifically because it's accessible "at the
  range" from any device, and note that desktop tools like FileMaker "do not
  run on Android." A new app should assume users move between phone/tablet and
  want the same data everywhere, independent of which reloading-press or
  chrono hardware brand they own.

## Phase 4 — Distribution Channel Check

Research date: 2026-08-10. Method note: as in Phases 2-3, `reddit.com` and all
`apple.com` domains were unreachable this pass (WebFetch returned
EGRESS_BLOCKED or "unable to fetch" for both). This pass additionally attempted
WebFetch on every third-party subreddit-stats/analytics aggregator that
surfaced in search results — `subredditstats.com`, `gummysearch.com`,
`oneup.today`, `forums.feedspot.com`, `reloadyourgear.com`, `discord.com`,
`ar15.com`, and `web.archive.org` — every single one of these also returned
EGRESS_BLOCKED. **Every data point below therefore comes only from WebSearch
result snippets** (the search tool's own synthesized summary of what it found,
not a page Claude read directly), exactly as in Phases 2-3. Where a snippet
attributes a number to a specific aggregator or thread, that source is cited;
where no snippet surfaced a number at all, the channel is listed with "size
unverified" per the task instructions rather than estimated.

One important structural finding surfaced during this pass: **Reddit removed
public subscriber counts from subreddit pages in September 2025**, replacing
them with private "weekly visitors" / "weekly contributions" metrics that are
not exposed to search indexing. This is a plausible explanation for why no
current subscriber count for r/reloading, r/guns, or r/longrange could be
found through any search query or aggregator this pass — the underlying data
Reddit used to publish (and that third-party sites like subredditstats.com
scraped) is no longer public, not simply that the search tool failed. (Source:
[Reddit Swaps Subreddit Member Counts for Active
Users](https://currently.att.yahoo.com/att/reddit-swaps-subreddit-member-counts-171548334.html).)

### Channels found

| Name | Type | Size | Source | Self-promo policy |
|---|---|---|---|---|
| r/reloading | Subreddit | Size unverified — confirmed to exist and be the primary reloading subreddit (referenced repeatedly across Phases 2-3 sourcing and general search results), but no subscriber count could be found (see Reddit subscriber-count removal note above); every direct/aggregator lookup was blocked | Existence confirmed via repeated cross-references in search results; no single citable count-bearing URL found | **Unknown** — could not fetch the subreddit's rules/wiki page (EGRESS_BLOCKED) or find its specific self-promotion rule text in any search snippet, despite multiple targeted queries (`"r/reloading" rules self promotion`, `"r/reloading" "no self-promotion"`, etc.). Not confirmed either way. |
| r/guns | Subreddit | Size unverified for the same reason as above (historically one of the largest gun subreddits, but no current count found) | Existence + quarantine status confirmed via multiple search snippets, though the exact quarantine date/reason was not found | **Reduced reach regardless of rules**: confirmed **quarantined** by Reddit (requires a logged-in user to explicitly opt in to view it, and is excluded from normal browse/search surfacing) — quarantine status itself is a distribution-limiting fact independent of any self-promo rule. Rule text not found. |
| r/Firearms | Subreddit | **293k members** | [gummysearch.com/r/Firearms](https://gummysearch.com/r/Firearms/) (search-snippet only; page itself not independently fetchable — EGRESS_BLOCKED) | Unknown — not found |
| r/gun | Subreddit | **31k members** | [gummysearch.com/r/gun](https://gummysearch.com/r/gun/) (same snippet-only caveat) | Unknown — not found |
| r/longrange | Subreddit | Size unverified — confirmed real and topically on-point (precision-shooting/handloading-adjacent; referenced in feedspot's "Top Sniper Rifle Forums" list alongside Sniper's Hide) but no subscriber count surfaced in any query | Existence confirmed via [forums.feedspot.com/sniper_rifle_forums](https://forums.feedspot.com/sniper_rifle_forums/) listing snippet (page not independently fetchable) | Unknown — not found |
| Sniper's Hide Forum (snipershide.com) | Forum | **100,000 registered members** — but this figure is from a milestone-announcement thread dated **March 1, 2014**; no current 2026 count was found, so treat this as stale/floor, not current | [100,000 registered members, thanks to all who contribute — Sniper's Hide Forum](https://www.snipershide.com/shooting/threads/100-000-registered-members-thanks-to-all-who-contribute.207125/) | Unknown — not found. Note: this forum was already used as an incumbent-app source in Phase 3, where real users organically named and discussed specific commercial apps (GUNR, Load Data, Reloading Assistant) in a thread titled "Recommendation for best iphone App for storing reloading data..." — i.e. app-related discussion is clearly on-topic content there, though that is distinct from confirmed permission to post a launch announcement. |
| Long Range Hunting Forum (longrangehunting.com) | Forum | **"Over 70,000 registered members and 400,000 total unique visitors per month"** — figure's original source/date is unclear; it surfaced via search snippets tied to the forum's YouTube channel description, not a dated forum media-kit page | [LongRangeHunting — YouTube](https://www.youtube.com/c/LongRangeHunting/videos) (channel description, per search snippet; not independently confirmed by direct fetch) | Unknown — not found. Also used as a Phase 3 incumbent-complaint source (Hornady crash-report thread), confirming it's a real, active, on-topic community. |
| Rokslide Forum (rokslide.com) | Forum | **~40,000 registered users** — sourced to a Rokslide moderator's own comment comparing registered-user count to a YouTube channel's subscriber count, but that comment is dated **April 5, 2020**; treat as stale, not current | [Message Counts and Member Ranking — Rokslide Forum](https://rokslide.com/forums/threads/message-counts-and-member-ranking.117357/) (per search snippet) | Unknown — not found. This is the single strongest forum for on-topic pain signal in Phase 3 (the "bouncing between 3-5+ apps" fragmentation thread), and GUNR is reported to already market itself directly into that thread's audience — some form of commercial-app visibility is evidently tolerated there, at minimum via organic discussion. |
| Nosler Reloading Forum (forum.nosler.com) | Forum | Size unverified — real, active forum confirmed (categorized subforums and indexed member-profile pages found), but no total member count surfaced in any query | Existence confirmed via [forum.nosler.com](https://forum.nosler.com/) and its subforum/member-profile pages appearing directly in search results | Unknown — not found |
| "Reloading..." Discord server | Discord | Size unverified with two conflicting snippet-derived estimates: one search synthesis cited **21,437 members**, a second citing "a forum post from 2022" gave **21,730 members** — neither traces to a single fetchable, dated page (Discord itself and the AR15.com thread discussing it were both EGRESS_BLOCKED), so this is reported as an approximate ~21-22k range, not a confirmed figure | Invite referenced via [AR15.com — "Reloading discord server" thread](https://www.ar15.com/forums/armory/Reloading-discord-server/42-542687/) and a live invite link surfaced in search results (`discord.com/invite/VzdRbmdAjV`, not independently verified by fetch) | Unknown — not found. Functionally described in snippets as a primer/powder in-stock notification server, not a general discussion community, so it may not be a natural venue for an app-launch post regardless of rules. |
| Hornady Manufacturing (YouTube) | YouTube (competitor-owned) | **471,000 subscribers** | Multiple search snippets referencing [youtube.com/@hornady](https://www.youtube.com/@hornady) channel stats (not independently fetched) | N/A — this is a competitor's own branded channel, not an open community; not a viable channel for an unaffiliated app announcement. |
| Ultimate Reloader (YouTube) | YouTube (independent creator) | **408K subscribers** (current, per 2026 search result), with a documented milestone history (150,000 subscribers as of a dated Aug 14, 2020 blog post, and 100,000 as of Dec 1, 2019), which corroborates the channel is real, large, and has been steadily growing rather than a fabricated/inflated number | [150,000 Subscribers on YouTube — Ultimate Reloader](https://ultimatereloader.com/2020/08/14/150000-subscribers-on-youtube-boom-and-whats-next/); current 408K figure from 2026 search results (page not independently fetched) | Unknown — not a place to "post" as a stranger; would require pitching the creator directly for a sponsorship/review (standard influencer outreach), not a self-serve announcement channel. |
| NSSF — National Shooting Sports Foundation | Trade org | **"More than 8,000 members"** | [nssf.org/membership](https://www.nssf.org/membership/) (per search snippet) | N/A — explicitly a **B2B** trade association whose members are manufacturers, distributors, retailers, ranges, and sportsmen's organizations, not individual consumers/reloaders. Not a channel for reaching end users directly; listed for completeness only. |

**Additional structural finding — paid distribution is explicitly closed on
Reddit for this category.** Reddit's own advertising policy was found and
directly names this niche as prohibited: "Reddit prohibits advertisements for
weapons and related products... weapons and guns including accessories,
**ammunition**, and safety parts." (Source: [Reddit Advertising Policy:
Prohibited
Advertisements](https://advertising.reddithelp.com/en/categories/reddit-advertising-policy/reddit-advertising-policy-prohibited-advertisements),
per search snippet.) This means even a paid promoted-post route on Reddit —
the fallback if organic self-promotion turns out to be against subreddit
rules — is not available for an ammunition-reloading app; only organic,
unpaid community participation is possible on that platform.

### Verdict

**GO, but narrow and conditional — not the "post to r/reloading and get
10,000 downloads" plan a founder might hope for.**

What is genuinely specific and real, not vague:
- The niche's audience unambiguously congregates in a short, nameable list of
  real communities: r/reloading, r/guns (quarantined), r/Firearms (293k,
  sourced), r/gun (31k, sourced), r/longrange, Sniper's Hide (~100k as of
  2014), Long Range Hunting (~70k+ / 400k monthly visitors, snippet-sourced),
  Rokslide (~40k as of 2020), Nosler's forum, a ~21-22k-member Reloading
  Discord, and two large YouTube channels (Hornady's own 471k, and independent
  creator Ultimate Reloader's 408k). These are not hypothetical — three of
  them (Sniper's Hide, Long Range Hunting, Rokslide) are the exact same forums
  already used as primary sources in Phase 3, where real, named threads show
  people actively asking "what app should I use for reloading data" and
  other users organically naming specific commercial apps in reply. That is
  concrete, already-observed evidence that app-related discussion is welcome
  content in these communities, not just a theoretical audience count.

What is genuinely vague or unresolved, and keeps this from being an
unqualified GO:
- **No self-promotion rule text was confirmed for any single channel**,
  including the two most important ones (r/reloading, r/guns), despite
  numerous targeted queries — every reddit.com rules/wiki page and every
  third-party subreddit-rules database (oneup.today's self-promo checker,
  specifically) was EGRESS_BLOCKED. This is a real, stated gap per the task
  instructions, not filled with invented policy text.
- Most size numbers that do exist are **stale** (Sniper's Hide 2014, Rokslide
  2020) or **snippet-only** (Long Range Hunting, Discord), not confirmed
  current 2026 figures.
- r/guns being **quarantined** and Reddit's advertising policy **explicitly
  banning ammunition-related ads sitewide** are two confirmed, concrete
  negatives: the single highest-reach Reddit path is gated, and the paid
  fallback is closed by policy, not just unclear.

Net call: distribution is **specific enough to name a real go-to-market
plan** (organic participation in Rokslide/Sniper's Hide/Long Range
Hunting/Nosler's forum threads that already exist and already discuss
competing apps, plus the ~21-22k Reloading Discord, rather than a cold launch
post to r/reloading or any paid Reddit ad), but it is **not the kind of large,
low-friction, self-serve channel that would derisk distribution for a small
indie team with zero audience**. Two strangers can plausibly participate in
these forums over time and mention an app in an on-topic reply without being
banned (Phase 3 shows this pattern already happening for other apps), but a
cold announcement post to the biggest, most reach-efficient channel
(r/reloading) carries confirmed unknown risk, and the paid-ads shortcut is
confirmed closed. Proceed only if the team is willing to do slow, manual,
forum-native community participation rather than a single big launch post —
if the plan requires a fast, one-shot, high-reach announcement, this
distribution picture argues for **KILL**.
