#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import requests
import sqlite3
import os


# In[14]:


os.makedirs("data", exist_ok=True)

df.to_csv("data/weather.csv", index=False)


# In[15]:


# extract weather information for a city using OpenWeather API
# returns the API response in JSON format
def extract_weather(city, api_key):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


API_KEY = "YOUR_API_HERE"

cities = ["Madinah", "Jeddah", "Istanbul", "London", "Cairo","Taif"]

data = []

#convert temp to Celsius

for city in cities:

    weather = extract_weather(city, API_KEY)

    if weather:
        data.append({
            "city": city,
            "temperature_c": round(weather["main"]["temp"] - 273.15,2),
            "humidity": weather["main"]["humidity"],
            "pressure": weather["main"]["pressure"]
        })


df = pd.DataFrame(data)

df.dropna(inplace=True)

# store final dataset in SQLite database
conn = sqlite3.connect("weather.db")

df.to_sql("weather_data", conn, if_exists="replace", index=False)

conn.close()

df.to_csv("data/weather.csv", index=False)

print("ETL pipeline completed")


# In[ ]:




