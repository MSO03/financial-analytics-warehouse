import yfinance as yf
import pandas as pd

TICKERS = ["VT", "IJS","VXUS","SPY"]

def fetch_data():

    df = yf.download(
        TICKERS,
        period="5d",
        group_by="ticker",
        auto_adjust=True
    )
    df = (
        df
        .stack(level=0)
        .reset_index()
        .rename(columns={
            "Date": "TRADE_DATE",
            "Ticker": "TICKER",
            "Open": "OPEN",
            "High": "HIGH",
            "Low": "LOW",
            "Close": "CLOSE",
            "Volume": "VOLUME"
        })
    )

    return df[
        [
            "TRADE_DATE",
            "TICKER",
            "OPEN",
            "HIGH",
            "LOW",
            "CLOSE",
            "VOLUME"
        ]
    ]


def main():

    df = fetch_data()

    df.to_csv("raw_prices.csv", index=False)



main()
