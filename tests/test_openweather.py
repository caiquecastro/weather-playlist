import responses
from app.services.openweather import OpenWeatherService

class FakeCache:
    def __init__(self):
        self.data = {}

    def get(self, key):
        return self.data[key] if key in self.data else None

    def set(self, key, value, expire=None):
        self.data[key] = value


city_temperature_response = {
    'main': {
        'temp': 22
    }
}

@responses.activate
def test_fetch_city_temperature_from_api():
    fake_cache = FakeCache()
    responses.add(
        responses.GET,
        'https://api.openweathermap.org/data/2.5/weather',
        json=city_temperature_response
    )

    service = OpenWeatherService(fake_cache)
    temperature = service.get_temperature('Itatiba')
    assert temperature == 22


def test_fetch_city_temperature_from_cache():
    fake_cache = FakeCache()
    fake_cache.set('temperature:Itatiba', 12)

    service = OpenWeatherService(fake_cache)
    temperature = service.get_temperature('Itatiba')
    assert temperature == 12
