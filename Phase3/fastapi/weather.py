import os
from dotenv import load_dotenv
import httpx
import asyncio
import json
from datetime import datetime



load_dotenv()


OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/geo/1.0/direct"



async def get_coordinates(city_name: str):

    if not OPENWEATHER_API_KEY:
        raise RuntimeError("Weather API key is not configured")

    async with httpx.AsyncClient() as client:
        
        response = await client.get(
            BASE_URL,
            params={
                "q": city_name,
                "limit": 5,
                "appid": OPENWEATHER_API_KEY
            }
        )

        response.raise_for_status()

        data_response = response.json()
        
        locations = {}
        for i,data in enumerate(data_response,start=1):
            
            name = data.get("name")
            lat = data.get("lat")
            lon = data.get("lon")
            country = data.get("country")
            state = data.get("state")
            locations[i] = {
                'name': name, 
                'lat': lat, 
                'lon': lon, 
                'country': country, 
                'state': state
                }

        return locations


async def get_current(lat,lon):
    URL = "https://api.openweathermap.org/data/2.5/weather"
    
    if not OPENWEATHER_API_KEY:
        raise RuntimeError("Weather API key is not configured")
    
    async with httpx.AsyncClient() as client:
        response = await client.get(
            URL,
            params={
                "lat": lat,
                "lon": lon,
                "units": "metric",
                "appid": OPENWEATHER_API_KEY
            }
        )

        response.raise_for_status()

        data_response = response.json()
        
        return data_response




async def get_forecast(lat,lon):
    URL = "https://api.openweathermap.org/data/2.5/forecast"

    if not OPENWEATHER_API_KEY:
        raise RuntimeError("Weather API key is not configured")
        
    
    async with httpx.AsyncClient() as client:

        response = await client.get(
            URL,
            params={
                "lat": lat,
                "lon": lon,
                "units": "metric",
                "appid": OPENWEATHER_API_KEY
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

        today_miday = {"12:00":False}

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

            for key, value in days.items():
                if key.startswith(today) and value["time"] == "12:00:00":
                    today_miday["12:00"] = True
                    break
            
            if days[i]["time"] == "12:00:00":
                
                data_days[day]["time"] = days[i]["time"]
                data_days[day]["icon"] = days[i]["icon"]
            
            
            elif today == day and days[i]["time"] != "12:00:00" and today_miday["12:00"] == False:
                
                if days[i]["time"] == "15:00:00":
                    data_days[day]["time"] = days[i]["time"]
                    data_days[day]["icon"] = days[i]["icon"]

                elif days[i]["time"] == "18:00:00":
                    data_days[day]["time"] = days[i]["time"]
                    data_days[day]["icon"] = days[i]["icon"]

                elif days[i]["time"] == "21:00:00":
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

            #     elif days[i]["time"] == "15:00:00":
            #         data_days[day]["time"] = days[i]["time"]
            #         data_days[day]["icon"] = days[i]["icon"]

            #     elif days[i]["time"] == "18:00:00":
            #         data_days[day]["time"] = days[i]["time"]
            #         data_days[day]["icon"] = days[i]["icon"]

            #     elif days[i]["time"] == "21:00:00":
            #         data_days[day]["time"] = days[i]["time"]
            #         data_days[day]["icon"] = days[i]["icon"]

            
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
        

# current =  asyncio.run(get_current(-27.87,28.87))
# forecast = asyncio.run(get_forecast(-27.87,28.87))


# with open("current.json","w",encoding="utf-8") as f:
#     json.dump(current,f,indent=4)

# with open("forecast.json","w", encoding="utf-8") as f:
#     json.dump(forecast,f,indent=4)





