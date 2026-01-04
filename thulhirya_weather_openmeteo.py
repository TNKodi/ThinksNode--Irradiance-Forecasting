import requests
import pandas as pd

LAT = 7.274276317883622
LON = 80.2191266481395
TZ = "Asia/Colombo"
START_DATE = "2022-01-01"
END_DATE = "2025-12-01"

# Use archive API because the requested dates are in the past.
BASE_URL = "https://archive-api.open-meteo.com/v1/archive"

# Daily aggregates available from Open-Meteo.
params = {
    "latitude": LAT,
    "longitude": LON,
    "daily": "weathercode,temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max,windgusts_10m_max,shortwave_radiation_sum",
    "start_date": START_DATE,
    "end_date": END_DATE,
    "timezone": TZ,
}

response = requests.get(BASE_URL, params=params, timeout=30)
response.raise_for_status()
data = response.json()

daily = data.get("daily")
if not daily:
    raise ValueError("Daily data missing in Open-Meteo response")

df_weather = pd.DataFrame(daily)

required_keys = [
    "time",
    "weathercode",
    "temperature_2m_max",
    "temperature_2m_min",
    "precipitation_sum",
    "windspeed_10m_max",
    "windgusts_10m_max",
    "shortwave_radiation_sum",
]

missing_keys = [key for key in required_keys if key not in df_weather]
if missing_keys:
    raise ValueError(f"Missing keys in daily data: {missing_keys}")

df_weather = df_weather[required_keys]
df_weather["time"] = pd.to_datetime(df_weather["time"])
df_weather = df_weather.rename(columns={
    "weathercode": "weather_code",
    "temperature_2m_max": "temperature_max",
    "temperature_2m_min": "temperature_min",
    "precipitation_sum": "precipitation",
    "windspeed_10m_max": "wind_speed_max",
    "windgusts_10m_max": "wind_gust_max",
    "shortwave_radiation_sum": "solar_ghi_sum",
})

df_weather.set_index("time", inplace=True)

print(df_weather.head())

df_weather.to_csv("openmeteo_weather_data_daily.csv")
