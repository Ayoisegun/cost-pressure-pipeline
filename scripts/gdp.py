import requests
import pandas as pd
url = "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&per_page=5000"
r = requests.get(url)
json_data = r.json()
print(json_data)
gdp = pd.DataFrame(pd.json_normalize((json_data[1])))
gdp = gdp[['country.value', 'countryiso3code', 'date', 'value']]
print(gdp.head())
gdp.to_csv("./gdp.csv", index=False)


