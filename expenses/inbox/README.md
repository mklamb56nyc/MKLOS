# inbox — drop zone

## The monthly five (drop by the 4th; the scan runs the 5th, 9am ET)
Export the **prior calendar month** (1st–last day) for each account and drop here:

| # | Account | Export | Filename |
|---|---|---|---|
| 1 | Chase 0781 (card) | CSV | keep Chase's default (`Chase0781_Activity…CSV`) |
| 2 | Chase 7618 (card) | CSV | keep Chase's default (`Chase7618_Activity…CSV`) |
| 3 | Chase 0928 (checking) | CSV | keep Chase's default (`Chase0928_Activity…CSV`) |
| 4 | Amex Platinum | xlsx | **rename to** `AmexPlat_YYYY-MM.xlsx` |
| 5 | Amex Delta Reserve | xlsx | **rename to** `AmexDelta_YYYY-MM.xlsx` |

Chase filenames carry the account number, so defaults are fine. **Amex always names
the download `activity.xlsx`** — any `_1`/`_2` suffix is just the browser deduping by
download order, so it says nothing about which card it is. Rename each Amex file right
after download; ingest refuses unrenamed `activity_N.xlsx` files rather than guess the
card. Overlapping date ranges are safe — ingest dedupes.

Receipt photos / PDFs / screenshots can be dropped here any time → they get filed to
`receipts/` as `YYYY-MM-DD-<merchant>-<amount>.<ext>`.

This directory should be empty after a scan (except this README).
