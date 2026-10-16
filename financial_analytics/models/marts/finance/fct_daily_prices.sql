SELECT
    ticker.Ticker_id,
    date.date_id,
    stg.open,
    stg.high,
    stg.low,
    stg.close,
    stg.volume
FROM {{ ref('stg_prices') }} as stg
LEFT JOIN {{ ref('dim_ticker') }} as ticker
ON ticker.ticker = stg.ticker
LEFT JOIN {{ ref('dim_date') }} as date 
ON date.trade_date = stg.trade_date
