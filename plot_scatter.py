import pandas as pd
import plotly.express as px

# Read the csv and store it as a local df
file_path = 'data/stock_data.json'
stock_data = pd.read_json(file_path)

# Create a df to store the daily % change in stock prices
closing_pct_change = pd.DataFrame()

# List the ticker symbols you are interested in
tickers = ["('SPY', 'Close')", "('AAL', 'Close')", "('ZM', 'Close')", "('NFLX', 'Close')"]

# Create a df for the closing prices of stocks
closing_prices = stock_data[["('SPY', 'Close')", "('AAL', 'Close')", "('ZM', 'Close')", "('NFLX', 'Close')"]]

# Calc this value for closing prices using pandas pct_change()
for t in tickers:
    closing_pct_change[t] = (closing_prices[t].pct_change()) * 100

# Calc the avg daily % change for closing stock prices
print(closing_pct_change.mean())

# Calc the std deviation for the % changes in closing price
print(closing_pct_change.std())


# --------------------------------------------------------------------------


fig = px.scatter(
    closing_pct_change,
    x = closing_pct_change.mean(),
    y = closing_pct_change.std(),
    text =  closing_pct_change.columns,
    size_max = 60,
    labels= {
        'x' : 'Daily Price Change (%)',
        'y' : 'Risk'
    },
    title = 'Stock Price Change vs Risks'
)

fig.update_xaxes(
    zeroline = True,
    zerolinewidth = 2,
    zerolinecolor = 'Black'
)

fig.update_yaxes(
    zeroline = True,
    zerolinewidth = 2,
    zerolinecolor = 'Black'
)

fig.update_traces(
    textposition = 'top center'
)

fig.show()
