_pinion - a small cog which engages the teeth of a larger wheel_

# pinion.weather 😈⛅

- a small weather microservice

## Features

- Uses OpenWeatherMap API
- caches response data

## Dependencies

- Python 3.9.5
- faster_than_requests
- Flask
- python-dotenv

## Setup

1. Create a `.env` file from the `.env.example`
2. `pip install -r requirements.txt`
3. `. venv/bin/activate`
4. `flask run`

## Routes

- `/weather/now` - returns the weather now
- `/weather/hourly` - returns the weather for the next 48 hours
- `/weather/daily` - returns the forecast for the next 8 days

