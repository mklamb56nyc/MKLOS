# Open items — setup

Blockers before the first real cycle can run end-to-end. Each closes by me answering
in a session; record the answer where it belongs (rules.md, CLAUDE.md) and check it off.

## Needed from me
- [ ] **CPA name + email** for the monthly Received Wisdom package. → CLAUDE.md
- [ ] **Rydoo email registration:** confirm which email my Rydoo account is registered
      under. Forwards to `receipts@rydoo.com` must come from a registered address —
      if the account is under my RTB House work email, add `mklamb@gmail.com` as a
      secondary address in Rydoo personal settings (Settings → personal → email
      addresses), since drafts are created in personal Gmail.
- [ ] **Accounts in scope:** which cards/bank accounts to scan, and how I'll get
      statements (CSV export dropped in `inbox/` is best; PDF works). Any card that's
      exclusively business?
- [ ] **First data drop:** last 1–2 months of statements into `inbox/` to seed the
      ledger and start building merchant rules.
- [ ] **RTB House policy basics:** what's reimbursable, any pre-approval/receipt
      thresholds. → rules.md
- [ ] **CPA's preferred package format:** spreadsheet columns, receipt naming, one
      email per month or quarter. → CLAUDE.md / package template

- [ ] **Routine lacks Gmail:** the monthly Routine (`trig_01HG7dn8Pq4NG3SDiWB9yvpF`,
      5th of month 9am ET, fresh session) was created from a session whose connector
      grants couldn't be passed through, so its fired sessions run **without Gmail**
      — they can process `inbox/` and the ledger but can't sweep receipts or create
      drafts. Fix: recreate the routine from the claude.ai Routines UI with the Gmail
      connector attached, then delete this one. Until then, run the scan by asking in
      a Gmail-enabled session.

## Decisions log
- 2026-07-22 — Rydoo intake path chosen: email forwarding to `receipts@rydoo.com`
  (per Rydoo help docs), prepared as Gmail drafts. No direct Rydoo/employer-system
  integration, by design.
- 2026-07-22 — Monthly automated scan created as a scheduled Routine (fires a fresh
  session on the 5th of each month, 9am ET). It degrades gracefully while setup is
  incomplete: reports what it found and what's blocked instead of guessing.
