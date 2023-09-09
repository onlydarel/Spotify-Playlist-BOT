import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = 'f9eac0be5e4e45f992407f90e8eb1e7c'
CLIENT_SECRET = 'ad223ddee0244588839e5f5770bb882e'
SCOPE = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='https://open.spotify.com/?', scope=SCOPE))

results = sp.current_user()

create_playlist = sp.user_playlist_create(user= results['id'], name='the day I fall in love with you.', public=False)

playlist_id = create_playlist['id']

track_uris = []

with open('Week-7/Spotify Playlist/song_lists.txt') as songs_list:
    for line in songs_list:
        song_name = line.strip()
        search_results = sp.search(q=song_name, type='track', limit=1)

        if search_results['tracks']['items']:
            track_uri = search_results['tracks']['items'][0]['uri']
            track_uris.append(track_uri)
            print(f"Added '{song_name}' to the playlist.")
        else:
            print(f"Track not found for '{song_name}'.")

add_songs = sp.user_playlist_add_tracks(user=results['id'], playlist_id=playlist_id, tracks=track_uris)