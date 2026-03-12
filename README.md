# Weather Data ETL Pipeline

## Overview
A lightweight ETL (Extract, Transform, Load) pipeline that automates weather data collection for major cities.

## Project Structure
```text
weather-etl-pipeline/
├── data/               # Stores the output CSV files
├── Weather.py          
├── weather.db          # SQLite database (generated after running)
├── requirements.txt    
└── README.md           
```
## Tech Stack
- **Language:** Python
- **Libraries:** Pandas, Requests
- **Database:** SQLite

## Pipeline Architecture
1. **Extract:** Fetch real-time weather data from OpenWeatherMap API.
2. **Transform:**Convert temperatures from Kelvin to Celsius and clean missing values.
3. **Load:** Store data into SQLite database and export a CSV backup.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Open `Weather.py` and replace `YOUR_API_HERE` with your API key.
3. Run the script: `python Weather.py`
