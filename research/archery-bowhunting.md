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

---

# Phase 3 — Pain Mining

Research date: 2026-08-10. Method note: this environment's egress proxy blocks
all apple.com domains (confirmed EGRESS_BLOCKED again on itunes.apple.com and
apps.apple.com), so the App Store customer-reviews RSS feed was not reachable.
WebFetch was also tried on non-Apple domains that came up in search results —
www.bbb.org and www.archerytalk.com both returned EGRESS_BLOCKED as well, so
this environment's proxy is blocking those hosts too, not just Apple's. As a
result, **everything below was gathered from WebSearch result snippets only** —
no page was directly fetched and read in full. Any "quote" below is a short
phrase (a few words) that appeared verbatim inside a WebSearch snippet, not
something pulled from a live review page; the snippet's summarizing model may
have lightly paraphrased around those phrases. Treat exact wording as
indicative, not a certified verbatim transcript, and treat all counts as
"at least N distinct complaints referenced across snippets," not exhaustive
tallies from reading every review.

## Incumbents reviewed

1. **AccuBow** (AccuBow / AccuBow 2025, id1448656716) — chosen per task
   instructions as incumbent #1: the weakest confirmed iOS rating in the Phase 2
   set (3.70/5, 890 ratings) with real volume, meaning there's more indexed
   review text to mine than the "not enough ratings" apps.
2. **Bow Shop Bible** (Lifetime id1492396052 / Subscription id1584051239) —
   chosen as incumbent #2 over CapTarget Archery and PRO Archery Ballistics
   because it was the only other Phase 2 app with real, independent third-party
   discussion threads showing up in search results (multiple dedicated Archery
   Talk forum threads about the app specifically). CapTarget Archery's search
   results were almost uniformly positive/marketing-flavored (5.0/5, "most
   professional archery app") with only vague, minor gripes and no dedicated
   forum threads found; PRO Archery Ballistics returned essentially no
   complaint content at all ("did not reveal significant complaints").

## Complaint themes

### AccuBow

**1. Paywall/subscription retrofit — at least 4 distinct complaints referenced**
Users say the app or its game modes used to be free and were later put behind a
subscription. Quoted phrases surfaced in snippets: *"only reason I gave 1 star
is cause I can't review for 0"*, and a user who said they were *"not giving
yall $8 every 3 months when I paid $150 for the bow."* Another complaint
(BBB-sourced snippet) said the app "was free when it first came out" and then
"suddenly required a subscription," calling it unhelpful to the archery
community. A packaging-vs-reality complaint also appeared: the box/packaging
said the app and games were free to play, but an update added a paywall.
Sources: [AccuBow BBB complaints](https://www.bbb.org/us/il/peru/profile/exercise-equipment-repair/accubow-0654-90016243/complaints), [AccuBow App Store reviews](https://apps.apple.com/us/app/1448656716?see-all=reviews&platform=iphone), [AccuBow 2025 App Store](https://apps.apple.com/us/app/accubow-2025/id1448656716)

**2. Login / account-creation failures — at least 2 distinct complaints referenced**
Reviewers describe being unable to create a login at all: a manual
account-creation flow whose "loading wheel" spins for "2-4 minutes" and then
errors out, and separately that the app "doesn't respond when trying to log in
with the iCloud option." Some reviewers explicitly blame the developer rather
than their own internet connection.
Sources: [AccuBow App Store reviews](https://apps.apple.com/us/app/1448656716?see-all=reviews&platform=iphone), [AccuBow BBB complaints](https://www.bbb.org/us/il/peru/profile/archery-equipment/accubow-0654-90016243/complaints)

**3. App crashes / won't open — at least 3 distinct complaints referenced**
Separate from login issues: users report the app "won't load and just keeps
closing out," or not loading fully before "kicking them out." One complaint
pattern described in a snippet: when a user tries to cancel out of a
subscription prompt, "the app errors out and won't open." Reviewers also say
customer support told them they "have to subscribe" to get it working, and that
the company "will not answer phone calls and has quit responding to emails."
Source: [AccuBow crash/complaint search results — BBB, Facebook, Google Play, App Store]

**4. Unreliable/random arrow-fire mechanic — at least 2 distinct complaints referenced**
One reviewer: *"half the time the arrow doesn't fire,"* estimating *"1 out of
every 10 shots actually fires."* A second, separate complaint says "the app
shoots the arrow on its own randomly every time you try to use it," even after
adjusting settings — i.e. the opposite failure mode (misfires that shouldn't
happen) from the same core mechanic.
Source: [AccuBow 1-star review search results](https://apps.apple.com/us/app/1448656716?see-all=reviews&platform=iphone)

**5. Hardware quality / feel — at least 2 distinct complaints referenced (hardware, not app, but drives app 1-star ratings since they share a listing)**
*"Bow started to fall apart right out of the box."* Another called it a
"garbage product" by a "garbage company," saying "It feels like an explosion on
every shot. It is so loud and uncomfortable to shoot" and warning "If you have
shot a quality bow, you'll hate this thing."
Source: [AccuBow 1-star review search results](https://apps.apple.com/us/app/1448656716?see-all=reviews&platform=iphone)

Note on rating consistency: different searches returned different aggregate
AccuBow figures — 3.70/5 on 890 ratings (Phase 2, and repeated in one Phase 3
search), 3.8/5 on "1,000 ratings" in another, and 2.80/5 on "950 ratings" in a
third. These are WebSearch-summarized snippets of what are likely different
cached/aggregator snapshots (or possibly the separate "AccuBow" vs "AccuBow
2025" listing IDs), not a single confirmed live figure — flagging as an
unresolved discrepancy rather than picking one.

### Bow Shop Bible

Far less negative content surfaced than for AccuBow. No true 1-2-star review
text was found — only a small number of mixed/lukewarm comments inside
otherwise positive threads and listings.

**1. Subscription price objections — at least 2 distinct complaints referenced**
A Google Play-sourced snippet quoted a review saying the subscription is *"not
worth the subscription price."* Separately, an Archery Talk forum
participant reportedly said they passed on the app because of the cost /
felt the subscription fee was too high (paraphrase — no direct quote surfaced
in the snippet). One other forum participant dismissed the negative comments as
"probably trolls," suggesting the complaint volume there is genuinely low, not
just under-indexed.
Sources: [Bow Shop Bible Subscription — Google Play](https://play.google.com/store/apps/details?id=com.stsportsllc.BowShopBiblePro&hl=en_US), [Anyone use Bow Shop Bible App — Archery Talk](https://www.archerytalk.com/threads/anyone-use-bow-shop-bible-app.5981946/)

**2. Minor UX gripes — 1 complaint referenced, low confidence**
A snippet mentioned "content seems to be organized in odd places" as a
secondary note inside an otherwise positive review; not corroborated elsewhere.

**Explicit gap:** unlike AccuBow, no actual quoted 1-star/2-star review text for
Bow Shop Bible was found via WebSearch — the only aggregate figures found (4.8/5
on 17 Google Play reviews for the Lifetime version, 4.5/5 on 11 reviews for the
Subscription version) are counts too small to be meaningful, and the qualitative
tone across every source was net-positive. This should be read as "insufficient
mined complaint volume to call a pattern," not as "the app has no problems."

## Forum/reddit signal

Every direct `site:reddit.com` query (`site:reddit.com archery is there an app
that`, `site:reddit.com r/bowhunting app recommendation`, and follow-up
variants like `reddit.com/r/bowhunting "app" frustrating`, `reddit AccuBow app
worth it`, `reddit archery app subscription scam`, `reddit.com r/Archery sight
tape app recommendation`) came up **empty of actual Reddit threads** — results
were apps.apple.com listings, Wikipedia, Steam, or unrelated pages. Stating
this plainly per instructions: **no Reddit threads were found or read**; nothing
below is sourced from Reddit despite the queries the task suggested.

What did surface, from non-Reddit forums (Archery Talk, Archery Interchange,
Rokslide), via WebSearch snippets only (none of these pages were fetched
directly — archerytalk.com WebFetch returned EGRESS_BLOCKED):

- [Anyone use Bow Shop Bible App | Archery Talk Forum](https://www.archerytalk.com/threads/anyone-use-bow-shop-bible-app.5981946/) — thread of archers asking about/discussing the Bow Shop Bible app; snippet content is net-positive with a cost objection.
- [Bow Shop Bible App | Archery Talk Forum](https://www.archerytalk.com/threads/bow-shop-bible-app.5819897/) — earlier thread on the same app, general discussion.
- [Bow Shop Bible Pro is finally available | Archery Talk Forum](https://www.archerytalk.com/threads/bow-shop-bible-pro-is-finally-available.6068092/) — announcement/discussion thread for the Pro tier.
- [Hunting App. Recommendations | Archery Talk Forum](https://www.archerytalk.com/threads/hunting-app-recommendations.6198287/) — archers actively asking the community which hunting app to use, i.e. direct "is there an app that..." demand signal.
- [Best Hunting App? | Archery Talk Forum](https://www.archerytalk.com/threads/best-hunting-app.6122798/) — same kind of ask-the-community app-recommendation thread.
- [Good Archery APP's? | Archery Talk Forum](https://www.archerytalk.com/threads/good-archery-apps.2445915/) — general "what apps do people use" thread, a recurring topic on the forum.
- [Best archery Apps for IOS | Archery Talk Forum](https://www.archerytalk.com/threads/best-archery-apps-for-ios.4781793/) — iOS-specific version of the same recurring ask.
- [Archery Apps. for the phone | Archery Talk Forum](https://www.archerytalk.com/threads/archery-apps-for-the-phone.5838135/) — another recurring "what apps exist" thread.
- [Best Sight Tape Software | Archery Talk Forum](https://www.archerytalk.com/threads/best-sight-tape-software.5310575/) — archers comparing sight-tape tools/apps (Archers Advantage, TAPes, etc.), i.e. demand for this specific utility.
- [Sight tape software? | Rokslide Forum](https://rokslide.com/forums/threads/sight-tape-software.256650/) — same ask on a different hunting forum, corroborating the sight-tape-tool demand signal.
- [ArcherzUpshot app??? | Archery Talk Forum](https://www.archerytalk.com/vb/showthread.php?t=4805345) and [Anyone know what has happened to ArcherZUpshot App? | Archery Talk Forum](https://www.archerytalk.com/threads/anyone-know-what-has-happened-to-archerzupshot-app.4234889/) and [ArcherZupshot iOS, "hacks" to keep it running? | Archery Talk Forum](https://www.archerytalk.com/threads/archerzupshot-ios-hacks-to-keep-it-running.5352687/) and [ArcherzUpshot is dead! What else is good | Archery Interchange](https://www.archeryinterchange.com/threads/archerzupshot-is-dead-what-else-is-good.242285/) — a cluster of threads across two forums about a popular archery scoring app (ArcherZupshot, by Missing Marble LLC) that was abandoned by its developer: it stopped working after OS updates, users lost paid "Pro" features because the license-check servers went down, and the community had to hunt for workarounds/alternatives (Target Tracker, XringScoring, rcherz.com). This is real, multi-thread evidence of pain caused by an archery app being discontinued/unmaintained, distinct from AccuBow/Bow Shop Bible specifically.

## Feature spec implied

- **No forced paywall retrofit on previously-free core features.** AccuBow's
  single loudest complaint cluster is "it used to be free, now it isn't" — any
  free tier offered at launch should stay free, or the pricing model should be
  transparent and stable from day one rather than changed after users are
  invested.
- **Rock-solid account creation / sign-in, including a no-login or offline-first
  path.** Multiple AccuBow complaints are about being unable to even create an
  account (spinning loaders, broken iCloud sign-in) — before a user ever
  reaches the app's actual features. A new app should let a user get to core
  functionality with minimal or zero mandatory account friction.
- **Crash/stability bar above what AccuBow apparently clears**, especially
  around subscription/paywall prompts specifically (the reported "cancel the
  subscription prompt and the app errors out" pattern) — paywall UI should be
  the most-tested path, not the least.
- **Responsive, human customer support**, since multiple complaints (BBB and
  App Store snippets) describe support as unreachable by phone/email once a
  user has a problem — even a lightweight in-app support/contact channel would
  differentiate from this pattern.
- **Long-term maintenance commitment / no risk of abandonment.** The
  ArcherZupshot thread cluster shows this community has been burned before by a
  well-liked app going dark and taking paid "Pro" purchases down with it
  (server-gated license checks). A new app should avoid server-gating paid
  features in a way that bricks them if the company stops operating, and should
  signal an ongoing update cadence.
- **Demand clearly exists for a recommendation-worthy, actively-discussed
  sight-tape / bow-tuning / hunting-log utility** — the recurring "what apps do
  people use" and "best hunting app?" threads on Archery Talk indicate the
  community does not have a single obvious go-to and keeps re-asking, which is
  itself a mild opportunity signal (not a complaint about a specific app, but a
  sign no incumbent has won mindshare enough to stop the question from
  recurring).
- **Caveat on this whole spec:** it rests on WebSearch snippets for one
  weak-rated app (AccuBow) plus one much-better-regarded app (Bow Shop Bible)
  with almost no mined negative content, plus forum-thread titles/snippets, not
  full-text reviews. Before committing to build, a follow-up pass with actual
  App Store RSS/API access (from an unblocked network) is needed to read full
  review text and confirm complaint frequency at scale.
