select * from {{ source('northwind', 'inventory_transaction_types') }}
