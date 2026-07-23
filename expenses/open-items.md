# Open items

Merged 2026-07-22 from the drained expenses-automation relay + new-project setup.
Close items by answering in a session; record answers where they belong
(`CLAUDE.md`, `rules/categorization.yml`) and check off here.

## From the earlier analysis (relay) — action items
- [ ] **Sornik reimbursement (top priority):** recurring payments never submitted for
      insurance reimbursement — 7 flagged transactions in the current ledger. Flag stays
      on every payment until I confirm submission.
- [ ] **Verizon — three relationships (confirmed by Mike 2026-07-22),** so the old
      "two simultaneous accounts / consolidate" item is resolved as intentional:
      1. **Business Fios, 111 South St Oyster Bay** — RW's account, $170.55/mo,
         auto-pay, bills in `receipts/`. Done.
      2. **Verizon Wireless** — July bill received 2026-07-22, filed as
         `receipts/2026-07-13-verizon-wireless-279.64.pdf`. Facts from the bill:
         account 686669080-00001 is **in Carrie's name (Evelyn Lamb)**, $279.64/mo,
         auto-pay from the 0928 checking (matches the monthly `VERIZON WIRELESS
         PAYMENTS` ACH). Six devices = the whole family: iPhone 13 Mini
         516-401-5452 $31.99 · iPhone 13 516-680-5506 $49.07 · iPhone SE
         917-387-6510 $48.93 · iPhone 15 Pro 917-434-3967 $63.96 (+ Watch SE
         number-share $9.15) · **iPhone 17 Pro 917-816-8443 $76.54 = Mike's line**
         (confirmed 2026-07-22; also in root CLAUDE.md). Mike intends to expense
         this to RW. **Pending before the rule goes GREEN: the CPA's call on
         treatment** — full account ($279.64) vs Mike's line (~$76.54) vs a
         percentage; account being in Carrie's name and covering the kids' lines
         makes full-account treatment the aggressive option (same "CPA has blessed
         it" bar as home office).
      3. **Home FiOS internet** — presumably the VERIZONRECURRING $89.99/mo on the
         Delta card; the one relevant to RTB's flat-rate internet reimbursement
         (only the excess above the flat rate is deduction-relevant). Confirm the
         $89.99 is it.
- [ ] **Streaming service** redundancy check.
- [ ] **Storage unit** duplication check.
- [ ] Unrecognized **book-summary app** subscription — identify and cancel.
- [ ] Second **Alaska/PNW** payment (equal to the Off the Beaten Path deposit) still
      due — cash-flow item.
- [ ] Ongoing vehicle gas/maintenance tracking at the 50% household split.
- [ ] **YELLOW backlog:** 2,299 of 2,540 transactions uncategorized (expected — young
      rulebook). Work down in review sessions; every ruling becomes a YAML rule.
- [ ] **Catch-up exports (May 1 – Jun 30), 2026-07-22:** received and ingested Chase
      7618 ✓, Chase 0928 ✓, Amex Platinum ✓, Amex Delta Reserve ✓, plus a **new sixth
      account: Amex Marriott Bonvoy** ✓ (mostly recurring TWO BY FOUR $106.80 charges).
      Still missing: **Chase 0781** — that card still ends 2026-05-06. Sornik flags now
      11 (4 new in May–June).

## Setup — needed from me
- [ ] **CPA name + email** for the monthly Received Wisdom package. → CLAUDE.md
- [x] **RTB entities — resolved 2026-07-22:** two real streams. W2 payroll from RTB
      House ($9,560.44 biweekly ACH) + monthly $1,000 Cyprus wire from RTB Marketing
      and Tech Services = **B2B/Schedule C income paid to Mike directly, not W2** —
      a residual stream kept direct when the consulting arrangement moved to Received
      Wisdom. Recorded in CLAUDE.md (income streams) and the rulebook.
- [ ] **Rydoo email registration:** confirm which address the Rydoo account is under;
      forwards to `receipts@rydoo.com` must come from a registered address. If it's the
      work email, add `mklamb@gmail.com` as a secondary in Rydoo personal settings
      (drafts are created in personal Gmail).
- [ ] **RTB House reimbursable rules:** none in the rulebook yet (only the flat-rate
      internet fact). What's reimbursable, receipt/pre-approval thresholds. → YAML
      (2026-07-22: tried Rydoo's policy assistant via the new connector — "Company
      policy was not found", not configured company-side, so this needs a human answer.)
- [ ] **CPA's preferred package format:** columns, receipt naming, monthly vs quarterly.
- [ ] **Routine lacks Gmail:** the monthly Routine (`trig_01HG7dn8Pq4NG3SDiWB9yvpF`,
      5th of month 9am ET, fresh session) fires sessions **without the Gmail connector**
      (grants couldn't be passed through at creation). Those runs can do the pipeline and
      ledger but not receipt sweeps or drafts. Fix: recreate the routine from the
      claude.ai Routines UI with Gmail attached, then delete this one. Until then, ask
      for a scan in a Gmail-enabled session.

## Decisions log
- 2026-07-22 — **Bank feeds: sticking with manual downloads.** Considered OpenBudget.sh
  (hosted read-only MCP over Plaid) for live Chase/Amex transaction feeds; Mike decided
  against for now — young third party holding full transaction history, plus rulebook
  regexes and ingest dedupe are keyed to raw statement descriptions. Statement CSV/xlsx
  exports dropped into `inbox/` remain the source of record. Revisit if the manual
  export step becomes the bottleneck.
- 2026-07-22 — **Rydoo write-path research:** the MCP connector is confirmed read-only
  (its fifth tool, submit_feedback, only sends feedback to Rydoo's team). A real write
  API exists (REST v2, OAuth2 client-credentials via accounts.rydoo.com) but access is
  **Enterprise-only and credentials are issued at the company level** (customer success
  manager / api@rydoo.com) — i.e., an RTB House tenant integration, not something an
  individual employee gets. Ruled out for this project: it would put employer-tenant
  credentials into personal automation (violates both the employer-separation and
  no-secrets guardrails). **Email intake stays the submission path**; if richer
  automation is ever wanted, the ask goes to RTB House finance/IT, not here.
- 2026-07-22 — **Read-only Rydoo MCP connector added** by Mike (list/get expenses,
  find trips, policy assistant; no write tools). Guardrail amended in CLAUDE.md:
  status verification via connector, submission still via Gmail email-intake drafts.
  Verified live: one expense visible last 30 days (Gold Coast Mailroom, $285.71,
  2026-07-09, submitted with receipt, pending approval). Scheduled Routine runs won't
  have this connector (same grant-passing limit as Gmail).
- 2026-07-22 — Relay drained and deleted: pipeline (`src/`, `rules/`, `data/`,
  workbook v5) moved into `expenses/`, context merged into `CLAUDE.md`. Earlier
  project's YAML rulebook kept as the single rulebook (scaffold's `rules.md` removed);
  `ledger.csv` is now a generated export of the categorized frame (1,904 tx,
  2025-12-30 → 2026-05-08; pipeline re-run verified 2026-07-22).
- 2026-07-22 — Rydoo intake path: email forwarding to `receipts@rydoo.com` (per Rydoo
  help docs), prepared as Gmail drafts. No direct Rydoo/employer-system integration,
  by design.
- 2026-07-22 — Monthly automated scan created as a scheduled Routine (fresh session,
  5th of each month, 9am ET). Degrades gracefully while setup is incomplete.
