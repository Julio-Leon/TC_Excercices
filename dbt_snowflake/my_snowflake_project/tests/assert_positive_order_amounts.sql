-- This test fails if any order has a non-positive amount
-- A failing row is any row returned by this query
select
    order_id,
    total_amount
FROM 
    {{ ref('stg_orders') }}
WHERE
    total_amount <= 0
-- If any row is returned, the test fails
-- An empty result = test passed