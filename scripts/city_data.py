import requests
import pandas as pd

url = "https://api.worldbank.org/v2/country?format=json&per_page=300"
r = requests.get(url)
json_data = r.json()

if len(json_data) > 1 and json_data[1] is not None:
    actual_data = json_data[1]
    df = pd.DataFrame(actual_data)
    city_data = df[['name', 'capitalCity', 'longitude', 'latitude']].copy()
    city_data = city_data.replace('', pd.NA)
    city_data = city_data.dropna(subset=['capitalCity', 'longitude', 'latitude'])
    city_data['latitude'] = pd.to_numeric(city_data['latitude'], errors='coerce')
    city_data['longitude'] = pd.to_numeric(city_data['longitude'], errors='coerce')
    city_data = city_data.dropna()

    print(f"Cleaned data shape: {city_data.shape}")
    print(city_data.head())
    city_data.to_csv("./city_data.csv", index=False)
    print("\nFile 'city_data.csv' has been created successfully.")
                
else:
    print("No data received or invalid response structure")
