from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .middleware.query_params import NormaliseCacheQueryParams, NormaliseLocationQueryParams, NormaliseUnitQueryParams
from .controllers.weather import open_weather_map

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(NormaliseCacheQueryParams)
app.add_middleware(NormaliseLocationQueryParams)
app.add_middleware(NormaliseUnitQueryParams)


@app.get("/")
async def weather(request: Request, now: str = None, hourly: str = None, daily: str = None):
    if now is None and hourly is None and daily is None:
        now = "now"
        hourly = "hourly"
        daily = "daily"
    return open_weather_map(request=request, now=now, hourly=hourly, daily=daily)
