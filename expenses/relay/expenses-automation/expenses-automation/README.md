# Expenses Automation

Ports the manual v4 transaction analysis (5 accounts, Jan 1 – May 10, 2026) into a
repeatable pipeline. **Read `CLAUDE.md` first** — it carries all the accumulated context
(tax treatment decisions, parsing quirks, open action items). Claude Code reads it
automatically when working in this repo.

## Quick start

```bash
pip install pandas openpyxl pyyaml
python src/ingest.py          # data/ -> output/all_tx.pkl (idempotent, dedupes)
python src/categorize.py      # applies rules/categorization.yml -> all_tx_categorized.pkl
python src/build_workbook.py  # -> output/expenses_workbook_v5.xlsx (GREEN/YELLOW/GRAY tabs)
```

Then verify the workbook's formulas recalculate cleanly (LibreOffice headless or Excel)
before relying on the totals.

## Adding new statements

Drop new exports into `data/` and rerun. Ingest dedupes on
(date, amount, description, account), so overlapping export windows are safe.
New Amex files auto-increment (`activity_2.xlsx`, …) — add a matching line in
`SOURCES` in `src/ingest.py`.

## The rulebook is the product

`rules/categorization.yml` is the living record of every categorization decision.
When Mike corrects a categorization, encode it there immediately — never as one-off
Python. Unknown vendors default to YELLOW so nothing slips through as personal.
