import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the CSV file
csv_file = 'weekly_feb_2024.csv'
data = pd.read_csv(csv_file)

# Convert the start_date column to datetime
data['start_date'] = pd.to_datetime(data['start_date'])

# Define a function to plot time series data for each pollutant
def plot_time_series(data, pollutant, title, ylabel):
    plt.figure(figsize=(14, 5))
    for key, grp in data.groupby(['latitude', 'longitude']):
        plt.plot(grp['start_date'], grp[pollutant], label=f'Location: {key}')
    
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.title(title)
    # plt.legend(loc='best')
    plt.grid(True)
    plt.show()

# Plot CO time series
plot_time_series(data, 'co', 'CO Time Series', 'CO (μg/m³)')

# Plot SO2 time series
# plot_time_series(data, 'so2', 'SO2 Time Series', 'SO2 (μg/m³)')

# Plot PM2.5 time series
# plot_time_series(data, 'pm2_5', 'PM2.5 Time Series', 'PM2.5 (μg/m³)')

# Plot PM10 time series
# plot_time_series(data, 'pm10', 'PM10 Time Series', 'PM10 (μg/m³)')