import pandas as pd
import os

# ==========================================
# CREATE PROCESSED FOLDER
# ==========================================

os.makedirs("data/processed", exist_ok=True)

print("=" * 60)
print("STARTING DATA CLEANING")
print("=" * 60)

# ==========================================
# 01 FUND MASTER
# ==========================================

print("\nCleaning 01_fund_master.csv")

fund = pd.read_csv("data/raw/01_fund_master.csv")

fund = fund.drop_duplicates()

fund["launch_date"] = pd.to_datetime(
    fund["launch_date"],
    errors="coerce"
)

fund.to_csv(
    "data/processed/01_fund_master_clean.csv",
    index=False
)

print("Saved: 01_fund_master_clean.csv")

# ==========================================
# 02 NAV HISTORY
# ==========================================

print("\nCleaning 02_nav_history.csv")

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav.drop_duplicates()

invalid_nav = nav[
    nav["nav"] <= 0
]

print("Invalid NAV rows:", len(invalid_nav))

nav.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("Saved: 02_nav_history_clean.csv")

# ==========================================
# 03 AUM BY FUND HOUSE
# ==========================================

print("\nCleaning 03_aum_by_fund_house.csv")

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum["date"] = pd.to_datetime(
    aum["date"],
    errors="coerce"
)

aum = aum.drop_duplicates()

aum.to_csv(
    "data/processed/03_aum_by_fund_house_clean.csv",
    index=False
)

print("Saved: 03_aum_by_fund_house_clean.csv")

# ==========================================
# 04 MONTHLY SIP INFLOWS
# ==========================================

print("\nCleaning 04_monthly_sip_inflows.csv")

sip = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

sip = sip.drop_duplicates()

sip.to_csv(
    "data/processed/04_monthly_sip_inflows_clean.csv",
    index=False
)

print("Saved: 04_monthly_sip_inflows_clean.csv")

# ==========================================
# 05 CATEGORY INFLOWS
# ==========================================

print("\nCleaning 05_category_inflows.csv")

category = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

category = category.drop_duplicates()

category.to_csv(
    "data/processed/05_category_inflows_clean.csv",
    index=False
)

print("Saved: 05_category_inflows_clean.csv")

# ==========================================
# 06 INDUSTRY FOLIO COUNT
# ==========================================

print("\nCleaning 06_industry_folio_count.csv")

folio = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

folio = folio.drop_duplicates()

folio.to_csv(
    "data/processed/06_industry_folio_count_clean.csv",
    index=False
)

print("Saved: 06_industry_folio_count_clean.csv")

# ==========================================
# 07 SCHEME PERFORMANCE
# ==========================================

print("\nCleaning 07_scheme_performance.csv")

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

perf = perf.drop_duplicates()

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct",
    "morningstar_rating"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

invalid_expense = perf[
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
]

print(
    "Invalid expense ratio rows:",
    len(invalid_expense)
)

perf.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Saved: 07_scheme_performance_clean.csv")

# ==========================================
# 08 INVESTOR TRANSACTIONS
# ==========================================

print("\nCleaning 08_investor_transactions.csv")

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn = txn.drop_duplicates()

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

invalid_amount = txn[
    txn["amount_inr"] <= 0
]

print(
    "Invalid amount rows:",
    len(invalid_amount)
)

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

invalid_kyc = txn[
    ~txn["kyc_status"].isin(valid_kyc)
]

print(
    "Invalid KYC rows:",
    len(invalid_kyc)
)

txn.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Saved: 08_investor_transactions_clean.csv")

# ==========================================
# 09 PORTFOLIO HOLDINGS
# ==========================================

print("\nCleaning 09_portfolio_holdings.csv")

holdings = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

holdings["portfolio_date"] = pd.to_datetime(
    holdings["portfolio_date"],
    errors="coerce"
)

holdings = holdings.drop_duplicates()

holdings.to_csv(
    "data/processed/09_portfolio_holdings_clean.csv",
    index=False
)

print("Saved: 09_portfolio_holdings_clean.csv")

# ==========================================
# 10 BENCHMARK INDICES
# ==========================================

print("\nCleaning 10_benchmark_indices.csv")

benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"],
    errors="coerce"
)

benchmark = benchmark.drop_duplicates()

benchmark.to_csv(
    "data/processed/10_benchmark_indices_clean.csv",
    index=False
)

print("Saved: 10_benchmark_indices_clean.csv")

# ==========================================
# SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("ALL DATASETS CLEANED SUCCESSFULLY")
print("=" * 60)