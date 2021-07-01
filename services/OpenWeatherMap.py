import requests
import json

from models.Weather import Clouds, Sun, Temperature, Wind

# Interfaces with the OpenWeatherMap API
# Docs: https://openweathermap.org/api/one-call-api
class OpenWeatherMap:
    def __init__(self, apiKey: str, latitude: float, longitude: float, units: str = "metric"):
        self.apiKey = apiKey
        self.latitude = latitude
        self.longitude = longitude
        self.units = units
        
    def __parse_hourly_oObject(self, object):
        return {
            'time': object['dt'],
            'description': object['weather'][0]['description'],
            'clouds': Clouds(
                cloud_cover = object['clouds']
            ),
            'temperature': Temperature(
                actual = object['temp'],
                feels_like = object['feels_like']
            ),
            'wind': Wind(
                speed = object['wind_speed'],
                degrees = object['wind_deg']
            )
        }
    
    def __parse_daily_object(self, object):
        return {
            'sun': Sun(
                sunrise = object['sunrise'],
                sunset = object['sunset']
            ),
            'wind': Wind(
                speed = object['wind_speed'],
                degrees = object['wind_deg'],
                gust = object['wind_gust']
            ),
            'temperature': {
                'morning': Temperature(
                    actual = object['temp']['morn'],
                    feels_like = object['feels_like']['morn']
                ),
                'day': Temperature(
                    actual = object['temp']['day'],
                    feels_like = object['feels_like']['day']
                ),
                'evening': Temperature(
                    actual = object['temp']['eve'],
                    feels_like = object['feels_like']['eve']
                ),
                'night': Temperature(
                    actual = object['temp']['night'],
                    feels_like = object['feels_like']['night']
                ),
                'max': Temperature(
                    actual = object['temp']['max']
                ),
                'min': Temperature(
                    actual = object['temp']['min']
                )
            }
        }
                
    def now(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.apiKey}&units={self.units}&exclude=minutely,hourly,daily,alerts")
        
        data = json.loads(response.text)
        now = data['current']
        
        return {
            'sun': Sun(
                sunrise = now['sunrise'],
                sunset = now['sunset']
            ),
            'now': self.__parse_hourly_oObject(now)
        }
    
    def hourly(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.apiKey}&units={self.units}&exclude=current,minutely,daily,alerts")
        
        data = json.loads(response.text)
        
        hourly = []
        
        for item in data['hourly']:
            hourly.append(self.__parse_hourly_oObject(item))

        return {
            'hourly': list(hourly)
        }

    def daily(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.apiKey}&units={self.units}&exclude=current,minutely,hourly,alerts")
        
        data = json.loads(response.text)

        daily = []

        for day in data['daily']:
            daily.append(self.__parse_daily_object(day))

        return {
            'daily': list(daily)
        }
