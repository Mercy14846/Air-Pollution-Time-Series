import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://air-quality-api.open-meteo.com/v1/air-quality"
params = {
	"latitude": [8.1339967, 8.1839067, 8.1161483, 8.1764417, 8.1011533, 8.1826733, 8.1652817, 8.1463517, 8.14878, 8.14668, 8.1579383, 8.16879, 8.1772333, 8.1681633, 8.1688867, 8.1124933, 8.1772317, 8.1155583, 8.135985, 8.1753783, 8.1357367, 8.1768333, 8.1396383],
	"longitude": [4.1852767, 4.164755, 4.1576683, 4.1191767, 4.1148217, 4.1642633, 4.1506883, 4.1835683, 4.1121817, 4.1547967, 4.1773533, 4.1227167, 4.1212733, 4.1454433, 4.14591, 4.179395, 4.1213833, 4.121825, 4.1865733, 4.1576183, 4.1914133, 4.1203217, 4.1756],
	"hourly": ["pm10", "pm2_5", "carbon_monoxide", "sulphur_dioxide"],
	"start_date": "2024-01-01",
	"end_date": "2024-01-31"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_pm10 = hourly.Variables(0).ValuesAsNumpy()
hourly_pm2_5 = hourly.Variables(1).ValuesAsNumpy()
hourly_carbon_monoxide = hourly.Variables(2).ValuesAsNumpy()
hourly_sulphur_dioxide = hourly.Variables(3).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["pm10"] = hourly_pm10
hourly_data["pm2_5"] = hourly_pm2_5
hourly_data["carbon_monoxide"] = hourly_carbon_monoxide
hourly_data["sulphur_dioxide"] = hourly_sulphur_dioxide

hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)

hourly_dataframe.to_csv('jan_O_air_quality_data.csv', index=False)
csv_file_path = 'jan_O_air_quality_data.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame
print(df.head())