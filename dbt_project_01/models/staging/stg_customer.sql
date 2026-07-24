WITH source AS (
    SELECT * 
    FROM {{ source('northwind', 'customer') }}
)

SELECT
    id AS customer_id,
    tax_status_name
FROM source