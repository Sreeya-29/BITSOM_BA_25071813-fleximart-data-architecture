import pandas as pd
import re
from sqlalchemy import create_engine, text
from datetime import datetime

# ---------------- DATABASE CONFIG ----------------
DB_USER = "postgres"
DB_PASSWORD = "290803"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "fleximart"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ---------------- HELPER FUNCTIONS ----------------
def clean_phone(phone):
    if pd.isna(phone):
        return None
    digits = re.sub(r"\D", "", phone)
    if digits.startswith("91"):
        digits = digits[2:]
    if digits.startswith("0"):
        digits = digits[1:]
    return "+91-" + digits

def clean_date(date_val):
    try:
        return pd.to_datetime(date_val, dayfirst=True).date()
    except:
        return None

def standardize_category(cat):
    if pd.isna(cat):
        return None
    return cat.strip().title()

# ---------------- DATA QUALITY REPORT ----------------
report = []

# ---------------- EXTRACT ----------------
import os

# Get the folder where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Read CSVs from the data folder
customers = pd.read_csv(os.path.join(BASE_DIR, "../data/customer_raw.csv"))
products  = pd.read_csv(os.path.join(BASE_DIR, "../data/products_raw.csv"))
sales     = pd.read_csv(os.path.join(BASE_DIR, "../data/sales_raw.csv"))

report.append(f"Customers raw records: {len(customers)}")
report.append(f"Products raw records: {len(products)}")
report.append(f"Sales raw records: {len(sales)}")

# ---------------- TRANSFORM CUSTOMERS ----------------
customers = customers.drop_duplicates(subset=["customer_id"])
customers["email"] = customers["email"].fillna(
    customers["first_name"].str.lower() + "." + customers["last_name"].str.lower() + "@fleximart.com"
)
customers["phone"] = customers["phone"].apply(clean_phone)
customers["registration_date"] = customers["registration_date"].apply(clean_date)

report.append(f"Customers after deduplication: {len(customers)}")

# ---------------- LOAD CUSTOMERS ----------------
customer_map = {}

with engine.begin() as conn:
    for _, row in customers.iterrows():
        result = conn.execute(
            text("""
                INSERT INTO customers (first_name, last_name, email, phone, city, registration_date)
                VALUES (:fn, :ln, :em, :ph, :ct, :rd)
                RETURNING customer_id
            """),
            {
                "fn": row["first_name"],
                "ln": row["last_name"],
                "em": row["email"],
                "ph": row["phone"],
                "ct": row["city"].title(),
                "rd": row["registration_date"]
            }
        )
        customer_map[row["customer_id"]] = result.fetchone()[0]

report.append(f"Customers loaded: {len(customer_map)}")

# ---------------- TRANSFORM PRODUCTS ----------------
products = products.drop_duplicates(subset=["product_id"])
products["category"] = products["category"].apply(standardize_category)
products["price"] = products["price"].fillna(products["price"].median())
products["stock_quantity"] = products["stock_quantity"].fillna(0)
products["product_name"] = products["product_name"].str.strip()

report.append(f"Products after cleaning: {len(products)}")

# ---------------- LOAD PRODUCTS ----------------
product_map = {}

with engine.begin() as conn:
    for _, row in products.iterrows():
        result = conn.execute(
            text("""
                INSERT INTO products (product_name, category, price, stock_quantity)
                VALUES (:pn, :cat, :pr, :sq)
                RETURNING product_id
            """),
            {
                "pn": row["product_name"],
                "cat": row["category"],
                "pr": row["price"],
                "sq": int(row["stock_quantity"])
            }
        )
        product_map[row["product_id"]] = result.fetchone()[0]

report.append(f"Products loaded: {len(product_map)}")

# ---------------- TRANSFORM SALES ----------------
sales = sales.drop_duplicates(subset=["transaction_id"])
sales = sales.dropna(subset=["customer_id", "product_id"])
sales["transaction_date"] = sales["transaction_date"].apply(clean_date)

report.append(f"Sales after cleaning: {len(sales)}")

# ---------------- LOAD ORDERS & ORDER ITEMS ----------------
orders_loaded = 0
items_loaded = 0

with engine.begin() as conn:
    for _, row in sales.iterrows():
        cust_id = customer_map.get(row["customer_id"])
        prod_id = product_map.get(row["product_id"])

        if not cust_id or not prod_id:
            continue

        total_amount = row["quantity"] * row["unit_price"]

        order_result = conn.execute(
            text("""
                INSERT INTO orders (customer_id, order_date, total_amount, status)
                VALUES (:cid, :od, :ta, :st)
                RETURNING order_id
            """),
            {
                "cid": cust_id,
                "od": row["transaction_date"],
                "ta": total_amount,
                "st": row["status"]
            }
        )

        order_id = order_result.fetchone()[0]
        orders_loaded += 1

        conn.execute(
            text("""
                INSERT INTO order_items (order_id, product_id, quantity, unit_price, subtotal)
                VALUES (:oid, :pid, :qty, :up, :sub)
            """),
            {
                "oid": order_id,
                "pid": prod_id,
                "qty": int(row["quantity"]),
                "up": row["unit_price"],
                "sub": total_amount
            }
        )
        items_loaded += 1

report.append(f"Orders loaded: {orders_loaded}")
report.append(f"Order items loaded: {items_loaded}")


print("ETL Pipeline completed successfully.")

# ---------------- DATA QUALITY SUMMARY ----------------
# This section calculates detailed statistics for the data_quality_report.txt

# 1.  Number of records processed per file
records_processed = {
    "customers": len(customers),
    "products": len(products),
    "sales": len(sales)
}

# 2️. Number of duplicates removed
duplicates_removed = {
    "customers": len(customers) - len(customers.drop_duplicates(subset=["customer_id"])),
    "products": len(products) - len(products.drop_duplicates(subset=["product_id"])),
    "sales": len(sales) - len(sales.drop_duplicates(subset=["transaction_id"]))
}

# 3️. Number of missing values handled (only important columns)
missing_values_handled = {
    "customers": customers[["email", "phone", "registration_date"]].isna().sum().sum(),
    "products": products[["price", "stock_quantity", "category"]].isna().sum().sum(),
    "sales": sales[["customer_id", "product_id", "transaction_date"]].isna().sum().sum()
}

# 4️. Number of records loaded successfully (from the maps used in ETL)
records_loaded = {
    "customers": len(customer_map),
    "products": len(product_map),
    "orders": orders_loaded,
    "order_items": items_loaded
}

# ---------------- WRITE TO DATA QUALITY REPORT ----------------
with open("data_quality_report.txt", "w") as f:
    f.write("====== DATA QUALITY REPORT ======\n\n")
    
    f.write("1. Records processed per file:\n")
    for k, v in records_processed.items():
        f.write(f"  {k}: {v}\n")
    f.write("\n")
    
    f.write("2. Duplicates removed:\n")
    for k, v in duplicates_removed.items():
        f.write(f"  {k}: {v}\n")
    f.write("\n")
    
    f.write("3. Missing values handled:\n")
    for k, v in missing_values_handled.items():
        f.write(f"  {k}: {v}\n")
    f.write("\n")
    
    f.write("4. Records loaded successfully:\n")
    for k, v in records_loaded.items():
        f.write(f"  {k}: {v}\n")
    f.write("\n")
    
    f.write("====== END OF REPORT ======\n")

print("Data quality report generated successfully!")

