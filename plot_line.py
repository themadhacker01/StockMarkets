import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Read the csv and store it as a local df
file_path = 'data/stock_data.json'
stock_data = pd.read_json(file_path)

# List the ticker symbols you are interested in
tickers = ['SPY', 'AAL', 'ZM', 'NFLX']

# To view all keys in the stock_data df
# print(stock_data.keys())

# Create a df for the closing prices of stocks
closing_prices = stock_data[["('SPY', 'Close')", "('AAL', 'Close')", "('ZM', 'Close')", "('NFLX', 'Close')"]]
print(closing_prices.head())

# Use plot method and matplotlib to create line chart
closing_prices.plot.line()
plt.show()

# Use plotly library to create line chart
fig = px.line(closing_prices, x = closing_prices.index, y = closing_prices.columns, title = 'Closing Prices')
fig.update_layout(hovermode = 'x', yaxis_title = 'Price')
fig.show()