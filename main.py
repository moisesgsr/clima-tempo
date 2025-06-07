import requests

api_key = "Put your key" # Your API key
api_link = "http://api.weatherapi.com/v1/current.json"

city_input = input("Enter the city to check the weather: ")
parameters = {
    "key": api_key,
    "q": city_input,
    "lang": "en", 
}

try:
    response = requests.get(api_link, params=parameters)
    response.raise_for_status() 

    weather_data = response.json()

    # Extracting specific weather information
    city_name = weather_data["location"]["name"]
    temperature_c = weather_data["current"]["temp_c"]
    feels_like_c = weather_data["current"]["feelslike_c"]
    humidity = weather_data["current"]["humidity"]
    weather_description = weather_data["current"]["condition"]["text"]
    wind_speed_kph = weather_data["current"]["wind_kph"]

    # Printing the desired weather information
    print(f"\nWeather in {city_name}:")
    print(f"  Temperature: {temperature_c}°C")
    print(f"  Feels Like: {feels_like_c}°C")
    print(f"  Humidity: {humidity}%")
    print(f"  Wind Speed: {wind_speed_kph} km/h")
    print(f"  Description: {weather_description}")

except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error querying the API: {errh}")
    if response.status_code == 400:
        print("Please check the city name. The city might not be recognized by the API.")
except requests.exceptions.ConnectionError as errc:
    print(f"Connection Error: Please check your internet connection. {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Request Timeout: The API took too long to respond. {errt}")
except requests.exceptions.RequestException as err:
    print(f"An unexpected error occurred during the request: {err}")
except KeyError as e:
    print(f"Error processing API data: Key '{e}' was not found.")
    print("The API response structure might have changed, or the request did not return the expected data.")
except Exception as e:
    print(f"An general error occurred: {e}")