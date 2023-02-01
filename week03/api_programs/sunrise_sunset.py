# A program that gets the sunrise and sunset times for a given location 
# for each solstice and equinox in the current year.

import requests
from geopy.geocoders import Nominatim

def get_sunrise_sunset_times(latitude, longitude, location_name):
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

        print(f"\nToday's Data for {location_name}:\n")
        print(f"Sunrise:    {data['sunrise']}")
        print(f"Sunset:     {data['sunset']}")
        print(f"Day length: {data['day_length']} hours")

    else:
        print(f"Error getting data for the location {location_name}...")

def main():
    print("Welcome to the Sunrise-Sunset Times program.")

    quit_program = False
    while not quit_program:

        input_str = input("\nPlease enter a location, or Q to quit:\n> ")

        if input_str.upper() == "Q":
            print("\nGoodbye!\n")
            quit_program = True

        else:
            # Get the lat/long data for the given location.
            geolocator = Nominatim(user_agent="sunrise-sunset")
            location = geolocator.geocode(input_str)
            my_lat = location.latitude
            my_long = location.longitude

            get_sunrise_sunset_times(my_lat, my_long, location.address)

if __name__ == "__main__":
    main()
    

