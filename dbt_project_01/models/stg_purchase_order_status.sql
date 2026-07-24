select * from {{ source('northwind', 'purchase_order_status') }}
