from fastapi import FastAPI
from .endpoints import ip_information  # Import the router

app = FastAPI()

# Include the router from the endpoint module
app.include_router(ip_information.router, prefix="/api")
