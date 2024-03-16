import pandas as pd
import matplotlib.pyplot as plt

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


# Drawing a distribution plot for Apple stocks
ticker_aal = "('AAL', 'Close')"
date_range_19 = pd.date_range('2019-01-01', '2019-12-31')
date_range_20 = pd.date_range('2020-01-01', '2020-12-31')

closing_pct_2019 = closing_pct_change[ticker_aal][closing_pct_change.index.isin(date_range_19)]
closing_pct_2020 = closing_pct_change[ticker_aal][closing_pct_change.index.isin(date_range_20)]

plt.figure(figsize = (6, 4))
closing_pct_2019.plot(kind = 'hist', label = '2019', bins = 12, alpha = 0.5)
closing_pct_2020.plot(kind = 'hist', label = '2020', bins = 50, alpha = 0.5)
plt.title('Distribution of ' + ticker_aal + 'price changes')
plt.xlabel('Daily Returns (%)')
plt.legend()
plt.show()
