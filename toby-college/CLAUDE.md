# toby-college — project context

## What this is
Toby's college-application tracker for the 2026–27 cycle (Fall 2027 entry). A single
Python build (`build_tracker.py`, openpyxl) generates a six-tab Excel workbook —
Application Tracker, Essay Prompts, Deadline Calendar, Prioritized Task List, Strategy
& Flags, and a live EV/PV Decision Model for the early-round choice. The workbook is
**generated from source** and kept diffable in git; the per-school findings and the
model math live in `docs/`.

## Current focus
- **Shortlist of 10** is set (Ambitious: MIT, Yale, UChicago · Match: UPenn, Columbia,
  Swarthmore · High confidence: Vassar, RIT, Wesleyan, U Minnesota). The other 11
  researched schools stay in the Application Tracker for reference.
- **Decision Model inputs are placeholder defaults** — replace the utilities and
  admission probabilities (yellow cells) with real reads before trusting the ranking.
  This is the main open task; it drives the early-lane decision.
- **Prompts/dates:** MIT and UChicago are already 2026–27; the rest are the 2025–26
  versions and finalize when the Common App opens (~Aug 1). Dates marked `*` are
  estimates — confirm on each school's site. The Essay Prompts tab links are authoritative.
- **The early-lane choice** (binding ED vs. non-binding EA, UChicago SSEN, yield
  protection) is the strategic question the Decision Model exists to inform.

## Conventions
- Edit files in place; keep changes scoped to this `toby-college/` directory.
- Keep anything private in this directory out of anything that later gets published.
- **The workbook is generated — don't hand-edit the `.xlsx`.** Edit `build_tracker.py`
  and re-run (`python build_tracker.py`) to produce `output/Toby_College_Tracker.xlsx`.
- To share a live copy with collaborators, push to the Google Sheet via the
  `google-sheets` MCP (see the root `CLAUDE.md` Google Sheets workflow); open the
  workbook with File → Open with Google Sheets so the Decision Model formulas and the
  Task List dropdown stay live.
