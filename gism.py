import requests
from bs4 import BeautifulSoup

# Specify the URL of the Gismeteo page for the desired location
url = 'https://www.gismeteo.com/weather-london-4368/'

# Send a GET request to fetch the page content
response = requests.get(url)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the forecast information
forecast = soup.find('div', class_='tab-content')
today_weather = forecast.find('div', class_='tab-content')
print(today_weather.text.strip())
