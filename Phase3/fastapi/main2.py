from fastapi import FastAPI, HTTPException, Query, Request
from weather import get_coordinates,get_current,get_forecast
import httpx
import asyncio
import time
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.extension import _rate_limit_exceeded_handler


limiter = Limiter(key_func=get_remote_address)

app = FastAPI()

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

app.add_middleware(SlowAPIMiddleware)

weather_cache = {}

@app.get("/city")
@limiter.limit("10/minute")
async def city(request: Request,city_name: str = Query(min_length=1)):
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
@limiter.limit("30/minute")
async def weather(request: Request,lat: float = Query(ge=-90,le=90), lon: float = Query(ge=-180,le=180)):
    
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
        #print(weather_cache)

        return data

    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail= "Could not retrieve weather data"
        )  