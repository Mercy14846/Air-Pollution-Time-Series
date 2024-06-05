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
	"latitude": [7.9742417, 7.94112, 7.94493, 7.9640833, 7.9641133, 7.977995, 7.98917, 7.95359, 7.9817967, 7.9678433, 7.94647, 7.9821433, 7.9445333, 7.979075, 7.9743167, 7.97493, 7.9734433, 7.945825, 7.9640567, 7.98882, 7.9678517, 7.9600033, 7.9678483],
	"longitude": [3.4971033, 3.481975, 3.5234917, 3.5088067, 3.5096683, 3.4903783, 3.5476083, 3.5562017, 3.4925283, 3.5595267, 3.54655, 3.5593967, 3.553905, 3.5579183, 3.5158967, 3.5019883, 3.526635, 3.5479517, 3.5097667, 3.5479483, 3.5595333, 3.5660183, 3.5592567],
	"hourly": ["pm10", "pm2_5", "carbon_monoxide", "sulphur_dioxide"],
	"start_date": "2024-03-01",
	"end_date": "2024-03-30"
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

hourly_dataframe.to_csv('mar_air_quality_data.csv', index=False)
csv_file_path = 'mar_air_quality_data.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame
print(df.head())