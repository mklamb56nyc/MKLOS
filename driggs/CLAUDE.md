# driggs — project context

## What this is
Due-diligence workspace for a prospective land purchase: **Lot 3, Crossed Arrows
Subdivision, Tetonia, Teton County, Idaho** — a ~23.85-acre raw, permit-ready building
lot at the foot of the Tetons. The goal is to evaluate cost, development opportunity, and
appeal before deciding whether to buy. This directory is the project's working record: a
research dossier (human-readable + machine-readable relay), an open-items / DD tracker,
and whatever analysis, cost models, or outreach notes accrue as the deal is worked.

- **Subject parcel:** Lot 3, PIN `RP021290000030` — raw/vacant, no well/septic/structures/water rights.
- **Seller:** Hardwick "Hacker" Caldwell (Charleston, SC) — a known-party resale, not an open listing.
- **Zoning:** LA-35 (Lowland Agriculture); one homesite + detached guest house permitted.
- **Location:** Sec 9, T5N R45E; centroid lat 43.77493, lon −111.15373; ~2.7 mi S of Tetonia.

## Current focus
Early DD — the dossier is captured; now work the open items that gate a go/no-go. The
critical ones (see `open-items.md`):
- **Get the 2023 price Caldwell paid the Beards** — the one real valuation anchor (Idaho
  is a non-disclosure state, so no public sale prices; assessed values are ag-productivity,
  not market).
- **EIPH septic determination** (test holes / soils) — lowland ground + shallow water
  table drive conventional-vs-engineered septic, which shapes budget and building envelope.
- **Pull the recorded CC&Rs + Development Agreement** (plat 279826) — can quietly restrict
  the LA-35 by-right flexibility; confirm the subdivision is "build-ready" (Certificate of
  Subdivision Completion + sanitary restrictions lifted).
- **Utility cost reads:** Fall River Electric line-extension estimate; local well-drill quote.

## Conventions
- Edit files in place; keep changes scoped to this `driggs/` directory.
- **The dossier is the fact base.** `dossier/crossed_arrows_lot3_dossier.md` is the
  human-readable source of record; `dossier/crossed_arrows_lot3_relay.json` is the matched
  machine-readable capture. When a fact changes or is verified, update both and note what it
  replaced if the prior value still matters.
- **`INDEX.txt` is the file map / current-state snapshot** — keep it current as things move.
- **`open-items.md` is the live DD tracker** — the actionable to-dos + contacts + decision
  log. Update it as items close.
- **Don't invent facts.** Idaho non-disclosure means many numbers (sale prices) are simply
  not obtainable from public records — say so rather than guessing. Distinguish assessed
  (ag-productivity) values from market values everywhere.
- Verify any regulatory item against the primary source (Teton County Planning, EIPH, IDWR,
  title company) before relying on it — contacts are in `open-items.md` and the dossier.
