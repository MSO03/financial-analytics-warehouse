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
            "Date": "trade_date",
            "Ticker": "ticker",
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume"
        })
    )

    return df[
        [
            "trade_date",
            "ticker",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]
    ]


def main():

    df = fetch_data()

    df.to_csv("raw_prices.csv", index=False)


if __name__ == '__main__':
        main()
