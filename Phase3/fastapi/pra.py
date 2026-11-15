from datetime import datetime
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



today_date = str(datetime.today()).split()[0]

print(today_date)


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
            return data_response
        except httpx.HTTPError as e:
                    print(f"API error: {e}")
                    return None


print(asyncio.run(get_forecast(-28.873721,27.879371,)))