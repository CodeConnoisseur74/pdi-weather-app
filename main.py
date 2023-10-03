from __future__ import annotations

import argparse

import pyfiglet
import requests
from simple_chalk import chalk


# API Key for openWeatherMap
API_KEY = "aeaadd7bd3ef0726b64f6538463c7613"
# Base URL for OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Mapping of weather codes to weather icons
WEATHER_ICONS = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}

# construct API URL with query parameters
parser = argparse.ArgumentParser(
    description="Check the weather for a certain country/city"
)
parser.add_argument(
    "country", help="The country/city to check the weather for"
)
args = parser.parse_args()

url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

# Make API request and parse the reponse using requests module
response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error: Unable to retrieve weather information"))
    exit()

# Parse the JSON response from the API and extract the weather info
data = response.json()

# Get info from response

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

# Construct the output with the weather icons
weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels like: {feels_like}°C\n"

# Print output
print(chalk.green(output))
