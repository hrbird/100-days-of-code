# A program that gets the sunrise and sunset times for a given location 
# for each solstice and equinox in the current year.

import requests
import geopy
from geopy.geocoders import Nominatim

# Get latitude and longitude data for Boise, ID.
MY_CITY = "Boise, ID"
geolocator = Nominatim(user_agent="sunrise-sunset")
location = geolocator.geocode(MY_CITY)
my_lat = location.latitude
my_long = location.longitude

def get_sunrise_sunset_times(latitude, longitude):
    """Get today's sunrise and sunset times for a given location.

    Args:
        latitude (float): the location's latitude
        longitude (float): the location's longitude
    """

    parameters = {
        "lat": latitude,
        "long": longitude
    }

    # Get live data from the Sunrise Sunset API.
    response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

    # If there was an API error, print it to the console.
    response_sun.raise_for_status()

    # Get the data.
    if response_sun.json()['status'] == "OK":
        
        data = response_sun.json()["results"]

        print(f"\nToday's Data for {MY_CITY}:\n")
        print(f"Sunrise:    {data['sunrise']}")
        print(f"Solar noon: {data['solar_noon']}")
        print(f"Sunset:     {data['sunset']}")
        print(f"Day length: {data['day_length']} hours")

    else:
        print(f"Error getting data for the location ({latitude}, {longitude})...")

get_sunrise_sunset_times(my_lat, my_long)