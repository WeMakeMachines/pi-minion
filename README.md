_pinion - a small cog which engages the teeth of a larger wheel_

# pinion.weather 😈⛅

- a small weather microservice
- can be configured for static or mobile systems

## Features

- Uses OpenWeatherMap API v2.5
- Keeps a local cache of the response data
- Allows mixing of units as metric / imperial for speed and temperature
- Can be configured for a static location

## Operation

### Routes

- `/now` - returns the weather now
- `/hourly` - returns the weather for the next 48 hours
- `/daily` - returns the forecast for the next 8 days

### Optional Parameters

The following parameters can be omitted, if the server has been setup with defaults

- `speed=` - can be either `metric` or `imperial`
- `temp=` - can be either `metric` or `imperial`
- `lat=` - latitude co-ordinate
- `long=` - longitude co-ordinate
- `nocache=` - force pinion.weather to make a fresh request

### Cache

#### Options

Possible options for `CACHE_VALIDITY` in `.env`

- hour - cache only valid for until the end of the current hour
- today - cache only valid for today (up till midnight)
- disable - disables all cache requests

> Note: If you want to disable system file writes, set `CACHE_VALIDITY` to `disable`

#### Deleting cache

Cached files are written to `/cache`

To delete the cache, simply delete this folder

## Installation and Usage

1. Make sure you have met the following dependencies on your system:
   - python >= 3.9.5
   - python pip
   - python venv
   
   See the guide [Installing Python Dependencies on Linux](./INSTALLING_PYTHON_DEPENDENCIES.md)
   
2. Create a `.env` file from the `.env.example`
   
    `python3 -m venv ./venv/`

3. Activate the virtual environment
   
    `. venv/bin/activate`
   
4. Install the requirements
   
    `pip install -r requirements.txt`

### Deploying on Linux

Running the following script will setup **pinion.weather** as a systemd service on Linux

`./register-service.sh`

### Development on Linux

To test the server, run the following command within the virtual environment

`flask run --host=0.0.0.0`
