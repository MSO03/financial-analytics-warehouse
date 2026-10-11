SELECT
    trade_date,
    ticker,
    open,
    high,
    low,
    close,
    volume
FROM {{ ref('stg_prices') }}    
