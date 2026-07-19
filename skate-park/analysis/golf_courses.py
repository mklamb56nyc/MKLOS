#!/usr/bin/env python3
"""
Golf-course provisioning counterpoint for the Glen Cove skatepark case.

Establishes, defensibly, how many PRIVATE 18-hole golf courses sit within a
~5-mile radius of the lead skatepark site (John Maccarone Memorial City Stadium,
Glen Cove) — the "golf courses vs. a 25-minute drive to a skatepark" contrast in
the strategy brief (04).

Two modes:
  (default)  Compute straight-line distances from an embedded, web-researched
             table of clubs (name, town, address, private/public, holes, source).
             Runs anywhere; writes data/golf_courses.csv.
  --osm      Refresh coordinates and DISCOVER courses directly from OpenStreetMap
             via the Overpass API (leisure=golf_course within the radius), the way
             the skatepark supply inventory was built. Needs outbound network to
             overpass-api.de (blocked in the cloud sandbox; run locally to verify).

The embedded table was researched July 2026 from club sites and golf directories
(GolfDigest, GolfPass, PGA directory, club websites); see `source` per row. Club
coordinates in the embedded table are APPROXIMATE (geocoding APIs were unreachable
from the authoring sandbox) — run `--osm` where egress is open to replace them with
authoritative OSM values and exact distances. The conclusion is robust to the
approximation: every club below is in a town bordering Glen Cove, and the farthest
(Engineers, Roslyn Harbor) is ~3.5 mi, corroborated by the 3.45-mi length of Glen
Cove Avenue connecting the two.
"""
import csv, math, os, sys

RADIUS_MILES = 5.0
# Lead site: John Maccarone Memorial City Stadium, Glen Cove (approx; central Glen Cove).
SITE = ("Lead site — Maccarone City Stadium, Glen Cove", 40.860, -73.631)

# name, town, address, access, holes, lat, lon, source
CLUBS = [
    ("Nassau Country Club", "Glen Cove", "30 St. Andrews Lane, Glen Cove NY 11542",
     "private", 18, 40.856, -73.641, "nassaucc.com / GolfPass 9379"),
    ("North Shore Country Club", "Glen Head", "500 Shore Road, Glen Head NY 11545",
     "private", 18, 40.842, -73.643, "nsccli.com / GolfPass 9382"),
    ("Glen Head Country Club", "Glen Head", "240 Glen Cove Rd, Glen Head NY 11545",
     "private", 18, 40.838, -73.626, "glenheadcountryclub.org / GolfDigest"),
    ("Brookville Country Club", "Old Brookville / Glen Head", "210 Chicken Valley Rd, Glen Head NY 11545",
     "private", 18, 40.848, -73.585, "PGA dir / GolfPass 9380"),
    ("Piping Rock Club", "Locust Valley / Matinecock", "150 Piping Rock Rd, Locust Valley NY 11560",
     "private", 18, 40.879, -73.588, "Wikipedia / GolfDigest"),
    ("The Creek Club", "Lattingtown", "1 Horse Hollow Rd, Lattingtown NY 11560",
     "private", 18, 40.898, -73.606, "creek.net / GolfDigest"),
    ("Engineers Country Club", "Roslyn Harbor", "Roslyn Harbor NY 11576",
     "private", 18, 40.807, -73.651, "Wikipedia / invitedclubs.com"),
    # Public — excluded from the private count, listed for completeness/contrast.
    ("Glen Cove Golf Club (municipal)", "Glen Cove", "109 Lattingtown Rd, Glen Cove NY 11542",
     "public", 18, 40.882, -73.646, "glencoveny.gov municipal golf"),
]

def haversine_mi(a_lat, a_lon, b_lat, b_lon):
    R = 3958.7613  # earth radius, miles
    p1, p2 = math.radians(a_lat), math.radians(b_lat)
    dp = math.radians(b_lat - a_lat)
    dl = math.radians(b_lon - a_lon)
    h = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2 * R * math.asin(math.sqrt(h))

def from_table():
    rows = []
    for name, town, addr, access, holes, lat, lon, src in CLUBS:
        d = haversine_mi(SITE[1], SITE[2], lat, lon)
        rows.append(dict(name=name, town=town, address=addr, access=access,
                         holes=holes, dist_mi=round(d, 2),
                         within_5mi=("yes" if d <= RADIUS_MILES else "no"),
                         lat=lat, lon=lon, source=src))
    rows.sort(key=lambda r: r["dist_mi"])
    return rows

def osm_discover():
    """Discover golf courses from OSM within RADIUS_MILES; needs network."""
    import requests
    meters = int(RADIUS_MILES * 1609.34)
    q = (f"[out:json][timeout:60];"
         f'(nwr["leisure"="golf_course"](around:{meters},{SITE[1]},{SITE[2]}););'
         f"out center tags;")
    r = requests.post("https://overpass-api.de/api/interpreter", data={"data": q}, timeout=90)
    r.raise_for_status()
    rows = []
    for el in r.json().get("elements", []):
        t = el.get("tags", {})
        lat = el.get("lat") or el.get("center", {}).get("lat")
        lon = el.get("lon") or el.get("center", {}).get("lon")
        if lat is None or lon is None:
            continue
        d = haversine_mi(SITE[1], SITE[2], lat, lon)
        rows.append(dict(name=t.get("name", "(unnamed)"), town="", address="",
                         access=t.get("access", ""), holes=t.get("holes", ""),
                         dist_mi=round(d, 2), within_5mi=("yes" if d <= RADIUS_MILES else "no"),
                         lat=lat, lon=lon, source="OSM/Overpass"))
    rows.sort(key=lambda r: r["dist_mi"])
    return rows

def main():
    rows = osm_discover() if "--osm" in sys.argv else from_table()
    priv18 = [r for r in rows if r["access"] == "private" and str(r["holes"]) == "18"
              and r["within_5mi"] == "yes"]
    os.makedirs("data", exist_ok=True)
    with open("data/golf_courses.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name", "town", "address", "access", "holes",
                                          "dist_mi", "within_5mi", "lat", "lon", "source"])
        w.writeheader(); w.writerows(rows)
    print(f"Anchor: {SITE[0]} ({SITE[1]}, {SITE[2]}); radius {RADIUS_MILES} mi\n")
    for r in rows:
        flag = "*" if (r["access"] == "private" and str(r["holes"]) == "18"
                       and r["within_5mi"] == "yes") else " "
        print(f" {flag} {r['dist_mi']:>4} mi  {r['access']:<7} {r['holes']}h  {r['name']} ({r['town']})")
    print(f"\nPRIVATE 18-hole courses within {RADIUS_MILES} mi: {len(priv18)}")
    print("  (* marks those counted)  ->  wrote data/golf_courses.csv")

if __name__ == "__main__":
    main()
