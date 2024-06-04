import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
csv_file_path = '1_air_quality_data.csv'  # Replace with your file path
df = pd.read_csv(csv_file_path, parse_dates=['date'])

# Set the date column as the index
df.set_index('date', inplace=True)

# Plotting the time series data
fig, axs = plt.subplots(4, 1, figsize=(12, 16), sharex=True)

# Plot PM10
axs[0].plot(df.index, df['pm10'], label='PM10', color='blue')
axs[0].set_title('PM10 Levels Over Time')
axs[0].set_ylabel('PM10 (µg/m³)')
axs[0].legend()

# Plot PM2.5
axs[1].plot(df.index, df['pm2_5'], label='PM2.5', color='green')
axs[1].set_title('PM2.5 Levels Over Time')
axs[1].set_ylabel('PM2.5 (µg/m³)')
axs[1].legend()

# Plot Carbon Monoxide
axs[2].plot(df.index, df['carbon_monoxide'], label='Carbon Monoxide', color='red')
axs[2].set_title('Carbon Monoxide Levels Over Time')
axs[2].set_ylabel('CO (mg/m³)')
axs[2].legend()

# Plot Sulphur Dioxide
axs[3].plot(df.index, df['sulphur_dioxide'], label='Sulphur Dioxide', color='purple')
axs[3].set_title('Sulphur Dioxide Levels Over Time')
axs[3].set_ylabel('SO₂ (mg/m³)')
axs[3].set_xlabel('Date')
axs[3].legend()

# Adjust the layout
plt.tight_layout()
plt.show()