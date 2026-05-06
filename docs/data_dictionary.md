# Data Dictionary

## Project: Sales Performance Dashboard

This document explains the datasets used in the Sales Performance Dashboard project.

---

## 1. orders.csv

This is the main dataset. It contains sales transaction records from the Superstore business. Each row represents one product line in an order. One order can have more than one row if the customer bought multiple products.

| Column | Description |
|---|---|
| row_id | Unique row number for each record |
| order_id | Unique ID for each customer order |
| order_date | Date when the order was placed |
| ship_date | Date when the order was shipped |
| ship_mode | Shipping method used for the order |
| customer_id | Unique ID for each customer |
| customer_name | Name of the customer |
| segment | Type of customer, such as Consumer, Corporate, or Home Office |
| country | Country where the order was placed |
| city | City where the customer is located |
| state | State where the customer is located |
| postal_code | Postal code of the customer location |
| region | Sales region |
| product_id | Unique ID for each product |
| category | Main product category |
| sub_category | Product sub-category |
| product_name | Name of the product |
| sales | Revenue generated from the sale |
| quantity | Number of units sold |
| discount | Discount given on the sale |
| profit | Profit made from the sale |

---

## 2. returns.csv

This dataset contains orders that were returned by customers.

| Column | Description |
|---|---|
| returned | Shows whether the order was returned |
| order_id | ID of the returned order |

---

## 3. people.csv

This dataset contains regional managers responsible for each sales region.

| Column | Description |
|---|---|
| person | Name of the regional manager |
| region | Sales region managed by the person |

---

## Key Business Metrics

| Metric | Formula / Meaning |
|---|---|
| Total Sales | Sum of sales |
| Total Profit | Sum of profit |
| Total Quantity Sold | Sum of quantity |
| Total Orders | Count of unique order_id |
| Total Customers | Count of unique customer_id |
| Profit Margin | Total Profit divided by Total Sales |
| Return Rate | Returned Orders divided by Total Orders |
| Average Order Value | Total Sales divided by Total Orders |

---

## Notes

- Negative profit values are not treated as errors. They show sales where the business made a loss.
- Missing postal codes can be handled as Unknown or left blank because location analysis can still use city, state, and region.
- The returns dataset may contain duplicate order IDs, so it should be cleaned before analysis.