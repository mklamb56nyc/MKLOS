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

# ---- 4. Access story (two-panel, on-brand): today's gap vs a Glen Cove park ----
def access_story():
    """Nassau/TOB/Greater Glen Cove access story by BIKE (the honest, kid test).
    Panel A: today's 20-min bike coverage; Panel B: + a Glen Cove park's ring.
    The cached bike union predates the firmed census, so contributions from
    now-excluded parks (Huntington's resident-ID pair, Tanner mid-rebuild,
    Red Creek fee) are ERASED via isolated buffers — no included park is within
    12 km of any of them, so the erase is clean. On-brand palette."""
    import geopandas as gpd
    from shapely.geometry import Point
    PAPER="#F1EFE9"; INK="#191A1E"; SOFT="#4C4D55"; POOL="#1C6FB5"; POOLD="#0C4A84"
    SPARK="#FF5A1F"; SPARKD="#C43F0E"
    for f,u in [("tl_2023_36_tract.shp","TRACT/tl_2023_36_tract.zip"),
                ("tl_2023_36_cousub.shp","COUSUB/tl_2023_36_cousub.zip"),
                ("tl_2023_36_place.shp","PLACE/tl_2023_36_place.zip")]:
        if not os.path.exists(f):
            urllib.request.urlretrieve("https://www2.census.gov/geo/tiger/TIGER2023/"+u,"z.zip")
            zipfile.ZipFile("z.zip").extractall(".")
    tr=gpd.read_file("tl_2023_36_tract.shp").to_crs(32618)
    na=tr[tr.COUNTYFP=="059"]; su=tr[tr.COUNTYFP=="103"]
    cs=gpd.read_file("tl_2023_36_cousub.shp").to_crs(32618)
    toob=cs[(cs.COUNTYFP=="059")&(cs.NAME.str.contains("Oyster Bay"))]
    gc=gpd.read_file("tl_2023_36_place.shp").to_crs(32618); gc=gc[gc.NAME=="Glen Cove"]
    dac=na[na.GEOID.isin(["36059517201","36059517202","36059517101"])]
    bike=gpd.read_file("data/bike_today.gpkg").to_crs(32618)
    excl=[(-73.3649,40.8625),(-73.3113,40.8822),(-73.3978,40.6579),(-72.5356,40.8873)]
    ex=gpd.GeoSeries([Point(x,y) for x,y in excl],crs=4326).to_crs(32618).buffer(9000)
    from shapely.ops import unary_union
    bike_geom=unary_union(bike.geometry.values).difference(unary_union(ex.values))
    bike=gpd.GeoDataFrame(geometry=[bike_geom],crs=32618)
    gcb=gpd.read_file("data/gc_bike.gpkg").to_crs(32618)
    parks=[("Long Beach",-73.6013,40.5902),("Baldwin",-73.6092,40.6256),
           ("Manorhaven",-73.7161,40.8388),("Laurelton (Queens)",-73.7365,40.6703),
           ("Far Rockaway (Queens)",-73.7465,40.5952)]
    pk=gpd.GeoDataFrame({"name":[p[0] for p in parks]},
        geometry=[Point(p[1],p[2]) for p in parks],crs=4326).to_crs(32618)
    beth=gpd.GeoSeries([Point(-73.4869,40.7439)],crs=4326).to_crs(32618)
    mac=gpd.GeoSeries([Point(-73.6389,40.8685)],crs=4326).to_crs(32618)
    b=na.total_bounds; pad=2000
    fig,axes=plt.subplots(1,2,figsize=(16,8.8),dpi=140)
    fig.patch.set_facecolor(PAPER)
    for i,ax in enumerate(axes):
        ax.set_facecolor(PAPER)
        su.plot(ax=ax,color="#E9E6DF",edgecolor="white",linewidth=.2)
        na.plot(ax=ax,color="#EFEDE7",edgecolor="white",linewidth=.3)
        toob.plot(ax=ax,color="none",edgecolor=SOFT,linewidth=1.4,linestyle=(0,(5,3)))
        bike.plot(ax=ax,color=POOL,alpha=.32,edgecolor=POOLD,linewidth=1.2)
        if i==1:
            gcb.plot(ax=ax,color=SPARK,alpha=.36,edgecolor=SPARKD,linewidth=1.8)
            mac.plot(ax=ax,color=SPARKD,marker="*",markersize=430,edgecolor=INK,zorder=9)
        gc.plot(ax=ax,color="none",edgecolor=SPARKD,linewidth=1.7)
        dac.plot(ax=ax,color=SPARK,alpha=(.55 if i==0 else .25),edgecolor=SPARKD,linewidth=.7)
        pk.plot(ax=ax,color=POOLD,markersize=55,edgecolor="white",linewidth=1,zorder=8)
        ax.scatter(beth.x,beth.y,marker="X",s=100,color=SOFT,edgecolor="white",linewidth=1,zorder=8)
        ax.annotate("Bethpage\n(closed)",xy=(float(beth.x.iloc[0]),float(beth.y.iloc[0])),
                    xytext=(8,-26),textcoords="offset points",fontsize=8.5,color=SOFT)
        ax.annotate("Town of Oyster Bay",xy=(.565,.185),xycoords="axes fraction",
                    fontsize=9,color=SOFT,style="italic")
        ax.annotate("Glen Cove",xy=(float(gc.geometry.centroid.x.iloc[0]),
                    float(gc.geometry.centroid.y.iloc[0])),xytext=(-64,34),
                    textcoords="offset points",fontsize=9,color=SPARKD,fontweight="bold")
        ax.set_xlim(b[0]-pad,b[2]+pad); ax.set_ylim(b[1]-pad,b[3]+pad); ax.axis("off")
    A,B=axes
    A.set_title("TODAY — where a kid can bike to a free skatepark in 20 minutes",
                loc="left",fontsize=13,fontweight="bold",color=INK)
    B.set_title("WITH ONE PARK IN GLEN COVE",loc="left",fontsize=13,fontweight="bold",color=INK)
    A.text(.015,.155,"Shut out today:",transform=A.transAxes,fontsize=11,
           color=INK,fontweight="bold")
    A.text(.015,.02,"77% of Nassau County\n97% of the Town of Oyster Bay\n"
           "100% of Glen Cove & the DAC core",transform=A.transAxes,fontsize=10.5,
           color=INK,linespacing=1.55)
    B.text(.015,.155,"One park at Maccarone:",transform=B.transAxes,fontsize=11,
           color=SPARKD,fontweight="bold")
    B.text(.015,.02,"~90% of Glen Cove & the DAC core\ncome inside a kid's bike ride —\n"
           "plus thousands more across the Town",transform=B.transAxes,fontsize=10.5,
           color=INK,linespacing=1.55)
    import matplotlib.patches as mpatches
    import matplotlib.lines as mlines
    handles=[mpatches.Patch(facecolor=POOL,alpha=.32,edgecolor=POOLD,label="20-min bike ride to an existing free park"),
             mpatches.Patch(facecolor=SPARK,alpha=.36,edgecolor=SPARKD,label="20-min bike ride to a Glen Cove park"),
             mpatches.Patch(facecolor=SPARK,alpha=.55,edgecolor=SPARKD,label="state-designated disadvantaged community"),
             mlines.Line2D([],[],color=SPARKD,linewidth=1.7,label="Glen Cove city limits"),
             mlines.Line2D([],[],marker="o",color="none",markerfacecolor=POOLD,markeredgecolor="white",markersize=9,label="existing free public skatepark"),
             mlines.Line2D([],[],marker="*",color="none",markerfacecolor=SPARKD,markeredgecolor=INK,markersize=15,label="proposed park (Maccarone) — and Bethpage marked ✕ (closed)")]
    fig.legend(handles=handles,loc="lower center",ncol=3,frameon=False,fontsize=9.5,
               labelcolor=SOFT,bbox_to_anchor=(.5,.0))
    fig.suptitle("The access story: almost nobody on the North Shore can reach a skatepark on their own — one park changes that",
                 x=.02,ha="left",fontsize=15,fontweight="bold",color=INK)
    plt.tight_layout(rect=[0,.055,1,.94])
    plt.savefig("maps/access_story.png",bbox_inches="tight",facecolor=PAPER); plt.close()
    print("rebuilt maps/access_story.png")
