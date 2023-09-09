import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/2022-12-10/"

response = requests.get(BILLBOARD_URL)
html_text = response.text

bs = BeautifulSoup(html_text, 'html.parser')
titles = bs.select("li ul li h3")

song_names = [song.getText().strip() for song in titles]

with open('Week-7/Spotify Playlist/song_lists.txt', 'w') as songs_file:
  for song in song_names:
    songs_file.write(f'{song}\n')
  