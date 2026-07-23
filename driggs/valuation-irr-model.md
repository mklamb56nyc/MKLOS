# Valuation cross-check — seller's IRR / basis model

A second, independent way to sanity-check Lot 3's price: from **Caldwell's economics**, not comps.
Caldwell (Lot 3) is a **passive co-investor**, *not* the developer — he took none of the entitlement
risk — so a fair expectation is an **8–15% IRR, best case**, on his 2023 basis. Compare that to
Nevin's ~$750k opinion. **The swing variable is what Caldwell paid in 2023 — which is why Karen's
number (Lot 2, a near-identical twin) is the linchpin.**

## Ask Karen (via Carrie) — the two questions that set the basis
1. **What did you pay** for Lot 2 in 2023? (≈ Caldwell's Lot 3 basis.)
2. **Were the road / electric / fiber included in that price, or did you pay a separate assessment?**
   - *Included* → basis = purchase price.
   - *Separate assessment* → **basis = price + assessment** (the "no free lunch" case — a higher basis
     justifies a higher fair sale price at the same IRR).
3. Any **ongoing dues** (road maintenance, fire-pond ~$1k/yr)? Minor, but part of cash invested.

## Assumptions
- **Hold:** Caldwell acquired 2023-04-03 (instr. 280113); "now" 2026-07-23 → **t ≈ 3.3 yr.**
- **Passive-investor IRR band:** 8–15% (best case). Compounding factors over 3.3 yr:
  8% → ×1.29 · 10% → ×1.37 · 12% → ×1.45 · 15% → ×1.59.
- Carrying costs (ag tax ~$37–62/yr, any dues) are small vs. price — ignored here; add to basis if known.

## Table A — implied "fair expectation" 2026 sale price (basis × IRR factor)
| Caldwell's 2023 basis | 8% | 12% | 15% |
|---|--:|--:|--:|
| $400k | $516k | $581k | $634k |
| $450k | $580k | $654k | $714k |
| $500k | $645k | $727k | $793k |
| $550k | $709k | $799k | $872k |
| $600k | $773k | $872k | $952k |

## Table B — reverse: the IRR that Nevin's $750k implies, by basis
| If Caldwell paid (2023) | $750k = IRR | Read |
|---|--:|---|
| $400k | ~21% | developer-level — rich |
| $450k | ~17% | above the best-case investor bar |
| $500k | ~13% | top of a fair band |
| $550k | ~10% | fair |
| $600k | ~7% | modest |

## How to use it
- Plug Karen's number in as the basis (add any assessment). Read the **fair band across 8–15%** in
  Table A → that's the reasonableness range to anchor an offer to **Caldwell**.
- If $750k sits **above the 15% column**, it prices in **developer-level returns** Caldwell didn't earn
  the risk for → argument to negotiate toward the 8–12% number.
- If a real **improvement assessment** pushes his basis up, $750k may already be a fair 8–12% return —
  in which case the comps (not IRR) are your better lever.

## Caveats (don't over-weight this)
- **A reasonableness frame, not a cap.** Caldwell can ask anything and **hold** (carrying cost ~$37/yr);
  these owners are holders, not distressed. The IRR math is the *argument*, not a forcing function.
- Pair with the **independent comps** (`comp-pull-request.md`) and **Karen's actual price**. Three
  angles — market comps, twin-lot actual, and seller-IRR — converging is the real basis for an offer.

*Formula: implied price = basis × (1 + IRR)^3.3. Implied IRR = (750,000 / basis)^(1/3.3) − 1.*
