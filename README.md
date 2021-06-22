# pi + minion = pinion 😈

A small home server to run on the raspberry pi, to do your bidding

## Dependencies

- Python 3.9.5
- faster_than_requests
- Flask
- python-dotenv

## What it does

- Parses weather information from OpenWeatherMap

## How to setup

1. Create a `.env` file from the `.env.example`
2. `. venv/bin/activate`
2. `flask run`

## Routes

- `/weather/now` - returns the weather now
- `/weather/hourly` - returns the weather for the next 48 hours
- `/weather/daily` - returns the forecast for the next 8 days

## TODO

- Implement caching in OpenWeatherMap module
