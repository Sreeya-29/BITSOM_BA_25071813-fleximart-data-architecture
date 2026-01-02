# NoSQL Justification Report

## Section A: Limitations of RDBMS (4 marks – ~150 words)

Relational databases like MySQL are designed for structured data with a fixed schema. In an e-commerce product catalog, products often have different attributes. For example, laptops require fields such as RAM, processor, and storage, while shoes require size, color, and material. In an RDBMS, this leads to many unused (NULL) columns or the creation of multiple tables, which increases complexity.

Frequent schema changes are another challenge. Whenever a new product type is added, the database schema must be altered. These changes can be time-consuming, risky, and may require application downtime.

Storing customer reviews is also difficult in a relational model. Reviews contain nested data such as ratings, comments, dates, and user details. Representing this requires multiple tables and complex joins, which reduces query performance and makes the database harder to maintain.

## Section B: NoSQL Benefits (4 marks – ~150 words)

MongoDB solves these problems by using a flexible, document-based schema. Each product is stored as a document and can have its own unique set of fields. This allows laptops, shoes, and other product types to coexist in the same collection without changing the database structure.

MongoDB supports embedded documents, which makes it easy to store customer reviews directly inside the product document. This keeps related data together, reduces the need for joins, and improves read performance.

MongoDB also provides horizontal scalability. Data can be distributed across multiple servers using sharding. As the number of products and users grows, the system can scale by adding more servers, making MongoDB suitable for large and dynamic applications.

## Section C: Trade-offs (2 marks – ~100 words)

One disadvantage of using MongoDB instead of MySQL is weaker support for complex transactions. Although MongoDB supports transactions, relational databases are still better for handling multi-table transactional operations.

Another drawback is data consistency. MongoDB may use eventual consistency in distributed systems, meaning updates may not be immediately visible everywhere. Enforcing relationships between data is also harder because MongoDB does not support foreign keys like MySQL.
