import spotipy
from spotipy.oauth2 import SpotifyOAuth
from scraper import Scraper

CLIENT_ID = '6ca6845b3caf4eafa0c7530de2d651d0'
CLIENT_SECRET = '340177e38a404d0bb99975de84035dd5'
REDIRECT_URI = 'http://example.com'


# input('PLease Enter the date where you want to travel back in format YYYY-MM-DD')
def authenticate():
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI))
    return sp


if __name__ == '__main__':
    auth = authenticate()
    print(auth.current_user_playlists())
    track = auth.track('track: {Tha Crossroads} year:{1996}')
    print(track)
    scrap = Scraper()
    scrap.get_list()

