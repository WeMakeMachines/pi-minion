_pinion - a small cog which engages the teeth of a larger wheel_

# pinion.weather 😈⛅

- a small weather microservice

## Features

- Uses OpenWeatherMap API v2.5
- Keeps a local cache of the response data

## Operation

### Routes

- `/now` - returns the weather now
- `/hourly` - returns the weather for the next 48 hours
- `/daily` - returns the forecast for the next 8 days

### Parameters

- `units=` - can be either `metric` or `imperial`

### Cache

#### Disable caching

If you want to disable system file writes, add to the `.env` file `DISABLE_CACHING` set to `True`

#### Deleting cache

Cached files are written to `/cache`

To delete the cache, simply delete this folder

## Setting up development (Linux)

### Setup Python 3

`sudo apt-get install python3 python-pip python3-venv`

### Setup

Create a `.env` file from the `.env.example`

```
python3 -m venv ./venv/
```

### Running

```
. venv/bin/activate
pip install -r requirements.txt
flask run --host=0.0.0.0
```
