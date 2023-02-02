# A program that gets the current location of the International Space Station.

# Every 5 seconds, it uses an API request to get the current latitude/longitude 
# of the ISS and prints which location on Earth it is currently flying over.

import datetime
import time
import requests
from geopy.geocoders import Nominatim

SPACE_ART = """
        _____
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_, '.
 /;   '/    ,  _`.- \\
| '`. (`     /` ` \` |  ☀  International Space Station  ☽
|:.  `\`-.   \_   /  |           Location Tracker
|     (   `,  .`\ ;' |
 \     | .'     `-' /
  `.   ;/         .'
    `'-._______. '
"""

def get_iss_location():
    """Get the current location of the ISS."""
    # Get live data from the ISS API.
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")

    # If there was an API error, print it to the console.
    response_iss.raise_for_status()

    # Get the current latitude and longitude of the ISS.
    iss_data = response_iss.json()
    iss_latitude = iss_data["iss_position"]["latitude"]
    iss_longitude = iss_data["iss_position"]["longitude"]
    iss_loc_str = f"{iss_latitude}, {iss_longitude}"

    # Get the nearest city to these coordinates.
    geolocator = Nominatim(user_agent="iss-location")
    location_nativelang = geolocator.reverse(iss_loc_str)
    location_eng = geolocator.reverse(iss_loc_str, language='en')

    # Print the current time in 12-hr format ("12:34:15 PM").
    current_day = datetime.date.today().strftime("%b %d, %Y")
    t = time.localtime()
    current_time = time.strftime("%I:%M:%S %p (%Z)", t)
    print(f"\n{current_day} - {current_time}")

    if location_eng != None:
        print(f"The ISS is currently over {location_eng.address}.")
    else:
        print(f"The ISS is currently over the ocean.")

    print(f"(Latitude: {iss_latitude}, Longitude: {iss_longitude})")


def main():
    print("\n")
    print(SPACE_ART)

    quit_program = False
    while not quit_program:

        time.sleep(5)
        get_iss_location()

        # input_str = input("\nPlease enter X, or Q to quit:\n> ")

        # if input_str.upper() == "Q":
        #     print("\nGoodbye!\n")
        #     quit_program = True

        # else:            
        #     get_iss_location()

if __name__ == "__main__":
    main()
    
