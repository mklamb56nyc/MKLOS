# Bold by Nature — working context for Claude

A student-run outdoor leadership club being launched at Miss Porter's School
(Farmington, CT). **Molly** — Mike's daughter, a freshman there — is the founder
and owner; Mike does behind-the-scenes research, strategy, and planning. Everything
here is designed to be handed to Molly to run herself, not run by an adult.

## Layout

- `STRATEGY.md` — positioning thesis, the name (locked), three pillars (locked),
  the five patterns of great programs, principles. **Read this first.**
- `PLAN.md` — the six-phase roadmap, year-one program, status, open threads.
- `CULTURE.md` — vocabulary/traditions ideas (Phase 6), endgame vision,
  multi-year escalation.
- `research/` — **the verified fact base**: every factual claim checked against
  primary sources (2026-07), claim-by-claim verdicts with a URL per fact.
  `research/README.md` is the index and corrections scorecard.
- `deliverables/` — the two Word documents Molly hands to people, plus design
  cues and pending revisions. Drive copies exist; repo is the working source.
- `microsite/bold-by-nature.html` — the public web version of the proposal.
  Working source lives here; it publishes to the `received-wisdom-site` repo
  (Cloudflare Pages) as `boldbynature.html` via the PR-to-deploy flow in the
  root CLAUDE.md. When this file changes, republish by copying it over there.
  **Publish rule: no family names on the page** (root CLAUDE.md guardrail) —
  the club speaks as "we."
- `archive/` — the original April 2026 project relay, superseded and kept for
  provenance only.

## Locked decisions (don't reopen without Mike)

- **Name: "Bold by Nature."** Generic "Outing/Outdoors Club" names explicitly
  rejected. Rationale in `STRATEGY.md`.
- **Three pillars:** Sustainability & Stewardship · Leadership · Legacy.
- **Positioning:** an extension of Porter's existing identity — Sarah Porter's
  1843 vision, the school's own "bold"/"in nature" mission language, and
  Mountain Day as the asset to build on, not compete with ("Mountain Day is the
  spark. Bold by Nature is the fire.").

## How to work here

- **Quote facts from `research/`, not from memory** — especially anything Molly
  would say to administrators. Verbatim-safe quotes are marked there; so are the
  do-not-quote items (campus acreage, Mountain Day survey stats, Choate).
- Keep everything executable by a motivated freshman/sophomore.
- Keep the club inside Porter's own language.
- When a decision lands or an open thread closes, update `PLAN.md` (and
  `STRATEGY.md` if positioning changes), noting what it replaced if the prior
  value still matters. The archive is frozen — never update it.
- When regenerating a deliverable, follow `deliverables/README.md` (design cues
  + pending revisions), and refresh the Google Drive copy.
