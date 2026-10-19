-- Calling the macro in a model
select
    order_id,
    {{ date_diff('order_date', 'order_date') }} as days_to_ship
from {{ ref('fct_orders') }}