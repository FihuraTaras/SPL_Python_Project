# Functions/WeatherFunctions.py
import requests

from Shared.Constants.config import API_KEY, API_URL


def get_weather(city):
    try:
        # Prepare request parameters
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Metric units ensure temperature is in Celsius
        }

        # Send GET request
        response = requests.get(API_URL, params=params)

        # Check for a successful response
        if response.status_code == 200:
            data = response.json()
            return {
                "city": data['name'],  # City name
                "temperature": data['main']['temp'],  # Temperature in Celsius
                "description": data['weather'][0]['description'].capitalize()  # Weather description
            }
        else:
            print(f"Error {response.status_code}: City '{city}' not found!")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to connect to the API. Details: {e}")
        return None

