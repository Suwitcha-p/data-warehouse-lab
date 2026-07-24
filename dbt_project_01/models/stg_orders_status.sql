select * from {{ source('northwind', 'orders_status') }}
