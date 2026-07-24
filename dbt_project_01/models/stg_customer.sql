select * from {{ source('northwind', 'customer') }}
