select * from {{ source('northwind', 'employee_privileges') }}
