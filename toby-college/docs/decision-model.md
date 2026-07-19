# Decision Model — methodology

The **Decision Model** tab prices out the one early-round decision that gates
everything else: which early lane to use. It is a small expected-utility model with
fully editable inputs. Everything is live Excel/Sheets formulas so edits recompute.

## Inputs (the yellow cells)

Per school:
- **Utility `U`** (0–100): how much Toby values enrolling there. Keep values distinct.
- **`P(admit) early`**: admission probability in that school's best early round
  (EA / SCEA / ED as applicable).
- **`P(admit) Regular`**: admission probability in Regular Decision.

Three global knobs:
- **UChicago SSEN admit probability** — the ED0 (pre-Nov-1 binding) odds.
- **Certainty / less-work bonus** (utility pts) — value of resolving early.
- **Aid-comparison penalty if bound** (utility pts) — cost of committing before
  seeing financial-aid offers.

Keep probabilities between 0.01 and 0.98 (the engine uses `LN(1 - p)`).

## Core quantity: "best-admit" expected value

Toby enrolls at the **highest-utility school that admits him**. For a probability
vector `p` (one entry per school) the probability he ends up enrolling at school `i` is

```
P(enroll_i) = p_i * PROD over j with U_j > U_i of (1 - p_j)
```

i.e. `i` admits him and nobody he prefers does. Implemented order-independently as

```
enroll_i = p_i * EXP( SUMPRODUCT( (U > U_i) * LN(1 - p) ) )
BestAdmitEV(p) = SUMPRODUCT(U, enroll)
```

The residual "admitted nowhere" mass carries utility 0 (tiny, given a ~0.97 safety).

## Strategies

Each strategy is just a choice of which round each school uses, plus (for binding
plans) a forced-enroll branch.

- **A — Yale SCEA** (non-binding, restrictive): Yale uses early odds, Minnesota uses
  EA, everyone else Regular (no early MIT/UChicago allowed). `EV = BestAdmitEV(vA)`.
- **B — UChicago SSEN** (binding, resolves pre-Nov-1):
  `EV = p_ssen*U_uchicago + (1 - p_ssen)*BestAdmitEV(vB_fallback)`.
  The fallback keeps **MIT at EA odds** (SSEN resolves before Nov 1, so MIT EA is
  still available), UChicago at Regular, others Regular.
- **C — All non-binding EA**: MIT, UChicago, RIT, Minnesota at early odds; the rest
  Regular. `EV = BestAdmitEV(vC)`.
- **D — UPenn ED** (binding, Nov 1): `EV = p_penn*U_penn + (1 - p_penn)*BestAdmitEV(all-RD)`.
  A Nov-1 ED denial leaves no MIT EA, so the fallback is all-Regular — this is why a
  reach-ED scores below SSEN.
- **E — Vassar ED** (binding, lock a likely): same shape as D with Vassar.

## PV vs EV

- **EV** = expected utility of where he enrolls (outcome only).
- **PV** = EV adjusted for process factors:

```
PV = EV
   + certainty_bonus * P(the early round resolves)
   - aid_penalty     * P(he is bound before comparing aid)
```

For binding strategies both probabilities equal the binding-admit probability. For
Yale SCEA the certainty bonus is weighted by the SCEA admit probability and there is
no aid penalty (non-binding). For all-EA the certainty bonus is weighted by the
chance of a *top-choice* early admit (MIT or UChicago), no aid penalty.

## Interpreting it

The winner is sensitive to inputs by design. Roughly: raise UChicago's utility or
SSEN probability and **B** dominates; raise Yale's utility / SCEA odds and **A**
climbs; set the aid penalty to 0 and the binding plans rise. The defaults shipped in
the workbook are illustrative, not prescriptive — replace them with real reads.
