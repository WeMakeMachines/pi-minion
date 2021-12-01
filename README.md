_pinion - the smaller wheels turns the larger ..._

# pinion.weather 😈⛅

A microservice which best serves applications that make uncommon and unpredictable requests for weather information

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

## Configuring

### config.ini

Follow the example from `config_example.ini`

- `CACHE_EXPIRES_AFTER`
   > `integer`
   > 
   > number of minutes the cache is valid for, i.e, _60_ for 1 hour
   
   > `string`
   > 
   > **today** - cache only valid for today (up till midnight)
   > 
   > **disable** - disables all cache requests

## System Dependencies (Linux)

- python >= 3.9.5
- pip
- pipenv or pythonenv

See the guide [Installing memcached on Linux](./INSTALLING_MEMCACHED.md)
See the guide [Installing Python Dependencies on Linux](./INSTALLING_PYTHON_DEPENDENCIES.md)

## Setup

> Make sure your `config.ini` is properly setup!

### Deploying on Linux

For production, it is recommended not to use pipenv

1. Create the virtual environment

   ```bash
   python3 -m venv ./venv/
   ```

2. Activate the virtual environment
   
   ```bash
   . venv/bin/activate
   ```
   
3. Install the requirements
   
   ```bash
   pip install -r requirements.txt
   ```

4. Running the following script will setup **pinion.weather** as a systemd service on Linux

   ```bash
   ./register-service.sh
   ```

You can interact with the service with the following commands

```bash
systemctl start pinion.weather
systemctl stop pinion.weather
systemctl status pinion.weather
```

### Development on Linux

To test the server, run the following command within the virtual environment

```bash
pipenv run uvicorn app.main:app --host 0.0.0.0 --reload
```
