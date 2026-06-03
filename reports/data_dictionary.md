# Data Dictionary

## Source Files

| Source File                  | Description                                  |
| ---------------------------- | -------------------------------------------- |
| 01_fund_master.csv           | Master information about mutual fund schemes |
| 02_nav_history.csv           | Historical NAV data                          |
| 03_aum_by_fund_house.csv     | Assets Under Management by fund house        |
| 04_monthly_sip_inflows.csv   | Monthly SIP statistics                       |
| 05_category_inflows.csv      | Category-wise inflows                        |
| 06_industry_folio_count.csv  | Industry folio statistics                    |
| 07_scheme_performance.csv    | Scheme performance metrics                   |
| 08_investor_transactions.csv | Investor transaction records                 |
| 09_portfolio_holdings.csv    | Scheme portfolio holdings                    |
| 10_benchmark_indices.csv     | Benchmark index data                         |

---

# dim_fund

| Column            | Data Type | Business Definition           |
| ----------------- | --------- | ----------------------------- |
| amfi_code         | INTEGER   | Unique AMFI scheme identifier |
| scheme_name       | TEXT      | Mutual fund scheme name       |
| fund_house        | TEXT      | Asset management company      |
| category          | TEXT      | Scheme category               |
| sub_category      | TEXT      | Scheme sub-category           |
| plan              | TEXT      | Direct or Regular plan        |
| launch_date       | DATE      | Scheme launch date            |
| benchmark         | TEXT      | Benchmark index               |
| expense_ratio_pct | REAL      | Expense ratio percentage      |
| exit_load_pct     | REAL      | Exit load percentage          |
| fund_manager      | TEXT      | Fund manager name             |
| risk_category     | TEXT      | Risk classification           |

---

# fact_nav

| Column    | Data Type | Business Definition |
| --------- | --------- | ------------------- |
| amfi_code | INTEGER   | Scheme identifier   |
| date      | DATE      | NAV date            |
| nav       | REAL      | Net Asset Value     |

---

# fact_aum

| Column         | Data Type | Business Definition       |
| -------------- | --------- | ------------------------- |
| date           | DATE      | Reporting date            |
| fund_house     | TEXT      | Fund house name           |
| aum_lakh_crore | REAL      | AUM in lakh crore         |
| aum_crore      | REAL      | AUM in crore rupees       |
| num_schemes    | INTEGER   | Number of schemes managed |

---

# fact_sip_inflows

| Column                    | Data Type | Business Definition              |
| ------------------------- | --------- | -------------------------------- |
| month                     | TEXT      | Reporting month                  |
| sip_inflow_crore          | REAL      | SIP inflow amount                |
| active_sip_accounts_crore | REAL      | Active SIP accounts              |
| new_sip_accounts_lakh     | REAL      | New SIP accounts opened          |
| sip_aum_lakh_crore        | REAL      | SIP assets under management      |
| yoy_growth_pct            | REAL      | Year-over-year growth percentage |

---

# fact_category_inflows

| Column           | Data Type | Business Definition |
| ---------------- | --------- | ------------------- |
| month            | TEXT      | Reporting month     |
| category         | TEXT      | Fund category       |
| net_inflow_crore | REAL      | Net inflow amount   |

---

# fact_folio_count

| Column              | Data Type | Business Definition |
| ------------------- | --------- | ------------------- |
| month               | TEXT      | Reporting month     |
| total_folios_crore  | REAL      | Total folios        |
| equity_folios_crore | REAL      | Equity folios       |
| debt_folios_crore   | REAL      | Debt folios         |
| hybrid_folios_crore | REAL      | Hybrid folios       |
| others_folios_crore | REAL      | Other folios        |

---

# fact_performance

| Column             | Data Type | Business Definition      |
| ------------------ | --------- | ------------------------ |
| amfi_code          | INTEGER   | Scheme identifier        |
| scheme_name        | TEXT      | Scheme name              |
| fund_house         | TEXT      | Fund house               |
| category           | TEXT      | Fund category            |
| plan               | TEXT      | Plan type                |
| return_1yr_pct     | REAL      | 1-year return percentage |
| return_3yr_pct     | REAL      | 3-year return percentage |
| return_5yr_pct     | REAL      | 5-year return percentage |
| benchmark_3yr_pct  | REAL      | Benchmark return         |
| alpha              | REAL      | Alpha measure            |
| beta               | REAL      | Beta measure             |
| sharpe_ratio       | REAL      | Sharpe ratio             |
| sortino_ratio      | REAL      | Sortino ratio            |
| std_dev_ann_pct    | REAL      | Annualized volatility    |
| max_drawdown_pct   | REAL      | Maximum drawdown         |
| aum_crore          | REAL      | Assets under management  |
| expense_ratio_pct  | REAL      | Expense ratio            |
| morningstar_rating | INTEGER   | Morningstar rating       |
| risk_grade         | TEXT      | Risk grade               |

---

# fact_transactions

| Column             | Data Type | Business Definition        |
| ------------------ | --------- | -------------------------- |
| investor_id        | TEXT      | Investor identifier        |
| transaction_date   | DATE      | Transaction date           |
| amfi_code          | INTEGER   | Scheme identifier          |
| transaction_type   | TEXT      | SIP / Lumpsum / Redemption |
| amount_inr         | REAL      | Transaction amount         |
| state              | TEXT      | Investor state             |
| city               | TEXT      | Investor city              |
| city_tier          | TEXT      | City classification        |
| age_group          | TEXT      | Investor age group         |
| gender             | TEXT      | Investor gender            |
| annual_income_lakh | REAL      | Annual income              |
| payment_mode       | TEXT      | Mode of payment            |
| kyc_status         | TEXT      | KYC verification status    |

---

# fact_portfolio_holdings

| Column            | Data Type | Business Definition         |
| ----------------- | --------- | --------------------------- |
| amfi_code         | INTEGER   | Scheme identifier           |
| stock_symbol      | TEXT      | Stock symbol                |
| stock_name        | TEXT      | Stock name                  |
| sector            | TEXT      | Industry sector             |
| weight_pct        | REAL      | Portfolio weight percentage |
| market_value_cr   | REAL      | Market value in crore       |
| current_price_inr | REAL      | Current stock price         |
| portfolio_date    | DATE      | Portfolio reporting date    |

---

# fact_benchmark_indices

| Column      | Data Type | Business Definition  |
| ----------- | --------- | -------------------- |
| date        | DATE      | Trading date         |
| index_name  | TEXT      | Benchmark index name |
| close_value | REAL      | Closing index value  |
