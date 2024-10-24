import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get("OWM_API")
MY_LAT = 49.162781
MY_LONG = -123.136650
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
AUTH_TOKEN = os.environ.get("AUTH_TKN")
ACC_SID = "id"
print(os.environ.get("OWM_API"))
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(WEATHER_ENDPOINT, params=weather_params)
# print(response.status_code)
response.raise_for_status()

weather_data = response.json()
for h in weather_data["list"]:
    if h["weather"][0]["id"] < 700:
        client = Client(ACC_SID, AUTH_TOKEN)
        message = client.messages.create(
            body="It's going to rain today. Bring an umbrella!",
            from_="+14043695348",
            to="+16726713688",
        )
        print(message.status)
        break
