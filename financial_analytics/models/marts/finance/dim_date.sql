SELECT
    DISTINCT trade_date,
   {{ dbt_utils.generate_surrogate_key(['trade_date']) }} as date_id
FROM {{ ref('stg_prices') }}
