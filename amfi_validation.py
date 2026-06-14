"""
Mutual Fund Analytics Project

Author: Suhana Begum

Description:
This script is part of the Bluestock Internship Project.
"""
import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("Total AMFI Codes in Fund Master:", len(master_codes))
print("Total AMFI Codes in NAV History:", len(nav_codes))

print("\nMissing Codes:")

if len(missing_codes) == 0:
    print("All AMFI codes are present in NAV history.")
else:
    print(missing_codes)