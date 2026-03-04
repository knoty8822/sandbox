import streamlit as st
import pandas as pd
import yfinance as yf

st.title("📁 Portfolio Tracker")

file = st.file_uploader("Upload CSV or Excel")

if file:

    if file.name.endswith("csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    prices = {}

    for ticker in df["Ticker"]:
        data = yf.Ticker(ticker)
        prices[ticker] = data.history(period="1d")["Close"].iloc[-1]

    df["Current Price"] = df["Ticker"].map(prices)
    df["Value"] = df["Shares"] * df["Current Price"]

    st.dataframe(df)

    st.metric(
        "Total Portfolio Value",
        f"${df['Value'].sum():,.2f}"
    )
