# inbox — drop zone

Put new files here; the scan consumes and files them:
- **Statement exports** (Chase CSV, Amex xlsx) → moved to `data/` **keeping their
  original filenames** — ingest recognizes accounts by filename pattern. New Amex
  files need a `SOURCES` line in `src/ingest.py`.
- **Receipt photos / PDFs / screenshots** → `receipts/`, renamed
  `YYYY-MM-DD-<merchant>-<amount>.<ext>`.

This directory should be empty after a scan (except this README).
