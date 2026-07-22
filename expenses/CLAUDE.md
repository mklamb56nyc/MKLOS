# expenses — project context

## What this is
Automated expense identification and submission prep. A regular scan of card/bank
statements, Gmail receipts, and dropped-in files sorts spending into two buckets and
preps each for its destination:

1. **RTB House** (W2 employer) — reimbursable business expenses. Destination is
   **Rydoo**, via its email intake: receipts forwarded as attachments to
   `receipts@rydoo.com` from a registered email address create expenses automatically
   (one expense per attachment). The seamless path: Claude prepares **Gmail forward
   drafts** with the receipt attached; I review and hit send. Rydoo help:
   [Forward a receipt via email](https://help.rydoo.com/hc/en-be/articles/8139189477660-Forward-a-receipt-via-email).
2. **Received Wisdom** (my S Corp) — expenses to be reimbursed by / deducted through
   the S Corp. Destination is a **monthly submission package** (itemized spreadsheet +
   receipts + summary) that I email to my CPA. Claude drafts that email too (in my
   voice per `/VOICE.md`).

Everything else is **personal** — logged in the ledger for completeness but no action.

**Guardrail:** this repo never connects to RTB House systems. No Rydoo credentials or
API — the only touchpoint is drafts in my own Gmail. That keeps the employer-separation
rule in the root `CLAUDE.md` intact.

## Layout
- `rules.md` — categorization rules: which merchants/patterns map to RTBH vs RW vs
  personal. **The scan's brain.** Grows as I confirm classifications; when unsure,
  the scan asks instead of guessing.
- `inbox/` — drop zone. I put new statement exports (CSV preferred, PDF fine) and
  receipt photos/PDFs here; the scan consumes them and files them.
- `statements/` — processed statement files, archived as `YYYY-MM-<account>.<ext>`.
- `receipts/` — receipt files, named `YYYY-MM-DD-<merchant>-<amount>.<ext>`, matched
  to ledger rows.
- `ledger.csv` — the running record of every classified transaction. Columns are
  documented in the header; `status` tracks each item from `identified` →
  `drafted`/`packaged` → `submitted` → `reimbursed`.
- `packages/` — monthly Received Wisdom output: `packages/YYYY-MM/` with
  `expenses.xlsx` (or csv), copies of that month's RW receipts, and `summary.md`.
- `open-items.md` — setup questions and unresolved classifications.

## The scan (each cycle)
1. **Ingest** anything in `inbox/`: parse statements into transactions, file receipts.
2. **Gmail sweep** for the period: e-receipts, order confirmations, travel bookings —
   match them to statement transactions where possible (a receipt without a statement
   line, or vice versa, is still logged).
3. **Classify** every new transaction per `rules.md`. Unknowns go in the ledger as
   `entity=unknown` and get listed for me to rule on; rulings get added to `rules.md`
   so the same merchant never asks twice.
4. **RTB House output:** for each new RTBH expense with a receipt, create a Gmail
   draft to `receipts@rydoo.com` with the receipt attached (one draft can carry
   several attachments — Rydoo splits them into separate expenses). Mark `drafted`.
5. **Received Wisdom output:** monthly, build `packages/YYYY-MM/` and a Gmail draft
   to my CPA with the package attached. Mark `packaged`.
6. **Report:** a short summary — counts and totals per bucket, unknowns needing a
   ruling, missing receipts, drafts awaiting send.

## Conventions
- Keep changes scoped to this `expenses/` directory.
- **Never send email** — drafts only, always. Never assume a draft was sent; `status`
  moves to `submitted` only when I say so or a sent message is found in Gmail.
- **Don't invent classifications.** A merchant not covered by `rules.md` is `unknown`,
  not a guess. Business-vs-personal is a judgment call that's mine (or the CPA's).
- Amounts come from statements, not receipts, when both exist and disagree — note the
  discrepancy.
- Statement files and receipts may contain full card numbers or account numbers —
  they shouldn't, but if a dropped-in file does, flag it rather than committing it.
- This is personal financial data: it stays in this private repo and out of anything
  published or shared.
