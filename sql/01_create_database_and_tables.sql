CREATE DATABASE IF NOT EXISTS superstore_sales_db;

USE superstore_sales_db;

DROP TABLE IF EXISTS superstore_sales_cleaned;

CREATE TABLE superstore_sales_cleaned (
    row_id INT,
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(100),
    customer_id VARCHAR(50),
    customer_name VARCHAR(255),
    segment VARCHAR(100),
    country VARCHAR(100),
    city VARCHAR(150),
    state VARCHAR(150),
    postal_code VARCHAR(50),
    region VARCHAR(100),
    product_id VARCHAR(100),
    category VARCHAR(100),
    sub_category VARCHAR(100),
    product_name TEXT,
    sales DECIMAL(12, 2),
    quantity INT,
    discount DECIMAL(5, 2),
    profit DECIMAL(12, 2),
    order_year INT,
    order_month INT,
    order_month_name VARCHAR(20),
    year_month VARCHAR(20),
    ship_days INT,
    profit_margin DECIMAL(12, 6),
    is_loss VARCHAR(10),
    is_returned VARCHAR(10),
    regional_manager VARCHAR(150)
); 