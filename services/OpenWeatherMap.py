import requests
import json

from models.Weather import Clouds, Sun, Temperature, Wind

class OpenWeatherMap:
    def __init__(self, apiKey: str, latitude: float, longitude: float, units: str = "metric"):
        self.apiKey = apiKey
        self.latitude = latitude
        self.longitude = longitude
        self.units = units
        
    def __parseHourlyObject(self, object):
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
    
    def __parseDailyObject(self, object):
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
            'now': self.__parseHourlyObject(now)
        }
    
    def hourly(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.apiKey}&units={self.units}&exclude=current,minutely,daily,alerts")
        
        data = json.loads(response.text)
        
        hourly = []
        
        for item in data['hourly']:
            hourly.append(self.__parseHourlyObject(item))

        return {
            'hourly': list(hourly)
        }

    def daily(self, days: int):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.apiKey}&units={self.units}&exclude=current,minutely,hourly,alerts")
        
        data = json.loads(response.text)   
        daily = []
        
        count = 0
        
        while (count < days):
            daily.append(self.__parseDailyObject(data['daily'][count]))
            count += 1

        return {
            'daily': list(daily)
        }
