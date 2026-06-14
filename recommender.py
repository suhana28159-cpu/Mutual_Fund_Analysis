"""
Mutual Fund Analytics Project

Author: Suhana Begum

Description:
This script is part of the Bluestock Internship Project.
"""
import pandas as pd

perf = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

result = perf[
    perf["risk_grade"]
    .str.lower()
    ==
    risk.lower()
]

result = result.sort_values(
    "sharpe_ratio",
    ascending=False
)

print(
    result[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio"
        ]
    ].head(3)
)