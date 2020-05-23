import spotipy
import logging
from .cache import cache
from spotipy.oauth2 import SpotifyClientCredentials


logger = logging.getLogger(__name__)


class SpotifyService:
    def __init__(self):
        credentials = SpotifyClientCredentials()
        self.client = spotipy.Spotify(client_credentials_manager=credentials)

        self.cache_prefix = 'playlist:'

    def _get_temperature_genre(self, temperature):
        if temperature > 25:
            return 'pop'

        if temperature >= 10:
            return 'rock'

        return 'classical'

    def get_playlist_for_temperature(self, temperature):
        genre = self._get_temperature_genre(temperature)

        cache_key = f'{self.cache_prefix}{genre}'
        cached_playlist = cache.get(cache_key)

        if cached_playlist is not None:
            return cached_playlist

        playlist = self.fetch_playlist_for_genre(genre)

        self.cache_playlist(cache_key, playlist)

        return playlist

    def cache_playlist(self, cache_key, playlist):
        cache.set(cache_key, playlist, expire=3600)

    def fetch_playlist_for_genre(self, genre):
        logger.info(f'Fetching playlist for {genre}')

        try:
            playlists = self.client.category_playlists(genre)

            playlist_tracks = self.client.playlist_tracks(
                playlists['playlists']['items'][0]['id']
            )

            return [{
                'name': item['track']['name'],
            } for item in playlist_tracks['items']]
        except Exception as er:
            return None


spotify_service = SpotifyService()
