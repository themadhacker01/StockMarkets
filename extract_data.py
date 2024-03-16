import os

import pandas_datareader as pdr
import pandas as pd

from datetime import datetime

# Set the current and start dates to pull data
# The end date is set to current date by default
start_date = '2018-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')

# List the ticker symbols you are interested in
tickers = ['SPY', 'AAL', 'ZM', 'NFLX']

# Store each dataframe seperately for easy plotting
ticker_data = {}
for t in tickers:
    ticker_data[t] = pdr.DataReader(t, 'stooq', start_date, end_date)

# Concat all df to create a single df named stocks
stocks = pd.concat(ticker_data, axis = 1, keys = tickers)

# Set names for the multi index
stocks.columns.names = ['Ticker Symbol', 'Stock Info']

# Check if data dir exists, else create one
file_dir = 'data'
if not os.path.exists(file_dir):
    os.makedirs(file_dir)

# Store the extracted data into a csv file
# Stock data contains 1 string row, all other rows are int or float
# This 1 row causes all values to get extracted as string when reading csv
# Causes issues in plotting, data conversion is not easy
stocks.to_csv(file_dir + '/stock_data.csv')

# Store the extracted data into a csv file
# Easier to read json when df has multiple data types
stocks.to_json(file_dir + '/stock_data.json')