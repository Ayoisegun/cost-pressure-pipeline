import requests
import pandas as pd
import time

try:
    city_df = pd.read_csv("city_data.csv")
except FileNotFoundError:
    print("Error: city_data.csv not found.")
    city_df = pd.DataFrame()

all_weather_data = []

#Loop through each row in the city dataframe
for index, row in city_df.iterrows():
    city = row['capitalCity']
    lat = row['latitude']
    lon = row['longitude']
    
    print(f"Fetching data for {city}...")

    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": "2023-01-01",
        "end_date": "2023-12-31",
        "daily": ["temperature_2m_mean", "precipitation_sum"],
        "timezone": "auto"
    }

    try:
        r = requests.get(url, params=params)
        
        if r.status_code == 200:
            data = r.json()
            # Create a dataframe for this specific city
            temp_df = pd.DataFrame(data['daily'])
            
            # Add the city name so as to know where the weather data came from
            temp_df['city'] = city
            
            # Append this city's data to our list
            all_weather_data.append(temp_df)
        else:
            print(f"Failed to fetch {city}. Status: {r.status_code}")
        time.sleep(0.1) 
        
    except Exception as e:
        print(f"Error processing {city}: {e}")

# 3. Combine all individual city dataframes into one master dataframe
if all_weather_data:
    final_weather_df = pd.concat(all_weather_data, ignore_index=True)
    
    # Cleaning
    final_weather_df = final_weather_df.dropna(subset=["temperature_2m_mean", "precipitation_sum"])
    
    print("\nSample of combined data:")
    print(final_weather_df.head())
    final_weather_df.to_csv("./global_weather_2023.csv", index=False)
    print("\nFile saved as global_weather_2023.csv")
else:
    print("No weather data was collected.")
