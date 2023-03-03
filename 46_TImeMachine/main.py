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


def get_playlist(playlist_name: str, dob_: str):
    for idx, item in enumerate(auth.current_user_playlists()['items']):
        if auth.current_user_playlists()['items'][idx]['name'] == f'{dob_.replace("-", "_")} Billboard 100':
            return auth.current_user_playlists()['items'][idx]['id']


def add_songs(uri_lists: list):
    auth.playlist_add_items(playlist_id=playlist_id, items=uri_lists)


def create_uri(song_list: list, dob_: str):
    uris = list()
    year = dob_[:4]
    logging.info(f"year is {year}")
    logging.info(f'song list is {len(song_list)}')
    # for song in song_list:
    for song in song_list:
        try:
            uris.append(auth.search(q=f'track {str(song)} year: {year}', type='track')["tracks"]["items"][0]["uri"])
        except Exception as e:
            logging.warning(f'{Exception} found in the flow')
    return uris


def create_playlist(dob_: str):
    auth.user_playlist_create(user=auth.current_user()["id"], name=f'{dob_.replace("-", "_")} Billboard 100')


if __name__ == '__main__':
    auth = authenticate()
    logging.basicConfig(level=logging.DEBUG)
    dob = input('What is the your Date of birth : YYYY-MM-DD: ')
    create_playlist(dob)
    playlist_id = get_playlist(playlist_name=f'{dob.replace("-", "_")} Billboard 100', dob_=dob)
    # scrap 100 songs
    scrap = Scraper(dob)
    # create uri list of songs
    uri_list = create_uri(scrap.get_list(), dob)
    # add song for URI
    logging.info(f'length is {len(uri_list)}')
    add_songs(uri_list)
