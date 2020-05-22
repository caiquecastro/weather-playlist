from fastapi import FastAPI
from app.core.config import settings
from app.services.spotify import spotify_service
from app.services.openweather import openweather_service


def create_app():
    app = FastAPI(title=settings.PROJECT_NAME)

    @app.get('/cities/{city}/playlists')
    def city_playlists(city):
        temperature = openweather_service.get_temperature(city)

        playlist = spotify_service.get_playlist_for_temperature(temperature)

        return {
            'city': city,
            'temperature': temperature,
            'playlist': playlist,
        }

    return app
