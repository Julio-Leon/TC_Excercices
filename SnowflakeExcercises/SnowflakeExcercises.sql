-- Beginner Level

-- Conceptual Questions
-- 1. What are the three layers of Snowflake’s architecture, and what does each handle?
    -- The storage layer, where storage is actually located.
    -- The processing layer, where transformations are happening.
    -- The cloud services, every other feature offered by Snowflake, manages the other 2 layers.
    
-- 2. Explain the difference between Permanent, Transient, and Temporary tables.
    -- Permanet tables are saved and have Time Travel and Fail Safe features.
    -- Transient tables have no Fail Safe features, but have Time Travel features only for 1 day.
    -- Temporary tables are not saved in between sessions, no Time Travel and Fail Safe features.

-- 3. What is the purpose of a Virtual Warehouse in Snowflake?
    -- Virtual warehouses are managed by Snowflake, all the computing and storage features are all managed directly by it, it can grow and shrink, and activate and deactivate clusters. We can specify settings for these features.

-- 4. How does Snowflake handle semi-structured data like JSON?
    -- It uses the Varient data type so that it can handle these semi-structured data types, for example JSON, it allows us to actually retriee the data just like we could in other systems, but with a special syntax.

-- 5. Compare Snowpipe with the COPY INTO command.
    -- Snow pipe is for near real-time pipelines
    -- COPY INTO is used for batch pipelines, where huge data transfer is the norm.

CREATE WAREHOUSE retail_wh
  WAREHOUSE_SIZE = 'SMALL'
  AUTO_SUSPEND = 300
  AUTO_RESUME = TRUE
  COMMENT = 'Retail warehouse for excercises';

CREATE DATABASE retail_db;
CREATE SCHEMA q3_sales;

USE DATABASE retail_db;
USE SCHEMA q3_sales;

CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(20),
    price DOUBLE
);

INSERT INTO products
    VALUES 
        (1, 'Milk', 9.99),
        (2, 'Eggs', 12.99),
        (3, 'Candy', 2.99),
        (4, 'Chips', 1.49),
        (5, 'Secret Sauce', 99.99);

SELECT * FROM products WHERE price > 10;


-- Intermediate Level

-- Conceptual Questions
-- 1. What is the difference between Time Travel and Zero-Copy Cloning in Snowflake?
    -- Time travel is when we access a a table at a previous state or time. We can go back to a specific time, or before a specific query.
    -- Zero-Copy cloning is when we clone a specific table, or database. There is no relationship in between the clone and the real one, the clone saves that specific state at that specific time, and will not change.

--2. How do Internal Stages differ from External Stages?
    -- Internal Stages are completely managed by Snowflake.
    -- External Stages aren't managed by Snowflake, Snowflake only read-only access to these stages.

-- 3. What role does RBAC play in Snowflake, and why is it important?
    -- 

-- 4. How do Streams help implement Change Data Capture (CDC)?
    -- Streams allow us to keep track of the the changes on a table since the last time it was consumed. When a table gets consumed by a task, these changes go away and we restart the process.

-- 5. Explain how Snowflake achieves separation of compute and storage.
    -- Snowflake achieves the separation by keeping these 2 features in different layers. There is a storage layer and a different computing layer. These can be scaled separately, also, if 1 fails, we have access to the other one.

CREATE FILE FORMAT my_csv_format
    TYPE = 'CSV'
    SKIP_HEADER = 1;

CREATE STAGE my_stage;
-- USE retail_db;
-- USE SCHEMA q3_sales;
-- PUT 'file:///C:/Users/Julio Diaz/Desktop/orders.csv' @my_stage;

CREATE TABLE sales_fact(order_id INT, amount DOUBLE);

COPY INTO sales_fact FROM @my_stage 
    FILE_FORMAT = (FORMAT_NAME = 'my_csv_format');

SELECT * FROM sales_fact;

CREATE TABLE customers (
    customer_id INT,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(20),
    city VARCHAR(20),
    state VARCHAR(20)
);

CREATE TABLE customers_json (
    customer VARIANT
);

COPY INTO customers_json FROM @my_stage/customers.json
    FILE_FORMAT = (TYPE = 'JSON' STRIP_OUTER_ARRAY = TRUE);

SELECT 
    customer:first_name::STRING || ' ' || customer:last_name AS customer_name 
FROM 
    customers_json;

CREATE OR REPLACE STREAM
    products_stream
ON TABLE
    products;

INSERT INTO 
    products 
VALUES
    (15, 'something finally', 0.89);

SELECT * FROM products_stream;

CREATE OR REPLACE TABLE products_end (
    product_id INT,
    product_name VARCHAR(20),
    price DOUBLE
)

CREATE OR REPLACE TASK merge_products_to_end
    WAREHOUSE = retail_wh
    SCHEDULE = '1 MINUTE'
AS
    MERGE INTO products_end tgt
        USING(
            SELECT
                *,
                METADATA$ACTION AS action,
                METADATA$ISUPDATE AS is_update
            FROM
                products_stream
            WHERE
                (METADATA$ACTION = 'INSERT' AND  NOT METADATA$ISUPDATE)
        ) src
        ON 
            tgt.product_id = src.product_id
        WHEN NOT MATCHED THEN
            INSERT (product_id, product_name, price)
            VALUES (src.product_id, src.product_name, src.price);

ALTER TASK merge_products_to_end RESUME;
ALTER TASK merge_products_to_end SUSPEND;


SELECT * FROM products_stream;
SELECT * FROM products_end;

SHOW TASKS LIKE 'MERGE_PRODUCTS_TO_END';

--Advanced Level

-- Conceptual Questions
-- 1. When would you use Snowpipe Streaming instead of classic Snowpipe?
    --Both ingest data into Snowflake, but the main difference is how the data arrives and how quickly you need it available.

-- 2. How do Secure Views and Row Access Policies secure shared data?
    -- These features let you control what consumers can see without necessarily giving them access to the underlying data.
    -- A Secure View hides the underlying query definition from users who consume the view and can help protect sensitive implementation details.
    -- A Row Access Policy controls which rows a user can see, based on their role or other conditions.

-- 3. What are best practices for designing role hierarchies in Snowflake?
    -- Snowflake uses role-based access control (RBAC). A good hierarchy makes permissions easier to manage and audit.

-- 4. How does LATERAL FLATTEN work with semi-structured data?
    --Snowflake stores semi-structured data in types such as VARIANT, which can contain JSON objects and arrays.
    -- FLATTEN converts elements of an array or object into individual rows. 
    -- LATERAL allows the function to reference a column from the preceding table row.

-- 5. Explain Snowflake billing: compute vs. storage
    -- Snowflake's costs primarily come from compute, storage, and additional services such as data transfer or serverless features.


-- Hands-On Excercise

UNDROP a_table;

CREATE OR REPLACE MASKING POLICY email_mask
AS (email VARCHAR)
RETURNS VARCHAR ->
    CASE
        WHEN CURRENT_ROLE() = 'HR_ROLE'
            THEN email
        ELSE '********'
    END;



CREATE OR REPLACE ROW ACCESS POLICY region_access_policy
AS (region VARCHAR)
RETURNS BOOLEAN ->
    CURRENT_ROLE() = 'ADMIN_ROLE'
    OR region = CURRENT_ROLE();