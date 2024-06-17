import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the CSV file
csv_file = 'weekly_All_24.csv'
data = pd.read_csv(csv_file)

# Convert the start_date column to datetime
data['start_date'] = pd.to_datetime(data['start_date'])

# Define a function to plot time series data for each pollutant
def plot_time_series(data, pollutant, title, ylabel):
    plt.figure(figsize=(25, 10))
    for key, grp in data.groupby(['latitude', 'longitude']):
        plt.plot(grp['start_date'], grp[pollutant], label=f'Location: {key}')
    
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.title(title)
    # plt.legend(loc='best')
    plt.grid(True)
    plt.show()

# Plot CO time seriesDecember
# plot_time_series(data, 'co', 'CO Time Series for 2024 From December to March in Ogbomosho', 'CO (μg/m³)')

# Plot SO2 time series
plot_time_series(data, 'so2', 'SO2 Time Series for 2024 From December to March in Ogbomosho', 'SO2 (μg/m³)')

# Plot PM2.5 time series
plot_time_series(data, 'pm2_5', 'PM2.5 Time Series for 2024 From December to March in Ogbomosho', 'PM2.5 (μg/m³)')

# Plot PM10 time series
plot_time_series(data, 'pm10', 'PM10 Time Series for 2024 From December to March in Ogbomosho', 'PM10 (μg/m³)')
