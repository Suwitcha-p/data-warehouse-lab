select * from {{ source('northwind', 'purchase_orders') }}
