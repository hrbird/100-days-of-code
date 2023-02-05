# Weather Report Program

# This program sends an email to/from my personal account
# with the current temperature and weather events for my location. 

import requests
import smtplib

# Coordinates for Boise, ID
MY_LATITUDE = 43.618881
MY_LONGITUDE = -116.215019
MY_LOCATION = "Boise, ID"

# Personal API key for the Open Weather Map site.
# (replaced with dummy data for personal privacy on github)
API_KEY = "1234567890ABCDEFGHIJKLMNOP"

# Email data (replaced with dummy data for personal privacy on github)
MY_EMAIL = "example@gmail.com"
MY_PASSWORD = "abcdefghijklmnop"
EMAIL_PROVIDER = "smtp.gmail.com"

def get_weather_data() -> str:
    """Gets current weather data for a given location
    with an API request to the Open Weather Map site.

    Returns:
        str: description of current weather/temperature
    """

    # The "Current weather data" API endpoint.
    API_URL = "https://api.openweathermap.org/data/2.5/weather"

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
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]
    cloud_percentage = data["clouds"]["all"]

    # If the weather is clear or cloudy, the subject should be "Weather Report for {Location}".
    # Otherwise, the subject should be "Weather Alert for {Location}!".
    output_str = ""
    if weather_type in ("Clear", "Clouds"):
        output_str = f"Subject:Weather Report for {MY_LOCATION}"
    else:
        output_str = f"Subject:Weather Alert for {MY_LOCATION}!"

    # Build the message.
    output_str += f"\n\nThe current weather condition is {weather_type.lower()} ({weather_desc.lower()})."
    output_str += f"\nThe temperature right now is {temp}°F, but it feels like {feels_like}°F."
    output_str += f"\nThe wind speed is {wind_speed} mph, and the atmospheric pressure is {pressure}."
    output_str += f"\nThere is {humidity}% humidity and {cloud_percentage}% cloud cover."

    return output_str


def send_email(message: str):
    """Sends an email containing the given message to and from your personal email address.
    
    Args:
        message (str): the message to send
    """

    # Start encrypted SMTP connection.
    with smtplib.SMTP(EMAIL_PROVIDER) as connection:
        connection.starttls()

        # Log in to your account and send yourself an email.
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL,
            msg=message.encode('utf-8')
        )

        connection.close()

def main():
    # Get the weather message.
    weather_message = get_weather_data()

    print("\nSending email containing this message:\n")
    print(weather_message)

    # If there is a message, send it inside an email.
    if len(weather_message) > 0:
        send_email(message=weather_message)


if __name__ == "__main__":
    main()