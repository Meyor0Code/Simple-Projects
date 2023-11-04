import requests

# OpenWeatherMap API key (sign up at https://openweathermap.org/)
api_key = "YOUR_API_KEY"

# Function to get weather information
def get_weather(city_name):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"Weather in {city_name}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Failed to retrieve weather information. Please check the city name and API key.")

# Main function
def main():
    print("Text-Based Weather Application")
    city_name = input("Enter a city name: ")
    get_weather(city_name)

if __name__ == "__main__":
    main()
