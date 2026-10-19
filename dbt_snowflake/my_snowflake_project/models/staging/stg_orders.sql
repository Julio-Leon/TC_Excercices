-- This SELECT statement is the entire model.
-- dbt creates analytics.stg_orders from it.


SELECT
    order_id,
    customer_id,
    order_date,
    total_amount
FROM
    {{ source('public', 'orders') }}
WHERE 
    order_id IS NOT NULL