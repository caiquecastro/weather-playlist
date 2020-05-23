import requests
from .cache import cache
from ..core.config import settings
from ..errors import NotFoundError


class OpenWeatherService:
    def __init__(self, cache_manager):
        self.endpoint = 'https://api.openweathermap.org/data/2.5/weather'
        self.cache_prefix = 'temperature:'
        self.app_id = settings.OPENWEATHER_API_KEY
        self.cache_manager = cache_manager

    def get_temperature(self, location):
        cache_key = f'{self.cache_prefix}{location}'
        cached_temperature = self.cache_manager.get(cache_key)

        if cached_temperature is not None:
            return int(cached_temperature)

        temperature = self.fetch_temperature(location)

        self.cache_manager.set(cache_key, temperature, expire=3600)

        return temperature

    def fetch_temperature(self, location):
        url = f'{self.endpoint}?q={location}&appid={self.app_id}&units=metric'

        response = requests.get(url)

        if response.status_code == 404:
            raise NotFoundError()

        response.raise_for_status()

        response_json = response.json()

        return response_json['main']['temp']


openweather_service = OpenWeatherService(cache)
