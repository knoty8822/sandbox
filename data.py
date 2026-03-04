import yfinance as yf

def get_stock_data(ticker, timeframe):

    try:
        df = yf.download(
            ticker,
            period=timeframe,
            auto_adjust=True
        )

        return df

    except:
        return None
