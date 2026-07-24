select * from {{ source('northwind', 'invoices') }}
