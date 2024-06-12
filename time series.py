import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

# Load the CSV file into a DataFrame
csv_file_path = 'feb_O_air_quality_data.csv'  # Replace with your file path
df = pd.read_csv(csv_file_path, parse_dates=['date'])

print (df.head())

# Set the date column as the index
df.set_index('date', inplace=True)

# Coordinates for the location
latitude = 8.1339967
longitude = 4.1852767

# Create a folium map centered on the location
map_center = [latitude, longitude]
m = folium.Map(location=map_center, zoom_start=12)

# Add a marker to the map
folium.Marker(
    location=map_center,
    popup='Air Quality Monitoring Location For Ogbomosho',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(m)

# Prepare data for the heatmap
# For simplicity, assume each pollutant contributes equally to the heatmap intensity
heat_data = [
    [latitude, longitude, row['pm10'] + row['pm2_5'] + row['carbon_monoxide'] + row['sulphur_dioxide'] ]
    for index, row in df.iterrows()
]

# Add heatmap layer to the folium map
HeatMap(heat_data, radius=15, blur=10, max_zoom=1).add_to(m)

# Save the map to an HTML file
map_html_path = 'map_with_heatmap.html'
m.save(map_html_path)

# Plotting the time series data
fig, axs = plt.subplots(4, 1, figsize=(10, 114), sharex=True)

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

# Display the map (in a Jupyter notebook environment, you can use the following)
m