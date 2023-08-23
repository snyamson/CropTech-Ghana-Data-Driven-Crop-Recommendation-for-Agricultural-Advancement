from fastapi import APIRouter
import httpx
from dotenv import load_dotenv
from os import getenv

router = APIRouter()

# Load environment variables from a .env.local file
load_dotenv('.env.local')
API_KEY = getenv('OPENWEATHER_API_KEY')



@router.get("/ip_information")
async def get_ip_information():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://ipapi.co/json/")
            if response.status_code == 200:
                ip_info = response.json()
                lon = ip_info.get("longitude")
                lat = ip_info.get("latitude")

                # Fetch weather information
                weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

                weather_response = await client.get(weather_url)
                if weather_response.status_code == 200:
                    weather_info = weather_response.json()
                    return {
                        "region": ip_info.get("region"),
                        "country": ip_info.get("country_name"),
                        "temperature": weather_info["main"].get("temp"),
                        "humidity": weather_info["main"].get("humidity"),
                    }
                else:
                    return {"error": "Failed to fetch weather information"}
            else:
                return {"error": "Failed to fetch IP information"}
    except httpx.HTTPError as e:
        return {"error": f"An error occurred: {e.request.url} - {e}"}
