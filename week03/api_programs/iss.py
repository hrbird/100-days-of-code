# A program that gets the current location of the International Space Station
# using an API request. It uses the geopy library to show the nearest city.

import requests

# Get live data from the ISS API.
response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")

# If there was an API error, print it to the console.
response_iss.raise_for_status()

# Get the current latitude and longitude of the ISS.
iss_data = response_iss.json()
iss_latitude = iss_data["iss_position"]["latitude"]
iss_longitude = iss_data["iss_position"]["longitude"]
print(f"lat: {iss_latitude}, long: {iss_longitude}")

