-- =========================
-- DIM DATE (30 ROWS)
-- =========================
INSERT INTO dim_date VALUES
(20240101,'2024-01-01','Monday',1,1,'January','Q1',2024,false),
(20240102,'2024-01-02','Tuesday',2,1,'January','Q1',2024,false),
(20240103,'2024-01-03','Wednesday',3,1,'January','Q1',2024,false),
(20240104,'2024-01-04','Thursday',4,1,'January','Q1',2024,false),
(20240105,'2024-01-05','Friday',5,1,'January','Q1',2024,false),
(20240106,'2024-01-06','Saturday',6,1,'January','Q1',2024,true),
(20240107,'2024-01-07','Sunday',7,1,'January','Q1',2024,true),
(20240108,'2024-01-08','Monday',8,1,'January','Q1',2024,false),
(20240109,'2024-01-09','Tuesday',9,1,'January','Q1',2024,false),
(20240110,'2024-01-10','Wednesday',10,1,'January','Q1',2024,false),
(20240111,'2024-01-11','Thursday',11,1,'January','Q1',2024,false),
(20240112,'2024-01-12','Friday',12,1,'January','Q1',2024,false),
(20240113,'2024-01-13','Saturday',13,1,'January','Q1',2024,true),
(20240114,'2024-01-14','Sunday',14,1,'January','Q1',2024,true),
(20240115,'2024-01-15','Monday',15,1,'January','Q1',2024,false),
(20240116,'2024-01-16','Tuesday',16,1,'January','Q1',2024,false),
(20240117,'2024-01-17','Wednesday',17,1,'January','Q1',2024,false),
(20240118,'2024-01-18','Thursday',18,1,'January','Q1',2024,false),
(20240119,'2024-01-19','Friday',19,1,'January','Q1',2024,false),
(20240120,'2024-01-20','Saturday',20,1,'January','Q1',2024,true),
(20240121,'2024-01-21','Sunday',21,1,'January','Q1',2024,true),
(20240201,'2024-02-01','Thursday',1,2,'February','Q1',2024,false),
(20240202,'2024-02-02','Friday',2,2,'February','Q1',2024,false),
(20240203,'2024-02-03','Saturday',3,2,'February','Q1',2024,true),
(20240204,'2024-02-04','Sunday',4,2,'February','Q1',2024,true),
(20240205,'2024-02-05','Monday',5,2,'February','Q1',2024,false),
(20240206,'2024-02-06','Tuesday',6,2,'February','Q1',2024,false),
(20240207,'2024-02-07','Wednesday',7,2,'February','Q1',2024,false),
(20240208,'2024-02-08','Thursday',8,2,'February','Q1',2024,false),
(20240209,'2024-02-09','Friday',9,2,'February','Q1',2024,false);

-- =========================
-- DIM PRODUCT (15 ROWS)
-- =========================
INSERT INTO dim_product (product_key, product_id, product_name, category, subcategory, unit_price) VALUES
(1,'P001','Laptop','Electronics','Computers',75000),
(2,'P002','Smartphone','Electronics','Mobiles',45000),
(3,'P003','Tablet','Electronics','Gadgets',30000),
(4,'P004','Headphones','Electronics','Accessories',2500),
(5,'P005','Smart Watch','Electronics','Wearables',12000),
(6,'P006','T-Shirt','Clothing','Men',799),
(7,'P007','Jeans','Clothing','Men',1999),
(8,'P008','Dress','Clothing','Women',2499),
(9,'P009','Jacket','Clothing','Winter',4999),
(10,'P010','Shoes','Clothing','Footwear',2999),
(11,'P011','Sofa','Home','Furniture',35000),
(12,'P012','Dining Table','Home','Furniture',45000),
(13,'P013','Mixer Grinder','Home','Kitchen',4999),
(14,'P014','Microwave Oven','Home','Appliances',18000),
(15,'P015','Bed','Home','Furniture',55000);

-- =========================
-- DIM CUSTOMER (12 ROWS)
-- =========================
INSERT INTO dim_customer (customer_key, customer_id, customer_name, city, state, customer_segment) VALUES
(1,'C001','Rahul Sharma','Mumbai','Maharashtra','Retail'),
(2,'C002','Anita Verma','Delhi','Delhi','Retail'),
(3,'C003','Suresh Rao','Bangalore','Karnataka','Corporate'),
(4,'C004','Priya Iyer','Chennai','Tamil Nadu','Retail'),
(5,'C005','Amit Patel','Mumbai','Maharashtra','Corporate'),
(6,'C006','Neha Singh','Delhi','Delhi','Retail'),
(7,'C007','Rohan Das','Bangalore','Karnataka','Retail'),
(8,'C008','Kavita Menon','Chennai','Tamil Nadu','Corporate'),
(9,'C009','Vikas Malhotra','Delhi','Delhi','Corporate'),
(10,'C010','Sunita Joshi','Mumbai','Maharashtra','Retail'),
(11,'C011','Arjun Mehta','Bangalore','Karnataka','Corporate'),
(12,'C012','Pooja Nair','Chennai','Tamil Nadu','Retail');

-- =========================
-- FACT SALES (40 ROWS)
-- =========================
INSERT INTO fact_sales
(date_key, product_key, customer_key, quantity_sold, unit_price, discount_amount, total_amount)
VALUES
(20240106,1,1,2,75000,5000,145000),
(20240107,2,2,3,45000,0,135000),
(20240113,3,3,1,30000,2000,28000),
(20240114,4,4,4,2500,0,10000),
(20240120,5,5,2,12000,1000,23000),
(20240121,6,6,5,799,0,3995),
(20240106,7,7,3,1999,0,5997),
(20240107,8,8,2,2499,0,4998),
(20240113,9,9,1,4999,500,4499),
(20240114,10,10,2,2999,0,5998),

(20240101,11,11,1,35000,3000,32000),
(20240102,12,12,1,45000,0,45000),
(20240103,13,1,3,4999,0,14997),
(20240104,14,2,2,18000,1000,35000),
(20240105,15,3,1,55000,5000,50000),

(20240203,1,4,2,75000,0,150000),
(20240204,2,5,3,45000,3000,132000),
(20240203,3,6,2,30000,0,60000),
(20240204,4,7,5,2500,0,12500),
(20240203,5,8,1,12000,0,12000),

(20240108,6,9,4,799,0,3196),
(20240109,7,10,2,1999,0,3998),
(20240110,8,11,3,2499,0,7497),
(20240111,9,12,1,4999,0,4999),
(20240112,10,1,2,2999,0,5998),

(20240205,11,2,1,35000,0,35000),
(20240206,12,3,1,45000,0,45000),
(20240207,13,4,2,4999,0,9998),
(20240208,14,5,1,18000,0,18000),
(20240209,15,6,1,55000,0,55000),

(20240115,1,7,1,75000,0,75000),
(20240116,2,8,2,45000,0,90000),
(20240117,3,9,1,30000,0,30000),
(20240118,4,10,3,2500,0,7500),
(20240119,5,11,2,12000,0,24000);
