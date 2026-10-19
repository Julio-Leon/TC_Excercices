-- Orders should never have a future date
SELECT
    order_id,
    order_date
FROM 
    {{ ref('stg_orders') }}
WHERE
    order_date > CURRENT_DATE