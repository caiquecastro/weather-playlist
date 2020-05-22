import spotipy
import requests
from fastapi import FastAPI
from app.core.config import settings
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def get_city_temperature(city):
    app_id = ''
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_id}&units=metric'

    response = requests.get(url)

    response_json = response.json()

    return response_json['main']['temp']


def get_track_name(item):
    return item['track']['name']


def get_temperature_playlist(temperature):
    playlists = get_temperature_playlists(temperature)

    first_playlist = playlists['playlists']['items'][0]

    playlist_tracks = sp.playlist_tracks(first_playlist['id'])

    return list(map(get_track_name, playlist_tracks['items']))

def get_temperature_playlists(temperature):
    if temperature > 25:
        return sp.category_playlists('pop')
    
    if temperature >= 10:
        return sp.category_playlists('rock')

    return sp.category_playlists('classical')


app = FastAPI(title=settings.PROJECT_NAME)


@app.get('/cities/{city}/playlists')
def city_playlists(city):
    city_temperature = get_city_temperature(city)

    playlist = get_temperature_playlist(city_temperature)
    
    return {
        'city': city,
        'temperature': city_temperature,
        'playlist': playlist,
    }