import requests

API_KEY = ""  

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    url = f"{base_url}?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)

        
        if response.status_code == 200:
            data = response.json()

            temperature_kelvin = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            city_name = data["name"]

            # Convert Kelvin to Celsius
            temperature_celsius = temperature_kelvin - 273.15

            print("\nWeather Details")
            print("----------------------------")
            print("City:", city_name)
            print("Temperature:", round(temperature_celsius, 2), "°C")
            print("Humidity:", humidity, "%")
            print("Condition:", description.capitalize())
            print("----------------------------")

        elif response.status_code == 404:
            print("City not found. Please check the spelling.")

        else:
            print("Error:", response.status_code)

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")


city = input("Enter city name: ")
get_weather(city)
