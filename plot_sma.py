import pandas as pd
import matplotlib.pyplot as plt

# Read the csv and store it as a local df
file_path = 'data/stock_data.json'
stock_data = pd.read_json(file_path)

# Ticker symbol we are interested in
ticker = 'NFLX'

# Plot the closing stock price of NFLX
stock_data["('NFLX', 'Close')"].plot(color = 'blue', use_index=True)

# Calc the simple moving average 'sma' of NFLX closing price
stock_nflx_sma = stock_data["('NFLX', 'Close')"].rolling(window = 10).mean()

# Plot the simple moving average of NFLX
stock_nflx_sma.plot(color = 'red', use_index=True)

# View the legend for the 2 plots
plt.legend(['Closing stock price', 'Simple moving avg'])
plt.show()