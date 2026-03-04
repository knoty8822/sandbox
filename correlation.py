import streamlit as st
import yfinance as yf
import plotly.express as px

st.title("🔗 Stock Correlation Analysis")

tickers = st.text_input(
    "Enter tickers",
    "AAPL,MSFT,NVDA,TSLA"
)

period = st.selectbox(
    "Time Period",
    ["6mo","1y","2y"]
)

if st.button("Run Analysis"):

    ticker_list = [t.strip() for t in tickers.split(",")]

    data = yf.download(
        ticker_list,
        period=period
    )["Close"]

    corr = data.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu"
    )

    st.plotly_chart(fig)
