import requests

latitude = input("Enter the latitude: ")
longitude = input("Enter the longitude: ")

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"

response = requests.get(url)
weather_data = response.json()

current_temperature = weather_data['current_weather']['temperature']
current_windspeed = weather_data['current_weather']['windspeed']

print(f"The current temperature is {current_temperature}°C")
print(f"The current wind speed is {current_windspeed} m/s")
