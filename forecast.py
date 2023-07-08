import requests
import json

# Replace the API key and location with your own values
api_key = 'YOUR_API_KEY'
location = 'New York'

# Make an API request to get the weather forecast
url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}'
response = requests.get(url)
data = json.loads(response.text) //1st

# Extract the relevant information from the API response
forecast_items = data['list']
city = data['city']['name']
forecast_items = data['list']
city = data['city']['name']

# Print the forecast for the next few days
print(f'Weather forecast for {city}:')
for item in forecast_items:
    date_time = item['dt_txt']
    temperature = item['main']['temp']
    description = item['weather'][0]['description']
    print(f'{date_time}: {description}, temperature: {temperature} K')
