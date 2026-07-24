select * from {{ source('northwind', 'privileges') }}
