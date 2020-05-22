import requests
from .cache import cache
from ..core.config import settings

class OpenWeatherService:
    def __init__(self):
        self.endpoint = 'https://api.openweathermap.org/data/2.5/weather'
        self.cache_prefix = 'temperature:'
        self.app_id = settings.OPENWEATHER_API_KEY

    def get_temperature(self, location):
        cache_key = f'{self.cache_prefix}{location}'
        cached_temperature = cache.get(cache_key)

        if cached_temperature is not None:
            return int(cached_temperature)

        temperature = self.fetch_temperature(location)

        cache.set(cache_key, temperature, expire=3600)

        return temperature

    def fetch_temperature(self, location):
        url = f'{self.endpoint}?q={location}&appid={self.app_id}&units=metric'

        response = requests.get(url)

        response.raise_for_status()

        response_json = response.json()

        return response_json['main']['temp']


openweather_service = OpenWeatherService()