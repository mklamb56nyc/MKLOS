# skate-park — project context

## What this is
Grassroots campaign to get a free, public, city-owned skatepark built in Glen Cove, NY —
lead site John Maccarone Memorial City Stadium, inside a state-designated Disadvantaged
Community (DAC). This directory is the project's working record: research dossier,
stakeholders, an open-questions tracker, the strategy brief, a concept microsite, and a
reproducible GIS access/provisioning analysis (the quantified "underserved" case).

## Current focus
2026 is a readiness year — line everything up to file the moment the next state park-grant
window opens (~2027):
- Get a real build-cost number (a builder site tour of Maccarone) — the biggest open gap.
- Win **written** city site approval (the critical-path gate) via the Rec Commission / mayor.
- Cultivate Assemblymember Lavine (A-13) as the primary state-capital path (DASNY).
- Still open from the pre-publication checklist: firm up the LI/Nassau supply census and
  re-verify the DAC V2.0 tracts. (The microsite went live July 2026 at `/sk8gc.html` on the
  public site ahead of these — owner's call. The placeholder-email item is done:
  contact is mklamb@gmail.com.)
- The microsite is published from the `received-wisdom-site` repo as `sk8gc.html`. The copy
  here is the working source — when it changes, republish by copying it over there
  (see the root CLAUDE.md "Website" section for the PR-to-deploy flow).

## Conventions
- Edit files in place; keep changes scoped to this `skate-park/` directory.
- Keep anything private in this directory out of anything that later gets published.
- `INDEX.txt` is the file map / current-state snapshot — keep it current as things move.
- API keys (Census, OpenRouteService) live in env vars `CENSUS_API_KEY` / `ORS_API_KEY`,
  never committed. See `analysis/README.md` §3. `knowledge-base/05_api-keys.txt` is local-only
  and git-ignored.
