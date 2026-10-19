-- Abstracts datediff syntax across different warehouses
{% macro date_diff(start_date, end_date) %}
    datediff(day, {{ start_date }}, {{ end_date }})
{% endmacro %}
