import requests
import csv
from datetime import datetime, timedelta
import pandas as pd

# Define your API key
api_key = 'e49b736b3458535b673de52e96ef95d7'

# List of coordinates
coordinates = [
    (8.1339967, 4.1852767),
    (8.1839067, 4.164755),
    (8.1161483, 4.1576683),
    (8.1764417, 4.1191767),
    (8.1011533, 4.1148217),
    (8.1826733, 4.1642633),
    (8.1652817, 4.1506883),
    (8.1463517, 4.1835683),
    (8.14878, 4.1121817),
    (8.14668, 4.1547967),
    (8.1579383, 4.1773533),
    (8.16879, 4.1227167),
    (8.1772333, 4.1212733),
    (8.1681633, 4.1454433),
    (8.1688867, 4.14591),
    (8.1124933, 4.179395),
    (8.1772317, 4.1213833),
    (8.1155583, 4.121825),
    (8.135985, 4.1865733),
    (8.1753783, 4.1576183),
    (8.1357367, 4.1914133),
    (8.1768333, 4.1203217),
    (8.1396383, 4.1756)
]
# Date range
start_date = datetime(2024, 2, 1)
end_date = datetime(2024, 2, 29)

# Function to make API request
def fetch_air_pollution_data(lat, lon, date, api_key):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={int(date.timestamp())}&end={int((date + timedelta(days=1)).timestamp())}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} for {lat}, {lon} on {date}")
        return None

# Collect data for all coordinates and dates
all_data = []
current_date = start_date
while current_date <= end_date:
    for lat, lon in coordinates:
        data = fetch_air_pollution_data(lat, lon, current_date, api_key)
        if data and 'list' in data:
            for entry in data['list']:
                all_data.append({
                    'date': current_date.strftime('%Y-%m-%d'),
                    'latitude': lat,
                    'longitude': lon,
                    'aqi': entry['main']['aqi'],
                    'co': entry['components'].get('co', None),
                    'no': entry['components'].get('no', None),
                    'no2': entry['components'].get('no2', None),
                    'o3': entry['components'].get('o3', None),
                    'so2': entry['components'].get('so2', None),
                    'pm2_5': entry['components'].get('pm2_5', None),
                    'pm10': entry['components'].get('pm10', None),
                    'nh3': entry['components'].get('nh3', None)
                })
    current_date += timedelta(days=1)

# Save data to CSV
csv_file = 'now_pollution_data_feb_2024.csv'
csv_columns = ['date', 'latitude', 'longitude', 'aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']
try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in all_data:
            writer.writerow(data)
    print(f"Data successfully written to {csv_file}")
except IOError:
    print("I/O error")

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Display the first few rows of the DataFrame
print(df.head())