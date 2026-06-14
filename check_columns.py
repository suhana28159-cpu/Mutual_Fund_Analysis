"""
Mutual Fund Analytics Project

Author: Suhana Begum

Description:
This script is part of the Bluestock Internship Project.
"""
import pandas as pd

files = [
    "data/raw/03_aum_by_fund_house.csv",
    "data/raw/04_monthly_sip_inflows.csv",
    "data/raw/05_category_inflows.csv",
    "data/raw/06_industry_folio_count.csv",
    "data/raw/09_portfolio_holdings.csv",
    "data/raw/10_benchmark_indices.csv"
]

for file in files:
    print("\n" + "="*60)
    print(file)

    df = pd.read_csv(file)

    print(df.columns.tolist())
    print(df.head(2))