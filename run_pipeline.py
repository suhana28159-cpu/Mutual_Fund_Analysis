"""
Master Pipeline Script

Author: Suhana Begum

Runs the main ETL workflow for the Mutual Fund Analytics project.
"""

import subprocess

scripts = [
    "data_ingestion.py",
    "clean_data.py",
    "create_db.py",
    "load_data.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    subprocess.run(["python", script])

print("\nPipeline completed successfully.")