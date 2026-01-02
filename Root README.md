# FlexiMart Data Architecture Project

**Student Name:** Sreeya Chinthalapani
**Student ID:** BITSOM_BA_25071813
**Email:** sreeyachinthalapani@gmail.com
**Date:** 02-01-2026

## Project Overview
This project focuses on designing and implementing a complete data architecture solution for the FlexiMart retail system. It includes building an ETL pipeline using Python to clean and load CSV data into a PostgreSQL database, justifying the use of NoSQL (MongoDB) for flexible product data, and designing a star schema for analytical reporting. The project also covers data quality checks, database constraints, and proper GitHub submission practices.

## Repository Structure
├── part1-database-etl/
│   ├── etl_pipeline.py
│   ├── schema_documentation.md
│   ├── business_queries.sql
│   └── data_quality_report.txt
├── part2-nosql/
│   ├── nosql_analysis.md
│   ├── mongodb_operations.js
│   └── products_catalog.json
├── part3-datawarehouse/
│   ├── star_schema_design.md
│   ├── warehouse_schema.sql
│   ├── warehouse_data.sql
│   └── analytics_queries.sql
└── README.md

## Technologies Used

- Python 3.x, pandas, mysql-connector-python
- PostgreSQL 18
- MongoDB 8.2.3

## Setup Instructions

### Database Setup

```bash
# Create databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run Part 1 - ETL Pipeline
python part1-database-etl/etl_pipeline.py

# Run Part 1 - Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

# Run Part 3 - Data Warehouse
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql


### MongoDB Setup

mongosh < part2-nosql/mongodb_operations.js

## Key Learnings

Through this project, I learned how to build an end-to-end ETL pipeline using Python, Pandas, and PostgreSQL. I understood how raw data needs cleaning, deduplication, and validation before loading into a database. I also learned when to use relational databases versus NoSQL databases based on data structure and flexibility. Additionally, I gained experience in debugging errors, managing project folders.

## Challenges Faced

1. Transforming data before loading into the database
    The raw datasets did not fully match the database schema, especially for customer IDs, product IDs, and order dates. This was resolved by mapping original IDs to surrogate keys generated in the database and deriving order dates from the transaction date present in the sales dataset. 
2. Executing and validating MongoDB operations (Task 2)
   While working with MongoDB, there was confusion about where and how the output of database operations would appear after running the script. This was resolved by understanding how mongosh executes JavaScript files and by verifying inserted and updated documents directly using MongoDB queries.
