# Toby — College Application Tracker

A single-file Python build that generates a six-tab Excel workbook tracking a
2026–27 (Fall 2027 entry) college application cycle: deadlines, essay prompts,
tasks, strategy, and a live expected-value decision model for the early-round choice.

The workbook is **generated from source** — edit `build_tracker.py` and re-run to
produce a fresh `output/Toby_College_Tracker.xlsx`. That keeps the whole thing
diffable in git rather than living inside an opaque binary.

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate   # optional
pip install -r requirements.txt
python build_tracker.py                             # writes ./Toby_College_Tracker.xlsx
```

By default the script writes to the path in the last line of `build_tracker.py`
(`wb.save(...)`). Point it wherever you like — e.g. `output/Toby_College_Tracker.xlsx`.

Open the result in Google Sheets with **File → Open with Google Sheets** (or
Import → Convert) so the Decision Model formulas and the Task List status dropdown
stay live.

## Living copy in Google Drive

The shared, collaboratively-edited tracker lives in Google Drive as a **native
Google Sheet**. Source-of-truth model:

- **The Drive Sheet is the living document.** Once seeded, edits (Decision Model
  inputs, Task statuses, notes) happen in the Sheet — that's the point of sharing it.
- **`build_tracker.py` is the seed/generator**, not a repeated overwrite. Re-running
  the build and re-uploading would clobber everyone's live edits, so **don't** publish
  over the live Sheet from a rebuild.
- **The repo `.xlsx` is a snapshot/backup.** To version a point-in-time copy, download
  the Sheet as `.xlsx` into `output/` and commit it.

**Seed it once (manual, ~1 min):** upload `output/Toby_College_Tracker.xlsx` to Drive,
then right-click → **Open with → Google Sheets** (this creates a native Sheet), and
**Share** it with edit access to the people who need it. Native format keeps the
Decision Model formulas and the Task List dropdown live.

**Programmatic sync (optional):** the repo is wired for a `google-sheets` MCP
(see root `.mcp.json`) that can push/update the Sheet from a session — useful for
refreshing the *static* reference tabs without touching the human-edited inputs. It
needs a one-time OAuth authorization (claude.ai connector settings) before it can be
used; until then, seed and edit manually as above.

## The six tabs

1. **Application Tracker** — all 21 researched schools, tier-coded (red = Ambitious,
   amber = Match, green = High confidence). The 10-school working shortlist is
   highlighted green. Each round cell reads `deadline → notification`.
2. **Essay Prompts** — every school's prompts + word limits, with the official
   application link in each banner (source of truth for exact wording).
3. **Deadline Calendar** — chronological, scoped to the shortlist of 10.
4. **Prioritized Task List** — ordered tasks with a status dropdown and a
   `COUNTIF` progress counter.
5. **Strategy & Flags** — early-lane logic, UChicago SSEN, binding vs. non-binding,
   testing, recommenders, yield protection.
6. **Decision Model** — a live EV/PV model of the early-lane choice. Edit the
   yellow cells (utilities + admission probabilities); the strategy ranking updates.
   See `docs/decision-model.md` for the math.

## The shortlist of 10

| Tier | Schools |
|------|---------|
| Ambitious | MIT, Yale, University of Chicago |
| Match | UPenn, Columbia, Swarthmore |
| High confidence | Vassar, RIT, Wesleyan, University of Minnesota |

The other 11 researched schools (Princeton, Brown, Cornell, Williams, Tufts, NYU,
Oberlin, Connecticut College, University of Washington, Ithaca, Baruch/CUNY) stay
in the Application Tracker for reference; the calendar/tasks/strategy are scoped to
the 10.

## Repo layout

```
toby-college-tracker/
├── build_tracker.py        # the whole build (openpyxl); edit + re-run
├── requirements.txt        # openpyxl==3.1.5
├── output/
│   └── Toby_College_Tracker.xlsx   # generated artifact (rebuild any time)
├── docs/
│   ├── admissions-research.md      # per-school findings + sources + caveats
│   └── decision-model.md           # EV/PV methodology and formulas
└── README.md
```

## Caveats baked into the data

- Most essay prompts and dates are the **2025–26** official versions; MIT and
  UChicago are already **2026–27**. The rest finalize when the Common App opens
  (~Aug 1). The links in the Essay Prompts tab are authoritative.
- Decision Model inputs are **placeholder defaults** — replace utilities and
  probabilities with real reads before trusting the ranking.
- Dates marked `*` in the workbook are estimates; confirm on each school's site.
