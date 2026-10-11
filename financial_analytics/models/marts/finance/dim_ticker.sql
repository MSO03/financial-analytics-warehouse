SELECT
    DISTINCT ticker,
   {{ dbt_utils.generate_surrogate_key(['ticker']) }} as Ticker_id 
FROM {{ ref('stg_prices')  }}
