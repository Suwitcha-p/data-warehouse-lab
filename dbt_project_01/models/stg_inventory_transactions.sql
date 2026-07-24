select * from {{ source('northwind', 'inventory_transactions') }}
