import spotipy
from spotipy.oauth2 import SpotifyOAuth
from scraper import Scraper
import logging

CLIENT_ID = '6ca6845b3caf4eafa0c7530de2d651d0'
CLIENT_SECRET = '340177e38a404d0bb99975de84035dd5'
REDIRECT_URI = 'http://example.com'


# input('PLease Enter the date where you want to travel back in format YYYY-MM-DD')
def authenticate():
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI))
    return sp


def get_playlist(playlist_name: str):
    for idx, item in enumerate(auth.current_user_playlists()['items']):
        if auth.current_user_playlists()['items'][idx]['name'] == '1996_06_09 Billboard 100':
            return auth.current_user_playlists()['items'][idx]['id']


def add_songs(uri_lists: list):
    auth.playlist_add_items(playlist_id=playlist_id, items=uri_lists)


def create_uri(song_list: list):
    year = 1996
    print(song_list)
    uris = [auth.search(q=f'track {song} year: {year}', type='track')['tracks']['href'] for song in song_list]
    print(uris)
    return uris


if __name__ == '__main__':
    auth = authenticate()
    result = auth.search(q='track: {Tha Crossroads} year:{1996}', type='track')
    uri = result['tracks']['href']
    playlist_id = get_playlist(playlist_name='1996_06_09 Billboard 100')
    # scrap 100 songs
    scrap = Scraper()
    # create uri list of songs
    uri_list = create_uri(scrap.get_list())
    # add song for URI
    add_songs(uri_list)
