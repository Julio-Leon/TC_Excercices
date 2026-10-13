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
    -- Snow pipe is for real-time pipelines
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
  
