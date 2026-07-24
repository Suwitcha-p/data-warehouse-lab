WITH source AS (
SELECT
    customer_id,
    tax_status_name,
    current_localtimestamp() as insertion_timestamp
FROM {{ ref('stg_customer') }}
),

unique_source AS (
    SELECT *,
            row_number() OVER(PARTITION BY customer_id) AS row_num
    FROM source
)

SELECT *
EXCLUDE (row_num)
FROM unique_source
WHERE row_num = 1