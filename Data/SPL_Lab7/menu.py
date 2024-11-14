from Shared.Classes.logger import Logger
from Shared.Functions.weatherFunctions import get_weather


def main7():
    logger = Logger()

    while True:
        city = input("Enter the city: ")
        if not city:
            print("Please enter a valid city name.")
            continue

        weather = get_weather(city)
        if weather:
            print(f"Weather in {weather['city']}: {weather['temperature']}°C, {weather['description']}")
            logger.log_query(city, weather)
        else:
            print(f"Could not fetch weather for {city}.")

        # Ask user if they want to check another city
        choice = input("Do you want to check another city? (y/n): ").lower()
        if choice != 'y':
            break

    # Show the query history
    logger.show_history()


if __name__ == "__main__":
    main7()