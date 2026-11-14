from fastapi import FastAPI, HTTPException, Query
from weather import get_coordinates,get_current,get_forecast
import httpx
import asyncio

app = FastAPI()

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
    try:
        current, forecast = await asyncio.gather(
            get_current(lat,lon),
            get_forecast(lat,lon)
        )  

        return {
            "current": current,
            "forecast": forecast
        }

    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail= "Could not retrieve weather data"
        )  