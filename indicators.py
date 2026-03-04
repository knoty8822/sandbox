import ta

def add_indicators(df, ma1, ma2):

    df["MA1"] = df["Close"].rolling(ma1).mean()
    df["MA2"] = df["Close"].rolling(ma2).mean()

    rsi = ta.momentum.RSIIndicator(df["Close"])
    df["RSI"] = rsi.rsi()

    bb = ta.volatility.BollingerBands(df["Close"])

    df["BB_upper"] = bb.bollinger_hband()
    df["BB_lower"] = bb.bollinger_lband()

    return df
