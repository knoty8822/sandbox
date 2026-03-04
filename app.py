import streamlit as st
import yfinance as yf
import pandas as pd

from utils.data_fetcher import get_stock_data
from utils.indicators import add_indicators
from visualizations.candlestick_chart import plot_candlestick
from visualizations.export_tools import export_chart

st.set_page_config(
    page_title="Stock Market Visualizer",
    layout="wide"
)

st.title("📊 Stock Market Visualizer")

# Sidebar Controls
ticker = st.sidebar.text_input("Ticker", "AAPL")
period = st.sidebar.selectbox(
    "Timeframe",
    ["1mo","3mo","6mo","1y","2y","5y","10y"]
)

ma1 = st.sidebar.slider("Moving Average 1", 5, 100, 20)
ma2 = st.sidebar.slider("Moving Average 2", 20, 200, 50)

show_rsi = st.sidebar.checkbox("Show RSI", True)
show_bb = st.sidebar.checkbox("Show Bollinger Bands", True)

# Fetch Data
data = get_stock_data(ticker, period)

if data is not None:

    df = add_indicators(data, ma1, ma2)

    fig = plot_candlestick(
        df,
        ma1=ma1,
        ma2=ma2,
        show_rsi=show_rsi,
        show_bb=show_bb
    )

    st.plotly_chart(fig, use_container_width=True)

    if st.button("Export Chart"):
        export_chart(fig, ticker)

else:
    st.error("Unable to fetch stock data.")
