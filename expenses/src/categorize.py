"""Apply rules/categorization.yml to the normalized transaction frame.

Adds: tier (GREEN/YELLOW/GRAY), treatment (IN/SPLIT/NONE), category, deductible_amount,
flag (e.g. REIMBURSEMENT_OUTSTANDING for Sornik), watch (recurring-payment monitor hits).

Charge reversals: refunds (negative normalized amount) are kept and net against spend so
category totals aren't inflated — see the large reversal caught in the manual v4 pass.
"""
import re
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
RULES = ROOT / "rules" / "categorization.yml"
PICKLE_IN = ROOT / "output" / "all_tx.pkl"
PICKLE_OUT = ROOT / "output" / "all_tx_categorized.pkl"


def load_rules(path: Path = RULES) -> dict:
    with open(path) as fh:
        return yaml.safe_load(fh)


def categorize(tx: pd.DataFrame, rules: dict) -> pd.DataFrame:
    tx = tx.copy()
    tx["tier"] = rules["defaults"]["unknown_vendor_tier"]
    tx["treatment"] = "NONE"
    tx["category"] = "Uncategorized"
    tx["split_pct"] = pd.NA
    tx["flag"] = ""
    tx["rule_note"] = ""

    desc = tx["description"].str.lower()
    matched = pd.Series(False, index=tx.index)
    for rule in rules["rules"]:  # first match wins — order in the YAML matters
        mask = desc.str.contains(rule["match"], regex=True, na=False) & ~matched
        matched |= mask
        tx.loc[mask, "tier"] = rule["tier"]
        tx.loc[mask, "treatment"] = rule["treatment"]
        tx.loc[mask, "category"] = rule["category"]
        if rule.get("split_pct") is not None:
            tx.loc[mask, "split_pct"] = rule["split_pct"]
        if rule.get("flag"):
            tx.loc[mask, "flag"] = rule["flag"]
        if rule.get("note"):
            tx.loc[mask, "rule_note"] = rule["note"]

    # Deductible amount: IN = full, SPLIT = pct, FLAT = fixed amount per transaction
    # (e.g. Mike's cell line at $76/mo regardless of the family-plan total), NONE = 0.
    # Refunds net naturally for IN/SPLIT.
    tx["flat_amount"] = pd.NA
    for rule in rules["rules"]:
        if rule.get("flat_amount") is not None:
            mask = desc.str.contains(rule["match"], regex=True, na=False)
            tx.loc[mask & (tx["treatment"] == "FLAT"), "flat_amount"] = rule["flat_amount"]
    tx["deductible_amount"] = 0.0
    m_in = tx["treatment"] == "IN"
    tx.loc[m_in, "deductible_amount"] = tx.loc[m_in, "amount"]
    m_split = (tx["treatment"] == "SPLIT") & tx["split_pct"].notna()
    tx.loc[m_split, "deductible_amount"] = (
        tx.loc[m_split, "amount"] * tx.loc[m_split, "split_pct"].astype(float) / 100
    )
    m_flat = (tx["treatment"] == "FLAT") & tx["flat_amount"].notna()
    tx.loc[m_flat, "deductible_amount"] = tx.loc[m_flat, "flat_amount"].astype(float)

    # Watch list (recurring-payment monitor)
    tx["watch"] = ""
    for w in rules.get("watch_list", []):
        mask = desc.str.contains(w["pattern"], regex=True, na=False)
        tx.loc[mask, "watch"] = w["reason"]

    return tx


if __name__ == "__main__":
    tx = pd.read_pickle(PICKLE_IN)
    out = categorize(tx, load_rules())
    out.to_pickle(PICKLE_OUT)
    print(out.groupby("tier")["amount"].agg(["count", "sum"]).round(2))
    print("\nDeductible (net of refunds):",
          round(out["deductible_amount"].sum(), 2))
    flagged = out[out["flag"] != ""]
    if len(flagged):
        print(f"\n⚠ {len(flagged)} flagged transactions (e.g. Sornik reimbursement outstanding)")
    watched = out[out["watch"] != ""]
    if len(watched):
        print(f"👀 {len(watched)} watch-list hits (Verizon dup / storage / streaming / book app)")
