from fastapi import APIRouter
import httpx

router = APIRouter()


@router.get("/ip_information")
async def get_ip_information():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://ipapi.co/json/")
            if response.status_code == 200:
                return {"ip": response.json()["ip"]}
            else:
                return {"error": "Failed to fetch IP information"}
    except httpx.HTTPError as e:
        return {"error": f"An error occurred: {e.request.url} - {e}"}
