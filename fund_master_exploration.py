import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUNIQUE FUND HOUSES:")
print(df["fund_house"].unique())

print("\nTOTAL FUND HOUSES:")
print(df["fund_house"].nunique())

print("\nCATEGORIES:")
print(df["category"].unique())

print("\nSUB-CATEGORIES:")
print(df["sub_category"].unique())

print("\nRISK CATEGORIES:")
print(df["risk_category"].unique())