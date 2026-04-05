# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('fdata.csv')
# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%y')

# Set Date as index
data.set_index('Date', inplace=True)

# Plot the line chart
plt.figure(figsize=(10, 6))

plt.plot(data.index, data['Open'], marker='o', label='Open')
plt.plot(data.index, data['High'], marker='o', label='High')
plt.plot(data.index, data['Low'], marker='o', label='Low')
plt.plot(data.index, data['Close'], marker='o', label='Close')

# Add labels and title
plt.title('Alphabet Inc. Financial Data (Oct 3–7, 2016)')
plt.xlabel('Date')
plt.ylabel('Stock Price')

# Rotate x-axis labels
plt.xticks(rotation=45)

# Show legend
plt.legend()

# Show grid
plt.grid()

# Display the plot
plt.show()