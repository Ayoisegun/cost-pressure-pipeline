import pandas as pd
import requests

url = "https://api.worldbank.org/v2/country/all/indicator/PA.NUS.FCRF?format=json&per_page=500&date=2023"
r = requests.get(url)
data = r.json()

if len(data) > 1 and data[1] is not None:
    # Normalize the JSON data
    actual_data = pd.json_normalize(data[1])
    exchange_rate = pd.DataFrame(actual_data)
    
    # DROP rows where the value is missing
    exchange_rate = exchange_rate.dropna(subset=['value'])
    exchange_rate = exchange_rate[['country.value', 'date', 'value', 'country.id']]
    
    if not exchange_rate.empty:
        print("First few rows with actual rates:")
        print(exchange_rate[['country.value', 'date', 'value']].head())
        exchange_rate.to_csv("./exchange_rate_filtered.csv", index=False)
        print(f"\nSaved {len(exchange_rate)} records to exchange_rate_filtered.csv")
    else:
        print("No exchange rate data found for the selected criteria.")
