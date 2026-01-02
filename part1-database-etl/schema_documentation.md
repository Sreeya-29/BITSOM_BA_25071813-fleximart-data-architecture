# FlexiMart Database Schema Documentation
## 1. Entity-Relationship Description
### ENTITY: customers

**Purpose:**  
Stores information about customers who shop on the FlexiMart platform.

**Attributes:**
- customer_id: Unique identifier for each customer (Primary Key)
- first_name: Customer’s first name
- last_name: Customer’s last name
- email: Customer’s email address (must be unique)
- phone: Customer’s contact number
- city: City where the customer lives
- registration_date: Date when the customer registered

### ENTITY: products

**Purpose:**  
Stores information about products available for sale.

**Attributes:**
- product_id: Unique identifier for each product (Primary Key)
- product_name: Name of the product
- category: Product category (Electronics, Fashion, Groceries)
- price: Price of the product
- stock_quantity: Number of items available in stock

### ENTITY: orders

**Purpose:**  
Stores information about orders placed by customers.

**Attributes:**
- order_id: Unique identifier for each order (Primary Key)
- customer_id: Identifier of the customer who placed the order (Foreign Key)
- order_date: Date when the order was placed
- total_amount: Total value of the order
- status: Current status of the order (Pending, Completed, Cancelled)

### ENTITY: order_items

**Purpose:**  
Stores detailed information about products included in each order.

**Attributes:**
- order_item_id: Unique identifier for each order item (Primary Key)
- order_id: Identifier of the related order (Foreign Key)
- product_id: Identifier of the product (Foreign Key)
- quantity: Number of units ordered
- unit_price: Price per unit at the time of purchase
- subtotal: Total price for this item (quantity × unit_price)

### Relationships

- One customer can place many orders (1:M relationship between customers and orders).
- One order belongs to only one customer.
- One order can contain many order items (1:M relationship between orders and order_items).
- One product can appear in many order items.

## 2. Normalization Explanation (Third Normal Form – 3NF)
The FlexiMart database design follows Third Normal Form (3NF), which ensures that the data is well-structured, consistent, and free from redundancy.

In this database, each table represents a single entity and all attributes depend only on the primary key. For example, in the customers table, attributes such as first_name, last_name, email, phone, city, and registration_date depend only on customer_id. There are no attributes that depend on other non-key attributes.

Functional dependencies are clearly defined. In the products table, product_id determines product_name, category, price, and stock_quantity. In the orders table, order_id determines customer_id, order_date, total_amount, and status. Similarly, in the order_items table, order_item_id determines order_id, product_id, quantity, unit_price, and subtotal.

This design avoids update anomalies because changes to customer or product details need to be made in only one place. Insert anomalies are avoided because new customers, products, or orders can be added without requiring unrelated data. Delete anomalies are also prevented because deleting an order does not remove customer or product information.

Since there are no partial dependencies or transitive dependencies, and all non-key attributes depend only on the primary key, the database is correctly normalized to Third Normal Form.

## 3. Sample Data Representation
### customers

| customer_id | first_name | last_name | email              | city      |
|------------|------------|-----------|--------------------|-----------|
| 1          | Rahul      | Sharma    | rahul@gmail.com    | Mumbai    |
| 2          | Ananya     | Verma     | ananya@gmail.com   | Delhi     |

### products

| product_id | product_name | category     | price | stock_quantity |
|------------|-------------|--------------|-------|----------------|
| 1          | Smartphone  | Electronics  | 15000 | 25             |
| 2          | T-Shirt     | Fashion      | 800   | 50             |

### orders

| order_id | customer_id | order_date | total_amount | status    |
|---------|-------------|------------|--------------|-----------|
| 1       | 1           | 2024-01-10 | 15800        | Completed |
| 2       | 2           | 2024-01-12 | 800          | Pending  |

### order_items

| order_item_id | order_id | product_id | quantity | subtotal |
|--------------|----------|------------|----------|----------|
| 1            | 1        | 1          | 1        | 15000    |
| 2            | 2        | 2          | 1        | 800      |
