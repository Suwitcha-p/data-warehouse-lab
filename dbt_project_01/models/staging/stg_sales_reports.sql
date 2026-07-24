select * from {{ source('northwind', 'sales_reports') }}
