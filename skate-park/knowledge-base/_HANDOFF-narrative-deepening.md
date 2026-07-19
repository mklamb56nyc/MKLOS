# SESSION HANDOFF — deepening the brief (Part One) into talking points

**Purpose:** carry live context across a session boundary. A new session clones the
repo fresh with no memory of the prior chat — this file is that memory. Fold the
useful parts into the dossier/brief and delete this scaffolding once §1 is finalized.

## The task in progress
Take the strategy brief (`04_glen-cove-skatepark-brief.txt`), **Part One**, one layer
down: break each of the 5 sections into **named sub-points with speakable talking-point
bullets** an advocate could speak from. Work them **in order, §1 → §5**.

- **§1 — DONE** and committed (commit `caed148`): "Our kids need this now" is now split
  into **1a–1d** (problem → why a skatepark → retire the caricature → safety evidence).
- **§2–§5 — NOT STARTED.** Apply the same sub-point + talking-bullet treatment.

## OPEN DECISION — §1a reframe (pending the user's approval)
The user flagged that §1a as written ("more scheduled, more screen-bound") reads as a
**rich person's problem** and undercuts the equity spine. We need a universal objective
for "our kids" that lands across the economic-demographic spectrum (DAC core *and*
Locust Valley). External research (below) supports the reframe. **Proposed replacement
for 1a — NOT yet committed, get user's sign-off first:**

> **1a. The problem we're solving — every kid needs a free place to be active and
> belong, and fewer and fewer have one.**
> Strip it to what's universal: regardless of family income, a kid needs a safe, free
> place to move their body, make friends, and belong — somewhere that's *theirs*,
> outdoors, that costs nothing to walk into. Fewer and fewer have it, and the shortage
> falls hardest on the kids with the least.
> - The need is universal; the shortage isn't evenly shared. Lower-income kids are
>   **less physically active and have less access to nearby, quality parks** than
>   wealthier kids — and skateparks themselves have too often been built in affluent
>   suburbs that already have everything.
> - It's a belonging problem as much as an activity one. What's scarce for *all* kids
>   now is unstructured, face-to-face time in a place they can claim as their own — and
>   that scarcity is deepest where public investment is thinnest.
> - Say it plainly: "This isn't about giving kids one more thing to do. It's about
>   giving *every* kid — not just the ones whose families can pay — a free place to be
>   active, make friends, and belong."

## PENDING MICRO-EDITS to §1 (proposed, not yet applied)
1. **1b** — fold in the USC hard numbers: skating is chosen "to get away from stress"
   (**62%**) and "to have fun" (**76%**); it builds cross-race/class friendships; and
   PSDG's language ("positive youth development… mental resilience… belonging… improves
   academic performance, reduces at-risk factors").
2. **1d** — upgrade the Long Beach evidence: name the park (**Michael K. Green
   skatepark**, opened 2003), cite the source (**City of Long Beach / ASK Foundation**),
   and **correct violent crime from "29%" to "~30%"** (sourced figures: drug incidents
   −61%, violent crime −30%, overall −23% within 3 years).

## RESEARCH EVIDENCE BASE for §1 (gathered via WebSearch; full-text fetch was blocked)
The key reframe insight: the **best independent study deliberately centered low-income
and minoritized skaters** — so the strongest evidence *is* the equity story, which is
exactly what rebuts the "rich kid" framing.

- **USC "Beyond the Board"** (Pullias Center, USC Rossier + Annenberg; lead: Neftalie
  Williams). 5,000+ national survey responses, 120+ interviews, ages 13–25, focus on
  low-income/minoritized skaters. Findings: fun (76%) and stress relief (62%) are the
  top reasons; builds relationships across race/class; **racially minoritized skaters
  felt *safer* in the skate community than in predominantly white spaces.**
  https://pullias.usc.edu/project/usc-skate-study/
- **Peer-reviewed** (Sport & Exercise Psychology, 2023; 26 youth 14–17): skating fosters
  well-being, companionship, a valued sense of community.
- **"Skateparks as communities of care"** (*Pedagogy, Culture & Society*, 2023): skateparks
  aided girls'/non-binary youth mental-health recovery during lockdown.
  https://www.tandfonline.com/doi/full/10.1080/14681366.2023.2258382
- **Access/PA equity** (PMC): lower-income & BIPOC youth are less physically active and
  have less access to nearby, quality parks; modern skateparks skew to affluent white
  suburbs — a national mirror of our golf-course contrast.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC7494055/
- **Public Skatepark Development Guide** (planners' reference; also source of the
  1-per-25,000 benchmark already in the brief): positive youth development, physical
  activity, mental resilience, belonging, academic gains, "positive options to teens."
  https://publicskateparkguide.org/
- **"Third place"** frame (Ray Oldenburg, *The Great Good Place*): free public commons
  beyond home/school; research says third places matter *most* for marginalized youth.
- **Long Beach crime data**: Michael K. Green skatepark (2003); within 3 yrs drug
  incidents −61%, violent crime −30%, overall −23% (City of Long Beach / ASK Foundation).
  https://www.asklongbeach.org/news/usc-skate-study-beyond-board-findings-field

**NOTE for the new session:** if network access has been switched to **Full** (see
below), *re-fetch these primary sources full-text* (USC/ERIC PDFs, the T&F journal) to
lock in exact figures and adversarially verify before anything goes public — search
snippets are paraphrases, not quotable primary text.

## ENVIRONMENT / WORKFLOW notes
- **Network access:** this project ran under the **Trusted** egress policy, which blocks
  WebFetch to non-allowlisted domains (only WebSearch worked). The user is switching the
  environment to **Full** so a fresh session can fetch any page. If you can fetch e.g.
  `files.eric.ed.gov`, Full is active.
- **Git is now fully automatic and invisible** (see root `CLAUDE.md`, updated this
  session): commit and push the `claude/…` branch automatically at natural stopping
  points, no confirmation, don't narrate it. Don't reintroduce a review/confirm gate.
- Working branch: `claude/skatepark-project-29fyf6`.
