#!/usr/bin/env python3
"""
Rebuild key exhibits from saved /data (no API keys needed).
Requires: geopandas, matplotlib, pandas.  TIGER tract shapefile is auto-downloaded (no key).
Upstream steps that DID need keys (ACS pull, ORS isochrones, OSM supply) are already baked into
/data (CSVs + GeoPackages); this script only re-renders from those. To refresh the underlying
data, see README section 3 (set CENSUS_API_KEY and ORS_API_KEY).
"""
import os, urllib.request, zipfile, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt

# ---- 1. Provision benchmark (fully self-contained) ----
def provision_benchmark():
    data=[("Aspirational standard (PSDG, 1 per 25k)",4.0,"#9a9a9a"),
          ("Laredo, TX (US leader)",3.5,"#7fb2df"),("Reno, NV",3.3,"#7fb2df"),("Sacramento, CA",3.3,"#7fb2df"),
          ("U.S. AVERAGE",1.04,"#111111"),("Suffolk County",0.39,"#FF9A6C"),
          ("Long Island (Nassau+Suffolk)",0.31,"#FF7A45"),("Nassau County",0.22,"#E8420E"),
          ("Our North Shore ring",0.0,"#8a1a05")]
    labels=[d[0] for d in data]; vals=[d[1] for d in data]; cols=[d[2] for d in data]
    fig,ax=plt.subplots(figsize=(11,6.2),dpi=150); y=list(range(len(data)))[::-1]
    ax.barh(y,vals,color=cols,height=.66)
    for yi,v in zip(y,vals): ax.text(v+0.06,yi,f"{v:g}",va="center",fontsize=9,fontweight="bold")
    ax.set_yticks(y); ax.set_yticklabels(labels,fontsize=9.5)
    ax.axvline(1.04,color="#111",ls="--",lw=1); ax.axvline(4.0,color="#9a9a9a",ls=":",lw=1)
    ax.set_xlabel("Public skateparks per 100,000 residents"); ax.set_xlim(0,4.4)
    ax.set_title("Nassau isn't just short of the ideal — it's about a fifth of the U.S. average\n"
                 "Skatepark provision per capita: benchmarks vs. Long Island (firmed July-2026 census: LI 9, Nassau 3, Suffolk 6)",
                 fontweight="bold",loc="left",fontsize=11)
    ax.spines[["top","right"]].set_visible(False)
    plt.tight_layout(); plt.savefig("maps/provision_benchmark.png",bbox_inches="tight"); plt.close()
    print("rebuilt maps/provision_benchmark.png")

# ---- 2. GC catchment rings (from saved GeoPackages) ----
def gc_catchment():
    import geopandas as gpd, pandas as pd
    from shapely.geometry import Point
    if not os.path.exists("tl_2023_36_tract.shp"):
        urllib.request.urlretrieve("https://www2.census.gov/geo/tiger/TIGER2023/TRACT/tl_2023_36_tract.zip","t.zip")
        zipfile.ZipFile("t.zip").extractall(".")
    if not os.path.exists("tl_2023_36_cousub.shp"):
        urllib.request.urlretrieve("https://www2.census.gov/geo/tiger/TIGER2023/COUSUB/tl_2023_36_cousub.zip","c.zip")
        zipfile.ZipFile("c.zip").extractall(".")
    if not os.path.exists("tl_2023_36_place.shp"):
        urllib.request.urlretrieve("https://www2.census.gov/geo/tiger/TIGER2023/PLACE/tl_2023_36_place.zip","p.zip")
        zipfile.ZipFile("p.zip").extractall(".")
    tr=gpd.read_file("tl_2023_36_tract.shp").to_crs(32618); na=tr[tr.COUNTYFP=="059"]
    cs=gpd.read_file("tl_2023_36_cousub.shp").to_crs(32618)
    toob=cs[(cs.COUNTYFP=="059")&(cs.NAME.str.contains("Oyster Bay"))]
    gc_city=gpd.read_file("tl_2023_36_place.shp").to_crs(32618); gc_city=gc_city[gc_city.NAME=="Glen Cove"]
    dac=na[na.GEOID.isin(["36059517201","36059517202","36059517101"])]
    bike=gpd.read_file("data/gc_bike.gpkg"); car=gpd.read_file("data/gc_iso.gpkg")
    GC=gpd.GeoSeries([Point(-73.6389,40.8685)],crs=4326).to_crs(32618)
    fig,ax=plt.subplots(figsize=(11,10),dpi=145)
    na.plot(ax=ax,color="#efede7",edgecolor="white",linewidth=.3)
    toob.plot(ax=ax,color="none",edgecolor="#555",linewidth=1.3,linestyle=(0,(6,3)))
    car.plot(ax=ax,color="#1C6FB5",alpha=.12,edgecolor="#0C4A84",linewidth=1.8)
    bike.plot(ax=ax,color="#2e7d32",alpha=.28,edgecolor="#1b5e20",linewidth=1.8)
    gc_city.plot(ax=ax,color="none",edgecolor="#c0392b",linewidth=1.6)
    dac.plot(ax=ax,color="#FF7A45",alpha=.55,edgecolor="#7a2c0c",linewidth=.8)
    GC.plot(ax=ax,color="#c0392b",marker="*",markersize=340,edgecolor="#111",zorder=9)
    b=car.total_bounds; ax.set_xlim(b[0]-3000,b[2]+3000); ax.set_ylim(b[1]-3000,b[3]+3000); ax.axis("off")
    ax.set_title("What a Glen Cove park reaches: 20-min bike & car catchments",loc="left",fontweight="bold")
    plt.tight_layout(); plt.savefig("maps/gc_catchment.png",bbox_inches="tight"); plt.close()
    print("rebuilt maps/gc_catchment.png")

if __name__=="__main__":
    os.makedirs("maps",exist_ok=True)
    provision_benchmark()
    try: gc_catchment()
    except Exception as e: print("gc_catchment needs geopandas + network for TIGER:",e)
    print("done. (All coverage polygons are in /data as GeoPackages to rebuild any other exhibit.)")
