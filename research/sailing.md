# Sailing / Cruising — Phase 2 Demand + Competition

**Research date:** 2026-08-10
**Method note:** This session's egress proxy blocks all apple.com domains, so the iTunes Search API and the App Store customer-reviews RSS feed were unreachable (confirmed via curl and WebFetch — both returned EGRESS_BLOCKED). All data below was gathered via the WebSearch tool only, which surfaces Apple App Store URLs and third-party aggregator snippets (AppFollow, JustUseApp, AppBrain, MWM, casualnavigation.com, etc.) rather than live App Store page data. Every figure is attributed to the query/source that produced it and marked "unverified" where no source gave a hard number.

## Search methodology (queries run)

1. `sailing app iphone app store`
2. `site:apps.apple.com sailing`
3. `marine navigation app ios app store`
4. `sailing logbook app ios`
5. `ASA sailing certification app ios`
6. `iNavX marine navigation app store rating reviews price`
7. `SeaNav app store rating reviews price subscription`
8. `SailFlow app store rating reviews price`
9. `Navionics Boating app store rating reviews price ios`
10. `PredictWind app store ios rating reviews price`
11. `Sail Racer app store rating reviews last updated`
12. `SailTies logbook app store rating reviews price`
13. `"Marine Navigation" app id528948720 rating reviews last updated version`

## Apps found

All entries below have a real, working `apps.apple.com` URL returned directly by WebSearch. Fields not confirmed by a specific source snippet are marked "unverified."

| # | App name | Developer / seller | App Store URL | Price | Rating | Rating count | Last updated |
|---|----------|--------------------|--------------------|-------|--------|---------------|---------------|
| 1 | iNavX: Marine Navigation | iNavX / Rite-Size (per aggregator pages; developer name unverified from a first-party source) | https://apps.apple.com/us/app/inavx-marine-navigation/id286616280 | $4.99 one-time + chart subscriptions $9.99–$199.99/yr (per casualnavigation.com / aggregator snippets) | 4.76–4.8 / 5 (two different sources gave 4.76 and 4.8; treated as consistent, high) | 19.4K (per justuseapp.com aggregator, not first-party) | unverified — not found |
| 2 | SeaNav (US) | SeaNav Ltd (per app description text, not independently confirmed) | https://apps.apple.com/us/app/seanav-us/id632635827 | Free app; chart subscription $9.99/yr (per casualnavigation.com) | unverified — not found | unverified — not found | unverified — not found |
| 3 | SailFlow: Sailing Forecasts | WeatherFlow (per appgrooves.com listing "SailFlow by WeatherFlow") | https://apps.apple.com/us/app/sailflow-sailing-forecasts/id555309964 | Free + tiers: Plus $3.99/mo or $44.99/yr, Pro $9.99/mo or $119.99/yr, Gold $14.99/mo or $179.99/yr (per appfollow.io / justuseapp.com) | 4.7 / 5 (per appfollow.io) | unverified — not found (appgrooves.com mentions "2,462 reviews" but that figure's platform/scope is unclear, so not trusted as an App Store count) | unverified — not found |
| 4 | Navionics® Boating | Navionics (self-named in listing) | https://apps.apple.com/us/app/navionics-boating/id744920098 | Free with 2-week Navionics+ trial, then $9.99/yr subscription (per appbrain.com/yachtingworld.com snippets) | 2.9 / 5 | 2.3K ratings | unverified — not found |
| 5 | PredictWind — Marine Forecasts | PredictWind Limited (per amazon.com listing "PredictWind Limited") | https://apps.apple.com/us/app/predictwind-marine-forecasts/id477048487 | Free download; paid Standard/Professional plans ~$190–$330/yr (per moneyformangos.com review) | 4.80 / 5 | 32.1K reviews | unverified — not found (requires iOS 15.5+, per aggregator) |
| 6 | ASA's Sailing Challenge | American Sailing Association (ASA) | https://apps.apple.com/us/app/asas-sailing-challenge/id1109489005 | $3.99 with in-app purchases | 4.8 / 5 | 2.8K ratings | unverified — not found (requires iOS 11.0+) |
| 7 | Sail Racer | Sailracer.net (inferred from Google Play package name `sailracer.net`; not confirmed for iOS listing) | https://apps.apple.com/us/app/sail-racer/id473901816 | unverified — not found | unverified — not found (Aptoide, a non-App-Store source, showed 5-star, not usable as App Store rating) | unverified — not found | unverified — user complaints in reviews reportedly say "not updated in 7 years"; no confirmed date found. Treat as anecdotal, not verified. |
| 8 | SailTies: Logbook & Sailing CV | SailTies (self-named in listing) | https://apps.apple.com/gb/app/sailties-logbook-sailing-cv/id1507376381 | Free (per appbrain.com) | 4.95 / 5 (iOS, per appbrain.com aggregator) | 150 ratings (iOS, per appbrain.com aggregator) — below the 200-rating threshold used in flag #1 below | unverified — not found |
| 9 | Marine Navigation | Marco Palaferri (per app description snippet: "Since 2009...") | https://apps.apple.com/us/app/marine-navigation/id528948720 | One-time purchase full version, or PRO subscription option (exact price unverified — not found) | 2.9 / 5 | 2,000+ reviews (approximate, per aggregator snippet) | unverified — not found |
| 10 | i-Boating: Marine Charts & GPS | unverified — not found | https://apps.apple.com/us/app/i-boating-marine-charts-gps/id994992062 | unverified — not found | unverified — not found | unverified — not found | unverified — not found |

Other real apps that surfaced in search but were not deep-dived (URL confirmed, all other fields unverified): Vantage Sailing (`id6544807723`), Sail Routing (`id6756657427`), KWINDOO Tracking for sailing (`id974955770`), SailSim – Sailing Simulator (`id6464166885`), Go Sailing (`id622198686`), 2Sail Sailing Simulator (`id1536527598`), Sailing World Tour Adventures (`id6618158512`), Argo Navigation: Boat GPS, Map (`id1463869636`), Boating Logbook: Skipper (`id671764434`), Ship's Log Book for Captains (`id533244045`), LogBook — Digital Yacht Log (`id6762569859`), Saillogger (web app with dedicated iOS app, per saillogger.com — App Store URL not directly surfaced).

## Opportunity flags

- **Top apps average <4.0 stars with >200 ratings: MIXED / UNCLEAR (leans False for the category leaders).**
  The two highest-visibility apps with large, confirmed rating counts are strong: PredictWind (4.80/5, 32.1K ratings) and iNavX (4.76–4.8/5, ~19.4K ratings, aggregator-sourced). ASA's Sailing Challenge (4.8/5, 2.8K ratings) and SailFlow (4.7/5, count unverified) are also well above 4.0. However, two general marine-navigation apps that surfaced prominently — Navionics® Boating (2.9/5, 2.3K ratings) and Marine Navigation (2.9/5, ~2,000+ reviews) — are both below 4.0 with >200 ratings, driven by reported technical/reliability complaints. So the flag is true for a subset of well-known apps but false for the category leaders by rating count (PredictWind, iNavX). Net verdict: does not indicate broad, uniform under-satisfaction — mixed.

- **Top apps not updated in >18 months: UNCLEAR — insufficient data.**
  No source returned a confirmed "last updated" date or version-history timestamp for any of the 10 apps (this is exactly the data iTunes Search API would normally supply, and it was unreachable). The only signal was an anecdotal, unverified claim in review snippets that Sail Racer "has not been updated in 7 years." That is a single, unconfirmed data point for one minor app, not evidence about the category leaders. Cannot be assessed reliably without App Store access.

- **Top 3 results are all free/ad-supported with no paid alternative: FALSE.**
  The category has clear paid options: iNavX is a $4.99 one-time purchase plus paid chart subscriptions up to $199.99/yr; Marine Navigation offers a one-time-purchase full version; ASA's Sailing Challenge is a flat $3.99 paid app; PredictWind's core value (departure planning, weather routing) sits behind $190–330/yr paid plans; SailFlow gates features behind $3.99–$14.99/mo tiers. Free-with-IAP/subscription is the dominant model, but genuine free-only, ad-supported apps were not the norm among the higher-profile results.

- **Fewer than 5 genuinely matching results (niche underserved): FALSE.**
  WebSearch surfaced well over 10 distinct, real, sailing/marine-relevant iOS apps across multiple sub-categories: navigation/chartplotting (iNavX, SeaNav, Navionics, Marine Navigation, i-Boating, Argo Navigation), weather/routing (SailFlow, PredictWind), logbooks (SailTies, Boating Logbook: Skipper, Ship's Log Book for Captains, LogBook, Saillogger), racing/tactics (Sail Racer, Sailrace, KWINDOO), and education/certification (ASA's Sailing Challenge). The niche is not underserved in raw count — it has established, long-running incumbents (iNavX since ~2009-era, PredictWind, Navionics) with large review bases (19.4K–32.1K ratings for the leaders), which is a sign of real, proven demand but also of high competitive/incumbency barriers.

## Overall assessment

The sailing/cruising niche shows genuine, proven demand (multiple incumbents with tens of thousands of ratings and years of operation) but is not underserved — navigation and weather-routing are dominated by entrenched, well-rated, well-monetized players (PredictWind, iNavX, Navionics) that would be hard to displace, while a few adjacent sub-niches (digital logbooks, ASA-style certification prep) look thinner and less saturated, with SailTies as a notable example of a small, highly-rated (4.95/5) but low-volume (150 iOS ratings) app that suggests room for a better-executed logbook or cert-prep product. Confidence in this assessment is low-to-moderate: rating counts, prices, and especially "last updated" dates could not be verified against a first-party source (iTunes Search API was blocked for this session) and instead rely on third-party aggregator snippets that may be stale or inconsistent with the live App Store.
