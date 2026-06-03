-- =====================================================
-- 1. Top 5 Funds by AUM
-- =====================================================

SELECT
    scheme_name,
    aum_crore
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY aum_crore DESC
LIMIT 5;


-- =====================================================
-- 2. Average NAV Per Month
-- =====================================================

SELECT
    substr(date,1,7) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- =====================================================
-- 3. SIP YoY Growth Trend
-- =====================================================

SELECT
    month,
    yoy_growth_pct
FROM fact_sip_inflows
ORDER BY month;


-- =====================================================
-- 4. Transactions By State
-- =====================================================

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- =====================================================
-- 5. Funds With Expense Ratio Less Than 1%
-- =====================================================

SELECT
    scheme_name,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- =====================================================
-- 6. Top 10 Performing Funds (1 Year Return)
-- =====================================================

SELECT
    df.scheme_name,
    fp.return_1yr_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY fp.return_1yr_pct DESC
LIMIT 10;


-- =====================================================
-- 7. Category Wise Net Inflows
-- =====================================================

SELECT
    category,
    ROUND(SUM(net_inflow_crore),2) AS total_inflow
FROM fact_category_inflows
GROUP BY category
ORDER BY total_inflow DESC;


-- =====================================================
-- 8. Top Sectors By Portfolio Weight
-- =====================================================

SELECT
    sector,
    ROUND(SUM(weight_pct),2) AS total_weight
FROM fact_portfolio_holdings
GROUP BY sector
ORDER BY total_weight DESC;


-- =====================================================
-- 9. Fund Houses By Average AUM
-- =====================================================

SELECT
    fund_house,
    ROUND(AVG(aum_crore),2) AS avg_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY avg_aum DESC;


-- =====================================================
-- 10. Benchmark Index Average Close Value
-- =====================================================

SELECT
    index_name,
    ROUND(AVG(close_value),2) AS avg_close
FROM fact_benchmark_indices
GROUP BY index_name
ORDER BY avg_close DESC;