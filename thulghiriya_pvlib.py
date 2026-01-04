import pvlib
import pandas as pd

# -----------------------------
# 1. LOCATION & TIME
# -----------------------------
LAT = 7.274276317883622
LON = 80.2191266481395
TZ  = "Asia/Colombo"

# Hourly time range (needed for daily integration)
times = pd.date_range(
    start="2022-01-01",
    end="2025-12-01 23:00",
    freq="1h",
    tz=TZ
)

location = pvlib.location.Location(LAT, LON, TZ)

# -----------------------------
# 2. SOLAR POSITION (HOURLY)
# -----------------------------
solar_pos = location.get_solarposition(times)

solar_zenith  = solar_pos["zenith"]
solar_azimuth = solar_pos["azimuth"]

# -----------------------------
# 3. AIR MASS (HOURLY)
# -----------------------------
air_mass = pvlib.atmosphere.get_relative_airmass(
    solar_zenith,
    model="kastenyoung1989"
)

# -----------------------------
# 4. CLEAR-SKY IRRADIANCE (HOURLY)
# -----------------------------
clearsky = location.get_clearsky(
    times,
    model="ineichen"
)

clear_sky_ghi = clearsky["ghi"]   # W/m²
clear_sky_dni = clearsky["dni"]   # W/m²

# -----------------------------
# 5. HOURLY DATAFRAME
# -----------------------------
df_hourly = pd.DataFrame({
    "solar_zenith": solar_zenith,
    "solar_azimuth": solar_azimuth,
    "air_mass": air_mass,
    "clear_sky_ghi": clear_sky_ghi,
    "clear_sky_dni": clear_sky_dni
})

# -----------------------------
# 6. DAILY AGGREGATION (KEY PART)
# -----------------------------
df_daily = pd.DataFrame()

# 🔹 ENERGY TERMS → SUM (Wh/m²/day)
df_daily["clear_sky_ghi_wh"] = df_hourly["clear_sky_ghi"].resample("D").sum()
df_daily["clear_sky_dni_wh"] = df_hourly["clear_sky_dni"].resample("D").sum()

# 🔹 GEOMETRY TERMS → MEAN
df_daily["solar_zenith_mean"]  = df_hourly["solar_zenith"].resample("D").mean()
df_daily["solar_azimuth_mean"] = df_hourly["solar_azimuth"].resample("D").mean()
df_daily["air_mass_mean"]      = df_hourly["air_mass"].resample("D").mean()

# -----------------------------
# 7. OPTIONAL UNIT CONVERSION
# -----------------------------
df_daily["clear_sky_ghi_kwh"] = df_daily["clear_sky_ghi_wh"] 
df_daily["clear_sky_dni_kwh"] = df_daily["clear_sky_dni_wh"] 

# -----------------------------
# 8. CLEANING (OPTIONAL)
# -----------------------------
# Remove days with almost no sun (very rare but safe)
df_daily = df_daily[df_daily["clear_sky_ghi_wh"] > 500]

# -----------------------------
# 9. SAVE RESULT
# -----------------------------
print(df_daily.head())
df_daily.to_csv("pvlib_clear_sky_daily_features.csv")
