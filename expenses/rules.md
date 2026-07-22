# Categorization rules

The scan's decision table. Every transaction gets an `entity`: `rtbh` (RTB House /
Rydoo), `rw` (Received Wisdom / CPA package), `personal`, or `unknown` (needs my
ruling). When I rule on an unknown, add the rule here so it never asks again.

**Status: seed file — nothing below is confirmed yet.** The category lists are
common-sense placeholders to react to, not facts. Until I confirm rules, most
transactions will land as `unknown` — that's correct behavior.

## Accounts in scope
(to fill in — see open-items.md)

| Account | Last 4 | Type | Notes |
|---|---|---|---|
| _e.g. Chase Sapphire_ | | credit card | |

## RTB House (`rtbh`)
Reimbursable per RTB House expense policy — submitted via Rydoo.
Typical shape (confirm against actual policy):
- Work travel: flights, hotels, trains, rideshares/taxis for business trips
- Client / business meals
- Conference fees, work events
- (policy specifics — per-diem rules, pre-approval thresholds — go here as learned)

### Merchant rules
| Pattern (statement text) | Rule | Confirmed |
|---|---|---|
| _none yet_ | | |

## Received Wisdom (`rw`)
S Corp expenses — reimbursed by or deducted through the company, packaged monthly
for the CPA. Typical shape (confirm with CPA what belongs here):
- Website/hosting, domains, software subscriptions used for the business
- Business insurance, filing/registration fees
- Professional services (CPA, legal)
- Home office / equipment items **only if the CPA has blessed the treatment**

### Merchant rules
| Pattern (statement text) | Rule | Confirmed |
|---|---|---|
| _none yet_ | | |

## Personal (`personal`)
Everything else. No action, logged only. Recurring known-personal merchants can be
listed here to keep the unknowns list short:

| Pattern | Confirmed |
|---|---|
| _none yet_ | |

## Tie-breakers
- A merchant that could be either business bucket (e.g. travel) classifies by trip
  context — calendar events and email around the transaction date are fair evidence,
  but if still ambiguous, `unknown`.
- Same merchant can have different rules per account (e.g. anything on a card used
  exclusively for RW is `rw` by default) — note that in the Accounts table.
