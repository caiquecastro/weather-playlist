from fastapi import FastAPI
from app.core.config import settings
from app.services.openweather import openweather_service
from app.services.spotify import spotify_service


app = FastAPI(title=settings.PROJECT_NAME)


@app.get('/cities/{city}/playlists')
def city_playlists(city):
    city_temperature = openweather_service.get_temperature(city)

    playlist = spotify_service.get_playlist_for_temperature(city_temperature)
    
    return {
        'city': city,
        'temperature': city_temperature,
        'playlist': playlist,
    }
