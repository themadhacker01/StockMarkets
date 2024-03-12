import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Read the csv and store it as a local df
file_path = 'data/stock_data.json'
stock_data = pd.read_json(file_path)

# List the ticker symbols you are interested in
tickers = 'SPY'

spy_stocks = stock_data[["('SPY', 'Open')", "('SPY', 'High')", "('SPY', 'Low')", "('SPY', 'Close')"]]

# Use plot method and matplotlib to create box chart
# Plots the open, close, high low values for each df column
spy_stocks.plot.box()
plt.show()

# Use plotly library to create box chart
fig = go.Figure(
    data = [
        go.Candlestick(
            x = spy_stocks.index,
            open = spy_stocks["('SPY', 'Open')"],
            close = spy_stocks["('SPY', 'Close')"],
            high = spy_stocks["('SPY', 'High')"],
            low = spy_stocks["('SPY', 'Low')"]
        )
    ]
)

fig.update_layout(
    title = 'Candlestick chart',
    yaxis_title = 'Price',
    xaxis_title = 'Date',
    hovermode = 'x'
)

fig.show()