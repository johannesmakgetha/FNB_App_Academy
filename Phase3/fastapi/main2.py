from fastapi import FastAPI, HTTPException, Query
from weather import get_coordinates,get_current,get_forecast
import httpx
import asyncio
import time


app = FastAPI()

weather_cache = {}

@app.get("/city")
async def city(city_name: str = Query(min_length=1)):
    try:
        results = await get_coordinates(city_name)

        if not results:
            raise HTTPException(
                status_code=404,
                detail="City not found"
            )
        return results

    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail="Could not retrieve locations"
        )


@app.get("/weather")
async def weather(lat: float, lon: float):
    
    # cache key
    cache_key = f"{lat},{lon}"

    if cache_key in weather_cache:
        cached_data, timestamp = weather_cache[cache_key]

        if time.time() - timestamp < 600:
            print("Returning cached weather")
            return cached_data
    
    try:
        current, forecast = await asyncio.gather(
            get_current(lat,lon),
            get_forecast(lat,lon)
        )  

        data = {
            "current": current,
            "forecast": forecast
        }

        #save data in cache
        weather_cache[cache_key] = (data,time.time())
        
        print("fetching fresh weather")
        print(weather_cache)

        return data

    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail= "Could not retrieve weather data"
        )  