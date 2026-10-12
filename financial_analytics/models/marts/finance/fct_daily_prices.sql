SELECT
    ticker.Ticker_id,
    stg.open,
    stg.high,
    stg.low,
    stg.close,
    stg.volume
FROM {{ ref('stg_prices') }} as stg
LEFT JOIN {{ ref('dim_ticker') }} as ticker
ON ticker.Ticker_id = stg.ticker
