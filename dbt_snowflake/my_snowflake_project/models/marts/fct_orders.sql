{{ config(materialized='table') }}

select
    order_id,
    order_date,
    customer_name,
    customer_tier,
    total_amount,
    case
        when total_amount >= 10000 then 'High Value'
        when total_amount >= 1000  then 'Mid Value'
        else 'Low Value'
    end as order_tier
from {{ ref('int_orders_enriched') }}