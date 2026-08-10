# Phase 1 — Candidate Niches

12 candidates chosen for: (a) an existing, visible spend habit (gear purchases,
courses, certification fees, consumables), (b) a hobby/profession with physical
gear or a certification body, (c) plausibly buildable as an offline, single-user,
no-backend iOS app in <6 weeks. Excludes dating, crypto, health diagnosis, general
productivity per constraints.

Any specific numeric claim about market size below is marked "unverified" — these
are hypotheses to test in Phase 2/3/4, not conclusions.

1. **Fly fishing** — rods/reels/flies/waders spend, guided trips, fly-tying gear.
2. **Reef / saltwater aquarium keeping** — tanks, lighting, dosing, livestock; notoriously expensive hobby (unverified: "average tank spend").
3. **Home espresso brewing** — machines, grinders, bean subscriptions, scales.
4. **Amateur (ham) radio** — FCC-licensed hobby, radios/antennas, license exam fees.
5. **Scuba diving** — PADI/SSI certification fees, gear, logbooks, dive computers.
6. **Archery / bowhunting** — bows, arrows, broadheads, range fees, hunting licenses.
7. **Beekeeping** — hives, extraction equipment, local beekeeping association dues.
8. **Astrophotography** — telescopes, mounts, cameras, filters; high gear spend.
9. **Handloading / ammunition reloading** — presses, dies, powder, brass, components.
10. **Overlanding / off-road 4x4** — vehicle mods, recovery gear, trip planning.
11. **Vinyl record collecting** — turntables, cartridges, cleaning gear, records themselves.
12. **Sailing / cruising** — ASA/USCG certification courses, boat gear, charts.

Next: Phase 2 hits the iTunes Search API per niche. **Note:** this session's
network egress proxy blocks all `apple.com` domains (`itunes.apple.com` and
`apps.apple.com`), confirmed via direct curl (403 from proxy gateway) and
WebFetch (explicit `EGRESS_BLOCKED` error) on 2026-08-10. Per user direction,
Phase 2/3 proceed on a **best-effort basis via WebSearch** instead of the raw
API/RSS endpoints. WebSearch can surface real app names, developer names, and
App Store URLs, and sometimes rating/price figures embedded in search snippets
or indexed review sites — but none of this is verified against the primary
API response the task originally specified. Every figure that isn't from the
primary API is labeled **unverified** and the search evidence (query, source
URL) is cited so it can be checked manually.
