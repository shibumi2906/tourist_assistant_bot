import httpx
import os

OPENTRIP_API_KEY = os.getenv("OPENTRIP_API_KEY")

async def fetch_opentrip_attractions(lat: float, lon: float, radius: int = 5000) -> list:
    url = "https://api.opentripmap.com/0.1/en/places/radius"
    params = {
        "radius": radius,
        "lon": lon,
        "lat": lat,
        "apikey": OPENTRIP_API_KEY,
        "format": "json",
        "limit": 10,
        "rate": 2
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()
