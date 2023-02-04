# Weather Forecast Program
# This program sends me a text message with the day's forecasted
# temperature and weather events for my location.

import requests

# Personal API key for the Open Weather Map site.
API_KEY = "600410297fd95c728b0329c3587e78ea"

# The "Current weather data" API endpoint.
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Coordinates for Boise, ID
MY_LATITUDE = 43.618881
MY_LONGITUDE = -116.215019

MY_NAME = "Heather"

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY,
    "units": "imperial"
}

# Send an API request to the Open Weather Map site.
response = requests.get(url=API_URL, params=parameters)

# If there was an API error, print it to the console.
response.raise_for_status()

# Get the data from the JSON.
data = response.json()
weather_type = data["weather"][0]["main"]
weather_desc = data["weather"][0]["description"]
temp = data["main"]["temp"]
temp_min = data["main"]["temp_min"]
temp_max = data["main"]["temp_max"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
cloud_percentage = data["clouds"]["all"]

print(data)

output_str = f"Hello, {MY_NAME}!"
output_str += f"\nThe main weather right now is: {weather_type} ({weather_desc})."
output_str += f"\nThe current temperature is {temp}°F, but it feels like {feels_like}°F."
output_str += f"\nCurrent temperatures are between {temp_min} and {temp_max}°F."
output_str += f"\nThe humidity is {humidity}% and the wind speed is {wind_speed} mph."

print(output_str)