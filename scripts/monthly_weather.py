import time
import pandas as pd
import requests
df = pd.read_csv("./global_weather_2023.csv")

df['time'] = pd.to_datetime(df['time'])
df['month'] = df['time'].dt.month

monthly_weather = df.groupby(['city', 'month']).agg({
    'temperature_2m_mean': 'mean',
    'precipitation_sum': 'sum'
}).reset_index()

#4. Rename columns for clarity
monthly_weather.columns = [
    'city', 
    'month', 
    'monthly_avg_temp', 
    'total_monthly_precipitation'
]

print("First few rowa of monthly_weather:")
print(monthly_weather.head())

monthly_weather.to_csv("./monthly_weather.csv", index=False)
print("\nFile 'monthly_weather.csv' created successfully.")