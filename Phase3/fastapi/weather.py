import os
from dotenv import load_dotenv
import httpx
import asyncio
import json
from datetime import datetime


# Load variables from .env file into os.environ
load_dotenv()


API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/geo/1.0/direct"



async def get_coordinates(city_name: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                BASE_URL,
                params={
                    "q": city_name,
                    "limit": 5,
                    "appid": API_KEY
                }
            )

            response.raise_for_status()

            data_response = response.json()
            
            jj = {}
            for i,data in enumerate(data_response,start=1):
                
                name = data.get("name")
                lat = data.get("lat")
                lon = data.get("lon")
                country = data.get("country")
                state = data.get("state")
                jj[i] = {'name': name, 'lat': lat, 'lon': lon, 'country': country, 'state': state}

            return jj

        except httpx.HTTPError as e:
            print(f"API error: {e}")
            return None

# city = input("city: ")
# fff = asyncio.run(get_coordinates(city))
    
# lat = fff[1]["lat"] 
# lon = fff[1]["lon"] 


async def get_current(lat,lon):
    URL = "https://api.openweathermap.org/data/2.5/weather"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                URL,
                params={
                    "lat": lat,
                    "lon": lon,
                    "units": "metric",
                    "appid": API_KEY
                }
            )

            response.raise_for_status()

            data_response = response.json()
            
            return data_response

        except httpx.HTTPError as e:
            print(f"API error: {e}")
            return None



async def get_forecast(lat,lon):
    URL = "https://api.openweathermap.org/data/2.5/forecast"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                URL,
                params={
                    "lat": lat,
                    "lon": lon,
                    "units": "metric",
                    "appid": API_KEY
                }
            )

            response.raise_for_status()

            data_response = response.json()
            
            # return data_response
            data_hour = {}
            days = {}
            data_days = {}
            days_min_max = {}
            data = {}


            for i in range(9):
                data_hour[f"time{i+1}"] = {
                "time": data_response["list"][i]["dt_txt"].split()[1],
                "temp": int(data_response["list"][i]["main"]["temp"]),
                "rain": int(data_response["list"][i]["pop"] * 100),
                "icon": data_response["list"][i]["weather"][0]["icon"]
                }

            
            for i in range(len(data_response["list"])):
                date_str = data_response["list"][i]["dt_txt"]
                dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                day_name = dt_obj.strftime("%A")
                today = datetime.now().strftime("%A")


                
                days[f"{day_name}{i}"]= {
                    "time": data_response["list"][i]["dt_txt"].split()[1],
                    "temp": data_response["list"][i]["main"]["temp"],
                    "rain": data_response["list"][i]["pop"],
                    "icon": data_response["list"][i]["weather"][0]["icon"]
                }

            for i in days:
                day = ''.join(filter(str.isalpha,i))

                if day not in data_days:
                    data_days[day] = {
                        "time": "",
                        "temp": [],
                        "rain": [],
                        "icon": ""
                    }

                data_days[day]["temp"].append(days[i]["temp"])
                data_days[day]["rain"].append(days[i]["rain"])
                
                if days[i]["time"] == "12:00:00":
                    data_days[day]["time"] = days[i]["time"]
                    data_days[day]["icon"] = days[i]["icon"]

                else:
                    if days[i]["time"] == "00:00:00":
                        data_days[day]["time"] = days[i]["time"]
                        data_days[day]["icon"] = days[i]["icon"]

                    elif days[i]["time"] == "03:00:00":
                        data_days[day]["time"] = days[i]["time"]
                        data_days[day]["icon"] = days[i]["icon"]

                    elif days[i]["time"] == "06:00:00":
                        data_days[day]["time"] = days[i]["time"]
                        data_days[day]["icon"] = days[i]["icon"]

                    elif days[i]["time"] == "09:00:00":
                        data_days[day]["time"] = days[i]["time"]
                        data_days[day]["icon"] = days[i]["icon"]

                    elif days[i]["time"] == "15:00:00":
                        data_days[day]["time"] = days[i]["time"]
                        data_days[day]["icon"] = days[i]["icon"]

                    elif days[i]["time"] == "18:00:00":
                        data_days[day]["time"] = days[i]["time"]
                        data_days[day]["icon"] = days[i]["icon"]

                    elif days[i]["time"] == "21:00:00":
                        data_days[day]["time"] = days[i]["time"]
                        data_days[day]["icon"] = days[i]["icon"]
            
                
            for i in data_days:
                days_min_max[i] = {
                    "min_temp": int(min(data_days[i]["temp"])),
                    "max_temp": int(max(data_days[i]["temp"])),
                    "rain": int((sum(data_days[i]["rain"])/len(data_days[i]["rain"])) * 100),
                    "icon": data_days[i]["icon"]
                }

            data["hours"] = data_hour
            data["days"] = days_min_max
            return data
            



        except httpx.HTTPError as e:
            print(f"API error: {e}")
            return None

# current =  asyncio.run(get_current(lat,lon))
#forecast = asyncio.run(get_forecast(-27.87,28.87))


# with open("current.json","w",encoding="utf-8") as f:
#     json.dump(current,f,indent=4)

# with open("forecast.json","w", encoding="utf-8") as f:
#     json.dump(forecast,f,indent=4)





