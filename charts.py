import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_candlestick_chart(df, ma1, ma2, show_rsi, show_bb):

    rows = 2 if show_rsi else 1

    fig = make_subplots(
        rows=rows,
        cols=1,
        shared_xaxes=True
    )

    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="Price"
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["MA1"],
            name=f"MA {ma1}"
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["MA2"],
            name=f"MA {ma2}"
        ),
        row=1,
        col=1
    )

    if show_bb:

        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["BB_upper"],
                name="BB Upper"
            ),
            row=1,
            col=1
        )

        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["BB_lower"],
                name="BB Lower"
            ),
            row=1,
            col=1
        )

    if show_rsi:

        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["RSI"],
                name="RSI"
            ),
            row=2,
            col=1
        )

    return fig


def export_chart(fig, ticker, filetype):

    filename = f"{ticker}_chart.{filetype}"

    if filetype == "png":
        fig.write_image(filename)

    if filetype == "html":
        fig.write_html(filename)
