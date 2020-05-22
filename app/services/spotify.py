import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyService:
    def __init__(self):
        credentials = SpotifyClientCredentials()
        self.client = spotipy.Spotify(client_credentials_manager=credentials)

    def _get_temperature_playlists(self, temperature):
        if temperature > 25:
            return self.client.category_playlists('pop')

        if temperature >= 10:
            return self.client.category_playlists('rock')

        return self.client.category_playlists('classical')

    def get_playlist_for_temperature(self, temperature):
        try:
            playlists = self._get_temperature_playlists(temperature)

            playlist_tracks = self.client.playlist_tracks(
                playlists['playlists']['items'][0]['id']
            )

            return [{
                'name': item['track']['name'],
                'track': item['track'],
            } for item in playlist_tracks['items']]
        except Exception as er:
            return []


spotify_service = SpotifyService()
