{{ config(materialized='view') }}

with usa_customer as (
    select * 
    from psql_schema.customers 
    where country = 'USA'
)
select *
from usa_customer