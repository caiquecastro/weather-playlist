import responses
from .openweather import OpenWeatherService

class FakeCache:
    def get(self, key):
        pass

    def set(self, key, value, expire=None):
        pass


city_temperature_response = {
    'main': {
        'temp': 34
    }
}

@responses.activate
def test_fetch_city_temperature():
    fake_cache = FakeCache()
    responses.add(
        responses.GET,
        'https://api.openweathermap.org/data/2.5/weather',
        json=city_temperature_response
    )

    service = OpenWeatherService(fake_cache)
    temperature = service.get_temperature('Itatiba')
    assert temperature == 34
