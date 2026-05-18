import yfinance as yf
import pandas as pd

TICKERS = ["VT", "IJS", "VXUS", "SPY"]

def fetch_data():
    all_data = []

    for ticker in TICKERS:
        df = yf.download(ticker, start="2020-01-01")
        df = df.reset_index()
        df["ticker"] = ticker
        all_data.append(df)

    return pd.concat(all_data, ignore_index=True)

def main():
    df = fetch_data()
    '''
    df.columns = [
        "date",
        "open",
        "high",
        "low",
        "close",
        "adj_close",
        "volume",
        "ticker"
    ]
    '''
    df.to_csv("raw_prices.csv", index=False)
    print("Saved data:", df.shape)
    print(df.columns)

if __name__ == "__main__":
    main()
