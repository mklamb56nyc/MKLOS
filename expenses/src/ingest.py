"""Ingest bank/card exports into a single normalized transaction frame.

Normalized schema: date, description, amount (positive = spend), account, source_file.
Handles all verified parsing quirks — see CLAUDE.md. Idempotent: dedupes against an
existing pickle by (date, amount, description, account).
"""
import html
import re
from pathlib import Path

import pandas as pd


def clean_desc(s: pd.Series) -> pd.Series:
    """Chase CSVs HTML-escape entities (H&amp;M) — unescape so rules match."""
    return s.astype(str).map(html.unescape).str.strip()

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "output"
PICKLE = OUTPUT_DIR / "all_tx.pkl"


def load_chase_credit(path: Path, account: str) -> pd.DataFrame:
    """Chase credit card CSV. QUIRK: negative = spend, so flip sign."""
    df = pd.read_csv(path)
    out = pd.DataFrame({
        "date": pd.to_datetime(df["Transaction Date"]),
        "description": clean_desc(df["Description"]),
        "amount": -df["Amount"],  # sign flip: spend becomes positive
        "account": account,
        "bank_category": df.get("Category"),
    })
    return out


def load_chase_checking(path: Path, account: str = "Chase0928") -> pd.DataFrame:
    """Chase checking CSV. QUIRK: trailing comma per row -> index_col=False."""
    df = pd.read_csv(path, index_col=False)
    out = pd.DataFrame({
        "date": pd.to_datetime(df["Posting Date"]),
        "description": clean_desc(df["Description"]),
        "amount": -df["Amount"],  # debits are negative in export; spend -> positive
        "account": account,
        "bank_category": df.get("Type"),
    })
    return out


def load_amex(path: Path, account: str) -> pd.DataFrame:
    """Amex export, xlsx or csv. QUIRK: xlsx has 6 metadata rows (header=6); csv has a
    plain Date,Description,Amount header. Positive = spend in both."""
    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    else:
        df = pd.read_excel(path, header=6)
    out = pd.DataFrame({
        "date": pd.to_datetime(df["Date"]),
        "description": clean_desc(df["Description"]),
        "amount": df["Amount"],
        "account": account,
        "bank_category": df.get("Category"),
        "card_member": df.get("Card Member"),  # multi-member CSV exports only
    })
    return out


# filename pattern -> (loader, account label)
# Amex exports all download as "activity.xlsx" (the _1 suffix is the browser's dedup
# rename, tied to download order, NOT the card) — so monthly Amex drops must be renamed
# AmexPlat_*.xlsx / AmexDelta_*.xlsx before ingest. The bare activity patterns remain
# only for the two original Jan-May files whose card mapping was verified manually.
SOURCES = [
    (re.compile(r"Chase0781", re.I), load_chase_credit, "Chase0781"),
    (re.compile(r"Chase7618", re.I), load_chase_credit, "Chase7618"),
    (re.compile(r"Chase0928", re.I), lambda p, a: load_chase_checking(p, a), "Chase0928"),
    (re.compile(r"amex.?plat", re.I), load_amex, "AmexPlatinum"),
    (re.compile(r"amex.?delta", re.I), load_amex, "AmexDeltaReserve"),
    (re.compile(r"amex.?bonvoy", re.I), load_amex, "AmexBonvoy"),
    (re.compile(r"^activity\.xlsx$", re.I), load_amex, "AmexPlatinum"),
    (re.compile(r"^activity_1\.xlsx$", re.I), load_amex, "AmexDeltaReserve"),
]


def check_no_unrenamed_amex(data_dir: Path) -> None:
    """Refuse bare activity_N.xlsx beyond the two verified originals — card unknown."""
    strays = [f.name for f in data_dir.iterdir()
              if re.match(r"^activity_[2-9]\d*\.xlsx$", f.name, re.I)]
    if strays:
        raise SystemExit(
            f"Unidentifiable Amex export(s) {strays}: the activity_N name comes from "
            "browser download order, not the card. Rename to AmexPlat_YYYY-MM.xlsx or "
            "AmexDelta_YYYY-MM.xlsx and rerun."
        )


def safe_sheet_name(s: str) -> str:
    """Excel-legal sheet name: strip illegal chars, cap at 31."""
    return re.sub(r"[\\/*?:\[\]]", "", s)[:31]


def ingest(data_dir: Path = DATA_DIR, pickle_path: Path = PICKLE) -> pd.DataFrame:
    check_no_unrenamed_amex(data_dir)
    frames = []
    for f in sorted(data_dir.iterdir()):
        for pattern, loader, account in SOURCES:
            if pattern.search(f.name):
                frames.append(loader(f, account).assign(source_file=f.name))
                break
    if not frames:
        raise SystemExit(f"No recognized source files in {data_dir}")
    tx = pd.concat(frames, ignore_index=True)

    # Idempotent merge against prior state
    if pickle_path.exists():
        prior = pd.read_pickle(pickle_path)
        combined = pd.concat([prior, tx], ignore_index=True)
    else:
        combined = tx
    combined = combined.drop_duplicates(
        subset=["date", "amount", "description", "account"], keep="first"
    ).sort_values("date").reset_index(drop=True)

    OUTPUT_DIR.mkdir(exist_ok=True)
    combined.to_pickle(pickle_path)
    return combined


if __name__ == "__main__":
    tx = ingest()
    print(f"{len(tx)} transactions | {tx['date'].min():%Y-%m-%d} -> {tx['date'].max():%Y-%m-%d}")
    print(tx.groupby("account")["amount"].agg(["count", "sum"]).round(2))
