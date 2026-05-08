USE superstore_sales_db;

-- =====================================================
-- DATA QUALITY CHECKS
-- Project: Superstore Sales Performance Dashboard
-- Purpose: Validate imported cleaned data before analysis
-- =====================================================

-- 1. Check total number of rows
SELECT 
    COUNT(*) AS total_rows
FROM superstore_sales_cleaned;

-- 2. Check total unique orders
SELECT 
    COUNT(DISTINCT order_id) AS total_orders
FROM superstore_sales_cleaned;

-- 3. Check total unique customers
SELECT 
    COUNT(DISTINCT customer_id) AS total_customers
FROM superstore_sales_cleaned;

-- 4. Check total unique products
SELECT 
    COUNT(DISTINCT product_id) AS total_products
FROM superstore_sales_cleaned;

-- 5. Check date range
SELECT 
    MIN(order_date) AS first_order_date,
    MAX(order_date) AS last_order_date
FROM superstore_sales_cleaned;

-- 6. Check missing important fields
SELECT 
    SUM(CASE WHEN order_id IS NULL OR order_id = '' THEN 1 ELSE 0 END) AS missing_order_id,
    SUM(CASE WHEN order_date IS NULL THEN 1 ELSE 0 END) AS missing_order_date,
    SUM(CASE WHEN customer_id IS NULL OR customer_id = '' THEN 1 ELSE 0 END) AS missing_customer_id,
    SUM(CASE WHEN product_id IS NULL OR product_id = '' THEN 1 ELSE 0 END) AS missing_product_id,
    SUM(CASE WHEN sales IS NULL THEN 1 ELSE 0 END) AS missing_sales,
    SUM(CASE WHEN profit IS NULL THEN 1 ELSE 0 END) AS missing_profit
FROM superstore_sales_cleaned;

-- 7. Check unknown postal codes
SELECT 
    COUNT(*) AS unknown_postal_codes
FROM superstore_sales_cleaned
WHERE postal_code = 'Unknown';

-- 8. Check invalid shipping dates
SELECT 
    COUNT(*) AS invalid_shipping_dates
FROM superstore_sales_cleaned
WHERE ship_date < order_date;

-- 9. Check negative sales values
SELECT 
    COUNT(*) AS negative_sales_rows
FROM superstore_sales_cleaned
WHERE sales < 0;

-- 10. Check negative profit rows
SELECT 
    COUNT(*) AS loss_making_rows
FROM superstore_sales_cleaned
WHERE profit < 0;

-- 11. Check returned order rows
SELECT 
    is_returned,
    COUNT(*) AS total_rows
FROM superstore_sales_cleaned
GROUP BY is_returned;

-- 12. Check available regions
SELECT 
    region,
    COUNT(*) AS total_rows
FROM superstore_sales_cleaned
GROUP BY region
ORDER BY total_rows DESC;

-- 13. Check available categories
SELECT 
    category,
    COUNT(*) AS total_rows
FROM superstore_sales_cleaned
GROUP BY category
ORDER BY total_rows DESC;

-- 14. Check regional managers
SELECT 
    region,
    regional_manager,
    COUNT(*) AS total_rows
FROM superstore_sales_cleaned
GROUP BY region, regional_manager
ORDER BY region;