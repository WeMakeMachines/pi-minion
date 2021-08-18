_pinion - a small cog which engages the teeth of a larger wheel_

# pinion.weather 😈⛅

- a small weather microservice
- can be configured for static or mobile systems

## Features

- Uses OpenWeatherMap API v2.5
- Keeps an in memory cache (memcached) of the response data
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
- `lon=` - longitude co-ordinate
- `nocache=` - force pinion.weather to make a fresh request

### Cache

#### Options

Possible options for `CACHE_EXPIRES_AFTER` in `.env`

##### integer
- number of minutes the cache is valid for, i.e, _60_ for 1 hour

##### string
- _today_ - cache only valid for today (up till midnight)
- _disable_ - disables all cache requests

## Installation and Usage

### System Dependencies

##### Linux

See the guide [Installing memcached on Linux](./INSTALLING_MEMCACHED.md)

### Setup

1. Make sure you have met the following dependencies on your system:
   - python >= 3.9.5
   - python pip
   - python venv
   
   See the guide [Installing Python Dependencies on Linux](./INSTALLING_PYTHON_DEPENDENCIES.md)
   
2. Create a `.env` file from the `.env.example`

3. Create the virtual environment

    `python3 -m venv ./venv/`

4. Activate the virtual environment
   
    `. venv/bin/activate`
   
5. Install the requirements
   
    `pip install -r requirements.txt`

### Deploying on Linux

Running the following script will setup **pinion.weather** as a systemd service on Linux

`./register-service.sh`

You can interact with the service with the following commands

```
sudo systemctl start pinion.weather
sudo systemctl stop pinion.weather
sudo systemctl status pinion.weather
```

### Development on Linux

To test the server, run the following command within the virtual environment

`flask run --host=0.0.0.0`
