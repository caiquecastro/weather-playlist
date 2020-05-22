import spotipy
import requests
from fastapi import FastAPI
from app.core.config import settings
from spotipy.oauth2 import SpotifyClientCredentials
from app.services.openweather import openweather_service

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def get_track_name(item):
    return item['track']['name']


def get_temperature_playlist(temperature):
    try:
        playlists = get_temperature_playlists(temperature)

        playlist_tracks = sp.playlist_tracks(
            playlists['playlists']['items'][0]['id']
        )

        return list(map(get_track_name, playlist_tracks['items']))
    except Exception as er:
        return []

def get_temperature_playlists(temperature):
    if temperature > 25:
        return sp.category_playlists('pop')
    
    if temperature >= 10:
        return sp.category_playlists('rock')

    return sp.category_playlists('classical')


app = FastAPI(title=settings.PROJECT_NAME)


@app.get('/cities/{city}/playlists')
def city_playlists(city):
    city_temperature = openweather_service.get_temperature(city)

    playlist = get_temperature_playlist(city_temperature)
    
    return {
        'city': city,
        'temperature': city_temperature,
        'playlist': playlist,
    }