from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .middleware.query_params import NormaliseCacheQueryParams, NormaliseLocationQueryParams, NormaliseUnitQueryParams
from .controllers.weather import open_weather_map_now, open_weather_map_hourly, open_weather_map_daily

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


@app.get("/now")
async def now(request: Request):
    return open_weather_map_now(request)


@app.get("/hourly")
async def hourly(request: Request):
    return open_weather_map_hourly(request)


@app.get("/daily")
async def daily(request: Request):
    return open_weather_map_daily(request)
