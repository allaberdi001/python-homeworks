import requests

API_KEY = "7dc555a05f943bd5c7b43762a335a085"  
CITY = "Tashkent" 
URL = f"https://api.openweathermap.org/data/2.5/weather?lat=41.2995&lon=69.2401&appid=7dc555a05f943bd5c7b43762a335a085&units=metric"
response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_desc = data["weather"][0]["description"]
    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_desc.capitalize()}")
else:
    print(f"Error: Can't to get weather data (Status Code: {response.status_code})")