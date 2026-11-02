import requests

from dotenv import load_dotenv
import os



# Build out the API and get a response
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_weather(city):
    params = {"q":city,"appid":API_KEY,"units":"metric"}

    try:
        response = requests.get(BASE_URL,params=params)

        if response.status_code == 200:
            data = response.json()
            print(data)
    except requests.exceptions.HTTPError:
        return False
    # if response.status_code == 200:
    #     data = response.json()
    #     return {
    #         "city" : data['name'],
    #         "temp" : data['main']["temp"],
    #         "humidity" : data['main']['humidity'],
    #         "weather" : data['weather'][0]["description"],
    #         "lat" : data['coord']["lat"],
    #         "lon" : data['coord']["lon"]
    #     }

print(get_weather("Bloemfontein"))
