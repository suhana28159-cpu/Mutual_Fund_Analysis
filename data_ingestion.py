import pandas as pd
import os

folder_path = "data/raw"

files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

print(f"Found {len(files)} CSV files")

for file in files:

    print("\n" + "="*70)
    print("FILE:", file)
    print("="*70)

    file_path = os.path.join(folder_path, file)

    df = pd.read_csv(file_path)

    print("\nSHAPE:")
    print(df.shape)

    print("\nDATA TYPES:")
    print(df.dtypes)

    print("\nFIRST 5 ROWS:")
    print(df.head())

    print("\nMISSING VALUES:")
    print(df.isnull().sum())

    print("\nDUPLICATE ROWS:")
    print(df.duplicated().sum())

print("\nAll datasets loaded successfully!")