select * from {{ source('northwind', 'order_details_status') }}
