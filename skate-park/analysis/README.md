# Glen Cove Skatepark — Access & Provisioning Analysis (reproducibility bundle)

This bundle preserves the geographic/demographic analysis behind the "underserved" case:
the provisioning shortfall, the access gap, and what a Glen Cove park would serve.
Last computed: July 2026.

--------------------------------------------------------------------------------
## 1. HEADLINE FINDINGS (see /maps for exhibits)

PART 1 — PROVISIONING (PSDG standard: 1 neighborhood skatepark per 25,000 residents)
- Long Island: needs ~117, has 14  -> 12% of standard
- Nassau County: needs ~56, has 4  -> 7% of standard
- Our North Shore ring: needs ~3, has 0 -> 0%
- Per-capita vs real world: US average ~1.0 skateparks/100k; LI 0.48; Nassau 0.29
  (Nassau ~= a quarter of the US average; leaders like Laredo/Reno ~3.3-3.5/100k).
  => Not just short of an ideal; below the actual national norm.

PART 2 — ACCESS (20-min isochrones; "gap" = residents with NO skatepark in reach)
Access gap TODAY (before any Glen Cove park), residents / kids:
- Glen Cove (city):      28,132 / 5,154  -> 100% shut out (bike AND car, today AND if Bethpage reopens)
- Glen Cove DAC area:    13,023 / 2,601  -> 100% shut out (every mode/scenario)
- Town of Oyster Bay:    97% can't bike to one; 61% can't drive to one in 20 min (21% if Bethpage back)
- Nassau County:         77% can't bike; 28% can't drive (14% if Bethpage back)

Share of that gap a Glen Cove park (at Maccarone) closes:
- Glen Cove & DAC:  ~90% of the gap (bike or car; identical with/without Bethpage — Bethpage never reaches us)
- Town of Oyster Bay (car): 29% today -> 72% if Bethpage reopens (park becomes the North Shore fix)
- Nassau (car): 24% today -> 43% if Bethpage back;  (bike) 4% — i.e., one park can't serve a county (= Part 1)

BETHPAGE: the town's only skatepark is closed. Modeled both ways. Our ring stays 18/18 in the gap
whether Bethpage is open or closed; the Glen Cove park's value to our community is Bethpage-proof.

--------------------------------------------------------------------------------
## 2. DATA SOURCES
- Demographics: US Census ACS 5-year 2018–2022, via the Census Data API (tract level, Nassau=059, Suffolk=103).
- Boundaries: Census TIGER/Line 2023 (tracts, places, county subdivisions) from www2.census.gov (no key).
- Skatepark supply: OpenStreetMap via Overpass API (leisure=skatepark), reconciled with web sources
  and known additions (Brentwood/Roberto Clemente). See supply rules below.
- Travel time: OpenRouteService isochrones (driving-car and cycling-regular), 1200 s = 20 min.

## 3. API KEYS REQUIRED (both free — NOT stored in this bundle)
Two upstream steps call APIs that need a free key. Get your own and provide them as environment
variables; do not commit them to any shared file.
- Census API key:  https://api.census.gov/data/key_signup.html  (emailed; must click the activation link)
    export CENSUS_API_KEY=...   # 40-hex-char key
- OpenRouteService key: https://openrouteservice.org/dev/#/signup  (create a token in the dashboard)
    export ORS_API_KEY=...
Notes:
- The Census API rejected the 2023 ACS vintage for this key; 2022 ACS5 works and is the standard release.
- The Census API percent-encoding gotcha: send geography params with raw ':' and '*' (urlencode safe=":*,"),
  or the API returns a misleading "Invalid Key" HTML page.
- If you only want to rebuild the MAPS, you do NOT need keys — see regenerate_maps.py (works from saved /data).

## 4. SUPPLY INVENTORY RULES (what counts as a "skatepark")
- INCLUDED: free, public, outdoor skateparks. Long Island count ≈14 open (Bethpage excluded as closed).
  Tanner Park (Copiague) counted as OPEN through its 2026 concrete rebuild (conservative — shrinks our gap).
  Queens/NYC parks tested and INCLUDED as supply (they don't change Nassau results — peninsula drive-times).
- EXCLUDED: indoor / fee-required / private facilities — Kohl's (Massapequa), Oil City (Oceanside), "110".
- Bethpage modeled as CLOSED (today) with a separate "reopened" scenario throughout.
- CAVEAT: the supply list is best-effort (OSM + additions); do a firmer park census before publishing.
  Even a generous recount (Nassau 6–8 parks) leaves Nassau ≈ half the US average or worse.

## 5. METHOD NOTES
- Coverage = union of 20-min isochrones around all supply points, by mode.
- "Gap" / "served" population computed by AREAL APPORTIONMENT: for each census tract,
  population × (tract area inside the ring / total tract area). More precise than whole-tract
  interior-point classification (which gave slightly higher, coarser numbers, e.g. 114,664 vs ~93,448).
  Standardize on area-weighting.
- Populations of interest: Nassau County (FIPS 059); Town of Oyster Bay (county subdivision);
  Glen Cove city (place); Glen Cove DAC area = tracts 36059517201, 36059517202, 36059517101
  (V1.0-designated; re-verify against the live NYSERDA V2.0 map before publishing).
- Access thresholds: the earlier flat "20-min drive" was arbitrary and modeled the wrong user
  (a driving parent). It is RETIRED as the headline in favor of (a) PSDG provisioning and
  (b) an access GAP shown by bike (kid, car-free) and car. 20-min figures kept only as a generous floor.
- CRS: EPSG:32618 (UTM 18N) for area math; areas reported in sq mi.

## 6. CAVEATS / RE-VERIFY BEFORE ANY SUBMISSION
- Park coordinates are approximate (±a few hundred m) but conclusions are robust to that.
- ACS 2018–2022 estimates carry margins of error (not shown; add for DAC-core figures).
- DAC tract set: confirm against live NYSERDA V2.0 map at the site address.
- Supply census: verify Tanner's open/closed status and do a firmer LI park count.

## 7. FILE MANIFEST
/data  — computed artifacts (CSV + GeoPackage), so maps rebuild without re-calling APIs
  master_supply.csv ...... all counted supply (16 LI open + 34 NYC + Bethpage closed)
  supply_final.csv ....... LI supply used for the LI/Nassau coverage
  li_gap.csv ............. per-tract pop/kids + car-gap flags (Nassau+Suffolk)
  nassau_scen.csv ........ per-Nassau-tract scenario flags (today / Bethpage / GC park)
  access_areas.csv ....... per-tract area memberships + catchment fractions
  ring_acs.csv ........... ACS detail for the North Shore ring (income, ethnicity, nativity)
  study_tracts.csv, drive_times.csv .. the 18-tract ring + drive times
  golf_courses.csv ....... golf-course counterpoint: private 18-hole clubs within ~5 mi of
                            the lead site (7 private + the municipal course), with distances
  *.gpkg ................. coverage polygons (covA today-car, covB Bethpage-car, gc_iso GC car,
                            gc_bike GC bike, nyc_cov, bike_today, bike_beth, etc.)
/maps  — exhibit PNGs (see filenames; provision_benchmark, gc_catchment, bethpage_matrix, etc.)
regenerate_maps.py — rebuilds the exhibits from /data (no API keys needed)
golf_courses.py ... establishes the private-18-hole-golf count within ~5 mi of the site
                   (embedded researched table; `--osm` discovers/refreshes from OpenStreetMap)
