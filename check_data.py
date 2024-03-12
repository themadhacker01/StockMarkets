import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the csv and store it as a local df
file_path = 'data/stock_data.json'
stock_data = pd.read_json(file_path)

# Validates that read json parses values correctly
print(stock_data.info())

# Print column type and acceptable values
print(stock_data.info())

# Print the num of rows, columns in the df
print(stock_data.shape)

# Get basic stats for the df
print(stock_data.describe())

# Missing values could be due to unstable APIs or because a company had not listed yet
# Visualise missing values in yellow in a heatmap using seaborn library
plt.figure(figsize = (4, 1))
sns.set_theme(font_scale = 0.75)
plt.tight_layout()
sns.heatmap(stock_data.isnull())
plt.show()