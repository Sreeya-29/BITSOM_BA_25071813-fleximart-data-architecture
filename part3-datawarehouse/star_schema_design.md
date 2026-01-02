# Star Schema Design Documentation

## Section 1: Schema Overview

### FACT TABLE: fact_sales

**Grain:**  
One row per product per order line item. Each row represents a single product sold in a single customer order.

**Business Process:**  
Sales transactions capturing customer purchases.

**Measures (Numeric Facts):**
- quantity_sold: Number of units sold
- unit_price: Price per unit at the time of sale
- discount_amount: Discount applied to the product
- total_amount: Final sales amount calculated as (quantity_sold × unit_price − discount_amount)

**Foreign Keys:**
- date_key → dim_date
- product_key → dim_product
- customer_key → dim_customer

---

### DIMENSION TABLE: dim_date

**Purpose:**  
Provides date-related information to support time-based sales analysis.

**Type:**  
Conformed dimension used consistently across analytical reports.

**Attributes:**
- date_key (PK): Surrogate key in YYYYMMDD integer format
- full_date: Actual calendar date
- day_of_week: Name of the day (Monday, Tuesday, etc.)
- month: Month number (1–12)
- month_name: Name of the month (January, February, etc.)
- quarter: Quarter of the year (Q1, Q2, Q3, Q4)
- year: Year value (e.g., 2023, 2024)
- is_weekend: Boolean flag indicating weekend

---

### DIMENSION TABLE: dim_product

**Purpose:**  
Stores descriptive information about products.

**Attributes:**
- product_key (PK): Surrogate key
- product_id: Original product identifier from source system
- product_name: Name of the product
- category: Product category (Electronics, Clothing, etc.)
- subcategory: Sub-category of the product
- brand: Brand or manufacturer name

---

### DIMENSION TABLE: dim_customer

**Purpose:**  
Stores descriptive customer information for analysis.

**Attributes:**
- customer_key (PK): Surrogate key
- customer_id: Original customer identifier
- customer_name: Full name of the customer
- city: City of residence
- state: State of residence
- country: Country of residence

---

## Section 2: Design Decisions

The granularity of the fact table is defined at the transaction line-item level to ensure the highest level of detail is captured. This allows the business to analyze sales data at multiple levels such as product, customer, and date without losing important information. Aggregated insights like daily, monthly, and yearly sales can easily be derived from this detailed data.

Surrogate keys are used instead of natural keys because they improve performance and maintain consistency within the data warehouse. Natural keys from source systems may change over time or may not be unique, whereas surrogate keys are stable and system-generated.

This star schema design supports drill-down and roll-up operations efficiently. Analysts can drill down from yearly sales to quarterly, monthly, and daily sales using the date dimension. Roll-up operations allow summarization of data by product category, city, or customer group, enabling flexible and fast analytical reporting.

---

## Section 3: Sample Data Flow

**Source Transaction:**  
Order #101  
Customer: John Doe  
Product: Laptop  
Quantity: 2  
Unit Price: 50000  

**Data Warehouse Representation:**

**fact_sales**
{
date_key: 20240115,
product_key: 5,
customer_key: 12,
quantity_sold: 2,
unit_price: 50000,
discount_amount: 0,
total_amount: 100000
}


**dim_date**
{
date_key: 20240115,
full_date: '2024-01-15',
month: 1,
quarter: 'Q1',
year: 2024
}


**dim_product**
{
product_key: 5,
product_name: 'Laptop',
category: 'Electronics'
}


**dim_customer**
{
customer_key: 12,
customer_name: 'John Doe',
city: 'Mumbai'
}