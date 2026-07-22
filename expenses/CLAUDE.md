# expenses — project context

Personal expense automation: a regular scan of card/bank exports plus Gmail receipts that
classifies every transaction and preps three submission paths. Continues the earlier
"expenses-automation" project (manual v4 analysis → pipeline), drained into this repo
2026-07-22 — its accumulated decisions live on below and in `rules/categorization.yml`.

## Entities & destinations
- **Received Wisdom** (my S Corp — the deduction entity; the earlier project called it
  "Consulting LLC") → **monthly package emailed to my CPA**: itemized spreadsheet +
  receipts + summary, prepared as a Gmail draft in my voice per `/VOICE.md`.
- **RTB House** (W2 employer; earlier notes said "RTB Marketing and Tech" — assumed same,
  confirm) → reimbursables submitted via **Rydoo email intake**: receipts forwarded as
  attachments to `receipts@rydoo.com` from a registered address create expenses
  automatically, one per attachment
  ([Rydoo help](https://help.rydoo.com/hc/en-be/articles/8139189477660-Forward-a-receipt-via-email)).
  Prepared as Gmail forward drafts; I hit send. Known policy fact: internet is reimbursed
  at a **flat monthly rate** — only the excess matters for deduction analysis.
- **Insurance reimbursement tracker** — Sornik payments (professional support for the
  kids) have **never been submitted for reimbursement**; every payment carries
  `flag=REIMBURSEMENT_OUTSTANDING` until I confirm submission. Highest-priority open item.
- Also in the picture: **MathCapital Fund I** (LP interest); office = Cavit Properties,
  Oyster Bay (rent) + Compass Greater NY (leasing commission).

**Income streams (confirmed by me 2026-07-22, visible in the 0928 checking data):**
1. `C71393 RTB HOUSE PAYROLL` ACH, $9,560.44 biweekly — **W2 salary** (RTB House).
2. Monthly **$1,000 Fedwire from "RTB Marketing and Tech Services L3" (Nicosia, Cyprus)**,
   "consulting services rendered" — **B2B / Schedule C income paid to me directly**, NOT
   on the W2. Residual stream: when the consulting arrangement moved to Received Wisdom,
   RTB needed to keep some flowing directly to me. Goes on my Schedule C, not through
   the S Corp — the CPA package should reflect this split on the income side.
3. The rest of the consulting revenue flows to **Received Wisdom** directly.

**Guardrail (amended 2026-07-22):** no write access to RTB House systems. I've added a
**read-only Rydoo MCP connector** (`mcp__Rydoo__*`: list/get expenses, find trips, policy
assistant) — use it to verify submissions landed and track status
(Submitted/PendingApproval → Approved → Reimbursed). It has no create/upload tools, so
**submission still goes through Gmail forward drafts** to the email intake. The policy
assistant returns "Company policy was not found" (not configured company-side) — policy
facts must come from me/HR, not the connector. Like Gmail, the connector is only
available in sessions where it's enabled — scheduled Routine runs won't have it.

## Non-negotiable categorization rules (confirmed by me — don't re-litigate)
1. **Guardian Life** (~$7k/mo whole life) → savings/investment, never insurance expense.
2. **Voya/ReliaStar** → personal term life, no deduction.
3. **ArentFox Schiff** → employment-law legal fees, 100% deductible (not personal legal).
4. **Vehicle:** 50% business-use split applied across the household fleet (4 cars, 2
   business-use) — not per-vehicle. Gas + maintenance tracked under this split.
5. **Beaver Dam** (youth hockey) → no dependent care credit.
6. Auction/vintage/antique platforms → Home/Decorating.
7. People Data Labs, AI software tools, state filing fees, office supplies → deductions.
8. Cavit rent + Compass commission → deductions.
9. Confirmed personal travel, no deduction: London, Costa Rica, DC history competition,
   Boston hockey, Philadelphia ×2, Alaska/PNW.
10. **Alaska trip:** Off the Beaten Path deposit is part of the trip; a second payment
    equal to the deposit is still owed (cash-flow item).
11. Net out **charge reversals** so category totals aren't inflated.

## Classification model
Three tiers — **GREEN** (confirmed deduction) / **YELLOW** (needs review) / **GRAY**
(confirmed personal). Treatment: **IN** (100%), **SPLIT** (pct, e.g. vehicle 50%), or
**NONE**. Unknown vendors default to **YELLOW** — nothing silently lands as personal.
Tier → submission mapping: GREEN + SPLIT feed the monthly CPA package;
`flag=REIMBURSEMENT_OUTSTANDING` feeds the insurance tracker; RTB House-reimbursable
rules (→ Rydoo drafts) don't exist yet — add them to the rulebook as they're confirmed.

**`rules/categorization.yml` is the single rulebook** — vendor/pattern → tier, treatment,
category, flags, watch list. First match wins, order matters (priority flags before the
payment-exclusion block; Zelle is deliberately NOT excluded). Every correction I give in
a session gets encoded there immediately — never as one-off logic. My real-time
corrections are authoritative.

## Pipeline
```bash
pip install pandas openpyxl pyyaml
python3 src/ingest.py          # data/ -> output/all_tx.pkl (idempotent, dedupes)
python3 src/categorize.py      # applies rules/categorization.yml
python3 src/build_workbook.py  # -> output/expenses_workbook_vN.xlsx (GREEN/YELLOW/GRAY tabs)
```
After any workbook build, run recalc verification (LibreOffice headless / Excel) and
confirm zero formula errors before trusting totals. Workbooks are versioned v1, v2, … —
manual analysis ended at v4, automation starts at v5. Formulas, never hardcoded totals.

### Data sources & parsing quirks (verified)
| File pattern | Account | Quirk |
|---|---|---|
| `Chase0781*.CSV` | Chase credit card | sign flip: negative = spend |
| `Chase7618*.CSV` | Chase credit card | sign flip: negative = spend |
| `Chase0928*.CSV` | Chase checking | trailing comma per row → `index_col=False` |
| `AmexPlat_*`, `AmexDelta_*`, `AmexBonvoy_*` (.csv or .xlsx) | Amex Platinum, Delta Reserve, Marriott Bonvoy | positive = spend. xlsx: `header=6` metadata rows; csv: plain header, and multi-member exports carry `Card Member` (Michael vs Evelyn/Carrie — kept in the ledger). **Rename on download** — Amex always exports `activity.<ext>` and the browser's `_N` dedup suffix does not identify the card; ingest refuses unrenamed `activity_N` files. (The two original bare `activity*.xlsx` files from Jan–May were card-verified manually and keep legacy patterns.) |

Ingest matches accounts by filename: Chase defaults are kept as-is (they carry the
account number); Amex files are renamed per the rule above. The monthly download
checklist lives in `inbox/README.md` — five exports (Chase ×3, Amex ×2) of the prior
calendar month, dropped by the 4th for the scan on the 5th.

## Layout
- `inbox/` — drop zone for new exports and receipt files; the scan moves exports to
  `data/` (original filenames) and receipts to `receipts/`.
- `data/` — source exports (Chase CSVs, Amex xlsx).
- `src/`, `rules/` — the pipeline and the rulebook.
- `output/` — workbooks + pickles (pickles gitignored; state persists via
  `all_tx.pkl` → `all_tx_categorized.pkl`).
- `ledger.csv` — **generated** git-diffable export of the categorized frame (don't
  hand-edit; regenerate from `all_tx_categorized.pkl` after each run).
- `receipts/` — receipt files, `YYYY-MM-DD-<merchant>-<amount>.<ext>`, from Gmail or inbox.
- `packages/` — monthly CPA output: `packages/YYYY-MM/` (spreadsheet, receipts, summary.md).
- `open-items.md` — merged action items + setup blockers.

## The scan (each cycle)
1. Ingest `inbox/` (exports → `data/`, receipts → `receipts/`), run ingest + categorize,
   regenerate `ledger.csv`.
2. Gmail sweep for the period's e-receipts; match to transactions where possible.
3. YELLOW review: list unknowns needing a ruling; encode every ruling in the YAML.
4. Rydoo: Gmail forward drafts to `receipts@rydoo.com` for confirmed RTBH reimbursables
   with receipts (drafts only, NEVER send). When the Rydoo connector is available,
   reconcile first: check previously `drafted`/`submitted` items via `list_my_expenses`
   — advance ledger status when an expense appears in Rydoo (that's the proof a draft
   was actually sent) and through PendingApproval/Approved/Reimbursed.
5. CPA package: monthly `packages/YYYY-MM/` from GREEN/SPLIT rows + Gmail draft to the
   CPA once their address is on file (drafts only, NEVER send).
6. Monitors: report watch-list hits (Verizon ×2, storage, streaming, book-summary app),
   Sornik outstanding total, charge reversals netted.
7. Report: totals per tier, deductible net, drafts awaiting send, unknowns, blockers.

## Conventions
- Keep changes scoped to `expenses/`. Never send email — drafts only; a draft is not
  sent until I say so or a sent message is found in Gmail.
- Don't guess classifications — unknowns are YELLOW, and business-vs-personal calls are
  mine (or the CPA's).
- Statements beat receipts on amounts; note discrepancies.
- Flag any dropped-in file carrying full card/account numbers rather than committing it.
- Personal financial data: stays in this private repo, out of anything published.
