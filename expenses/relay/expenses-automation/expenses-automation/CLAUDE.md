# Expenses Automation — Project Context

Personal financial analysis & tax planning automation for Mike. This project extends a manual
YTD transaction analysis (Jan 1 – May 10, 2026, five accounts) into a repeatable expenses
automation pipeline.

## Entities & tax context

- **Consulting LLC** (professional services) — the deduction entity
- **W-2 employer:** RTB Marketing and Tech — reimburses internet at a **flat monthly rate only**
  (only excess above the flat rate is relevant for deduction analysis)
- **LP interest:** MathCapital Fund I
- **Office:** Cavit Properties, Oyster Bay (rent); Compass Greater NY (leasing commission)

## Non-negotiable categorization rules (learned & confirmed by Mike)

These are authoritative decisions — do not re-litigate them:

1. **Guardian Life (~$7k/mo whole life)** → treat as **savings/investment**, NOT insurance
   expense, in all analysis.
2. **Voya/ReliaStar** → personal term life. No deduction.
3. **ArentFox Schiff** → employment-law legal fees, **100% LLC-deductible** (not personal legal).
4. **Vehicle:** 50% business-use allocation applied **across the household fleet** (4 cars,
   2 considered business-use) — not per-vehicle. Track gas + maintenance under this split.
5. **Beaver Dam** (youth hockey) → no dependent care credit.
6. **Auction houses / vintage & antique platforms** → Home/Decorating category.
7. **People Data Labs** (B2B data API), AI software tools, state filing fees, office supplies
   → LLC deductions.
8. Cavit Properties rent + Compass commission → LLC deductions.
9. **Confirmed personal travel (no deduction):** London, Costa Rica, DC history competition,
   Boston hockey, Philadelphia (×2 weekends), Alaska/PNW.
10. **Alaska trip:** Off the Beaten Path deposit is part of the Alaska trip (not a separate
    commitment). A **second payment equal to the deposit is still owed**.
11. Watch for **charge reversals** — net them out so spending categories aren't inflated.

## Three-tier classification model

- **GREEN** — confirmed clean LLC deduction
- **YELLOW** — needs review
- **GRAY** — confirmed personal / no action

Formula pattern per category: confirmed **IN** (full deduction), **SPLIT** (percentage-based,
e.g. vehicle 50%), or **personal/no action**.

## Data sources & parsing quirks (verified 2026-07-22)

| File | Parser | Quirk |
|---|---|---|
| `Chase0781_*.CSV` (credit card) | `pd.read_csv` | **Sign flip: negative = spend** |
| `Chase7618_*.CSV` (credit card) | `pd.read_csv` | **Sign flip: negative = spend** |
| `Chase0928_*.CSV` (checking) | `pd.read_csv(..., index_col=False)` | Trailing comma per row |
| `activity.xlsx`, `activity_1.xlsx` (Amex Platinum, Amex Delta Reserve) | `pd.read_excel(..., header=6)` | 6 rows of statement metadata; positive = spend |

- Amex sequential uploads auto-increment: `activity.xlsx`, `activity_1.xlsx`, …
- Excel sheet names: sanitize with `re.sub(r'[\\/*?:\[\]]', '', s)[:31]`
- State persistence between steps: pickle files (`all_tx.pkl`, `net_cat.pkl`, `all_tx_v4.pkl`)
- After any workbook save with formulas: run recalc verification (LibreOffice headless) and
  confirm zero formula errors before delivering.

## Open action items

1. **Sornik** (recurring professional support payments for Mike's children) — **never submitted
   for insurance reimbursement**. Highest-priority follow-up; automation should flag every
   Sornik payment as reimbursable-outstanding until Mike confirms submission.
2. Two simultaneous **Verizon** accounts — consolidation candidate.
3. **Streaming service** redundancy check.
4. **Storage unit** duplication check.
5. Unrecognized **book-summary app** subscription — identify and cancel.
6. Second **Alaska/PNW** payment (equal to deposit) still due — cash-flow item.
7. Ongoing vehicle gas/maintenance tracking at 50% household split.

## Working style

- Mike gives real-time corrections during sessions — treat them as authoritative and update the
  rules file (`rules/categorization.yml`) immediately so decisions persist.
- Iterative workbook versioning (v1, v2, … — currently at **v4**).
- Prefer editing `rules/categorization.yml` over hardcoding vendor logic in Python.

## Repo layout

```
data/       source exports (Chase CSVs, Amex xlsx)
src/        ingest.py, categorize.py, build_workbook.py
rules/      categorization.yml — vendor → category/tier/deduction rules (the living rulebook)
output/     generated workbooks + pickles
```

## Automation roadmap (the "extend this" goal)

Candidate next steps, roughly in order of value:
1. **Idempotent ingest** — drop new exports into `data/`, dedupe against prior pickle by
   (date, amount, description), append only new transactions.
2. **Rules engine maturity** — every manual correction becomes a YAML rule; unknown vendors
   land in YELLOW automatically.
3. **Recurring-payment monitor** — detect subscriptions/recurring charges, diff month-over-month,
   flag new/changed/duplicated ones (would have caught Sornik, Verizon ×2, storage units).
4. **Quarterly deduction summary** — auto-roll GREEN + SPLIT totals for estimated-tax planning.
5. **Reimbursement tracker** — Sornik and internet-excess ledger with submitted/outstanding status.
