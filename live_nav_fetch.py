"""
Mutual Fund Analytics Project

Author: Suhana Begum

Description:
This script is part of the Bluestock Internship Project.
"""
import requests
import pandas as pd

schemes = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"\nChecking {scheme_name} ({scheme_code})")

    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print("Failed to fetch data")
        continue

    try:
        data = response.json()

        df = pd.DataFrame(data["data"])

        filename = f"data/raw/{scheme_name}_NAV.csv"

        df.to_csv(filename, index=False)

        print(f"Saved: {filename}")

    except Exception as e:
        print(f"Error for {scheme_name}: {e}")

print("\nProcess completed.")