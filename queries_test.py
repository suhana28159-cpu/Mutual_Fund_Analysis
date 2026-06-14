"""
Mutual Fund Analytics Project

Author: Suhana Begum

Description:
This script is part of the Bluestock Internship Project.
"""
import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

queries = {

"Top 5 Funds By AUM": """
SELECT
    scheme_name,
    aum_crore
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY aum_crore DESC
LIMIT 5;
""",

"Transactions By State": """
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;
""",

"Average NAV Per Month": """
SELECT
    substr(date,1,7) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;
"""
}

for name, query in queries.items():
    print(f"{name}:\n")
    df = pd.read_sql_query(query, conn)
    print(df)
    print("\n")

conn.close()