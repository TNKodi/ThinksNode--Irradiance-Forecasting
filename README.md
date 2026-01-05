# ThinksNode--Irradiance-Forecasting# ThinksNode--Irradiance-Forecasting

A comprehensive solar irradiance forecasting system for Thulhiriya, Sri Lanka using multiple data sources and machine learning models.

## 📍 Location

- **Latitude:** 7.274276317883622
- **Longitude:** 80.2191266481395
- **Timezone:** Asia/Colombo (UTC+5:30)
- **Location:** Thulhiriya, Sri Lanka

## 🎯 Project Overview

This project provides GHI (Global Horizontal Irradiance) predictions using various data sources and machine learning approaches. The system integrates weather data, clear-sky models, and historical solar radiation data to generate accurate forecasts.

## 📊 Data Sources

### 1. Open-Meteo Weather Data
**Script:** [thulhirya_weather_openmeteo.py](thulhirya_weather_openmeteo.py)

Fetches daily weather aggregates including:
- Weather code
- Temperature (max/min)
- Precipitation sum
- Wind speed and gusts
- Shortwave radiation sum (solar GHI)

**Output:** [openmeteo_weather_data_daily.csv](openmeteo_weather_data_daily.csv)

### 2. PVLib Clear-Sky Model
**Script:** [thulghiriya_pvlib.py](thulghiriya_pvlib.py)

Generates clear-sky irradiance features using the Ineichen model:
- Clear-sky GHI and DNI (hourly → aggregated to daily)
- Solar position (zenith, azimuth)
- Air mass calculations
- Energy values in Wh/m²/day and kWh/m²/day

**Output:** `pvlib_clear_sky_daily_features.csv`

### 3. Solcast Historical Data
**Script:** [thulhirya_solcast.py](thulhirya_solcast.py)

Retrieves historic radiation and weather data with parameters:
- GHI (Global Horizontal Irradiance)
- DNI (Direct Normal Irradiance)
- DHI (Diffuse Horizontal Irradiance)
- GTI (Global Tilted Irradiance)

**Resolution:** Hourly (PT1H)  
**Output:** `solcast_nov_2025_1stweek_hourly.csv`

## 📁 Project Structure

```
.
├── thulhirya_weather_openmeteo.py   # Open-Meteo API integration
├── thulghiriya_pvlib.py              # PVLib clear-sky calculations
├── thulhirya_solcast.py              # Solcast historical data
├── openmeteo_weather_data_daily.csv  # Daily weather features
├── openmeteo_weather_data.csv        # Weather data
├── model_features.txt                # Model feature list
├── model_metadata.json               # Model configuration
├── fulldata/                         # Complete dataset directory
├── fulldata_daily/                   # Daily aggregated data
├── *.ipynb                           # Jupyter notebooks for analysis
└── *_predictions*.csv                # Generated forecast outputs
```

## 🔬 Notebooks

- **GHI_predictions.ipynb** - Core GHI prediction models
- **improved_model.ipynb** - Enhanced prediction algorithms
- **GHI predictions Improved with diffrent models.ipynb** - Model comparison
- **dnn_model_for ghi prediction.ipynb** - Deep Neural Network approach
- **ghi_prediction_for_location.ipynb** - Location-specific predictions
- **clearghi_daily.ipynb** - Clear-sky GHI analysis
- **daily_kt_forecast_fixed.ipynb** - Daily clearness index forecasting

## 📈 Output Files

- `ghi_predictions_Thulhiriya_Sri_Lanka.csv` - Location-specific predictions
- `future_ghi_forecast_20260105_101603.csv` - Future forecast
- `extended_ghi_forecast_7days_20260105_101621.csv` - 7-day extended forecast

## 🚀 Getting Started

### Prerequisites

```bash
pip install pvlib-python pandas requests
```

### Running Data Collection

1. **Fetch Open-Meteo weather data:**
   ```bash
   python thulhirya_weather_openmeteo.py
   ```

2. **Generate clear-sky features:**
   ```bash
   python thulghiriya_pvlib.py
   ```

3. **Download Solcast historical data:**
   ```bash
   # Add your API key to thulhirya_solcast.py
   python thulhirya_solcast.py
   ```

## 🔑 API Keys Required

- **Solcast API:** Required for historical radiation data (sign up at [solcast.com](https://solcast.com))

## 📅 Data Coverage

- **Historical Period:** 2022-01-01 to 2025-12-01
- **Forecast Horizon:** Up to 7 days
- **Temporal Resolution:** Daily aggregates (with hourly intermediate calculations)

## 🛠️ Features

The model uses various features including:
- Clear-sky irradiance (GHI, DNI)
- Solar geometry (zenith, azimuth, air mass)
- Weather conditions (temperature, precipitation, wind)
- Historical radiation measurements

See [model_features.txt](model_features.txt) for complete feature list.

## 📝 Model Metadata

Model configuration and parameters are stored in [model_metadata.json](model_metadata.json).

## 📄 License

This project is part of the ThinksNode Irradiance Forecasting initiative.

## 🤝 Contributing

For contributions and issues, please refer to the repository at [TNKodi/ThinksNode--Irradiance-Forecasting](https://github.com/TNKodi/ThinksNode--Irradiance-Forecasting).
```