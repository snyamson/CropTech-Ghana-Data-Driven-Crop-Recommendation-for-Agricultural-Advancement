from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import os
from .endpoints import ip_information  # Import the router

app = FastAPI()

# Include the router from the endpoint module
app.include_router(ip_information.router, prefix="/api")

# Serve static HTML files from the "static" directory
static_path = Path(os.path.dirname(os.path.abspath(__file__))) / "static"
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Define the route to render your static HTML file
@app.get("/", response_class=HTMLResponse)
async def get_homepage():
    return open(static_path / "index.html", "r").read()