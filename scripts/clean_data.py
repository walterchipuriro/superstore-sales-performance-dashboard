import pandas as pd
from pathlib import Path

# Define project paths
RAW_DIR = Path("data/raw")
CLEANED_DIR = Path("data/cleaned")

# Create cleaned folder if it does not exist
CLEANED_DIR.mkdir(parents=True, exist_ok=True)

# Load raw datasets
orders = pd.read_csv(RAW_DIR / "orders.csv")
people = pd.read_csv(RAW_DIR / "people.csv")
returns = pd.read_csv(RAW_DIR / "returns.csv")



# -----------------------------
# Clean orders.csv
# -----------------------------

# Remove extra spaces from column names
orders.columns = orders.columns.str.strip()

# Remove extra spaces from text columns
text_columns = orders.select_dtypes(include="object").columns

for column in text_columns:
    orders[column] = orders[column].astype(str).str.strip()

# Convert date columns to datetime
orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce")
orders["ship_date"] = pd.to_datetime(orders["ship_date"], errors="coerce")

# Convert postal_code to text and handle missing values
orders["postal_code"] = orders["postal_code"].fillna("Unknown")
orders["postal_code"] = orders["postal_code"].astype(str).str.replace(".0", "", regex=False)

# Create new date columns for analysis
orders["order_year"] = orders["order_date"].dt.year
orders["order_month"] = orders["order_date"].dt.month
orders["order_month_name"] = orders["order_date"].dt.month_name()
orders["year_month"] = orders["order_date"].dt.to_period("M").astype(str)

# Create shipping duration column
orders["ship_days"] = (orders["ship_date"] - orders["order_date"]).dt.days

# Create profit margin column
# Note: Dashboard profit margin should still use SUM(profit) / SUM(sales)
orders["profit_margin"] = orders["profit"] / orders["sales"]

# Create loss flag
orders["is_loss"] = orders["profit"].apply(lambda x: "Yes" if x < 0 else "No")





# -----------------------------
# Clean returns.csv
# -----------------------------

returns.columns = returns.columns.str.strip()

for column in returns.select_dtypes(include="object").columns:
    returns[column] = returns[column].astype(str).str.strip()

# Keep unique returned orders only
returns_cleaned = returns.drop_duplicates(subset=["order_id"]).copy()

# Create clear returned flag
returns_cleaned["is_returned"] = "Yes"

# Keep only useful columns
returns_cleaned = returns_cleaned[["order_id", "is_returned"]]




# -----------------------------
# Clean people.csv
# -----------------------------

people.columns = people.columns.str.strip()

for column in people.select_dtypes(include="object").columns:
    people[column] = people[column].astype(str).str.strip()

# Rename person column to regional_manager
people_cleaned = people.rename(columns={"person": "regional_manager"})

# Remove duplicate regions if any
people_cleaned = people_cleaned.drop_duplicates(subset=["region"])





# -----------------------------
# Create final combined dataset
# -----------------------------

# Join orders with returns
sales_cleaned = orders.merge(
    returns_cleaned,
    on="order_id",
    how="left"
)

# Fill non-returned orders
sales_cleaned["is_returned"] = sales_cleaned["is_returned"].fillna("No")

# Join regional manager data
sales_cleaned = sales_cleaned.merge(
    people_cleaned,
    on="region",
    how="left"
)



# -----------------------------
# Save cleaned datasets
# -----------------------------

orders.to_csv(CLEANED_DIR / "orders_cleaned.csv", index=False)
returns_cleaned.to_csv(CLEANED_DIR / "returns_cleaned.csv", index=False)
people_cleaned.to_csv(CLEANED_DIR / "people_cleaned.csv", index=False)
sales_cleaned.to_csv(CLEANED_DIR / "superstore_sales_cleaned.csv", index=False)




# -----------------------------
# Print cleaning summary
# -----------------------------

print("Data cleaning completed successfully.")
print("-----------------------------------")
print(f"Orders rows: {orders.shape[0]}")
print(f"Orders columns: {orders.shape[1]}")
print(f"Returned orders after removing duplicates: {returns_cleaned.shape[0]}")
print(f"People rows: {people_cleaned.shape[0]}")
print(f"Final cleaned dataset rows: {sales_cleaned.shape[0]}")
print(f"Final cleaned dataset columns: {sales_cleaned.shape[1]}")




# Basic data quality checks
print("-----------------------------------")
print("Missing values in final cleaned dataset:")
print(sales_cleaned.isnull().sum())

print("-----------------------------------")
print("Ship date before order date:")
print((sales_cleaned["ship_days"] < 0).sum())

print("-----------------------------------")
print("Negative profit rows:")
print((sales_cleaned["profit"] < 0).sum())