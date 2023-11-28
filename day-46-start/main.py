from datetime import datetime
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

user_choice = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD")
URL = ("https://www.billboard.com/charts/hot-100/" + user_choice)
print(URL)

response = requests.get(URL)
top_100_web_page = response.text

soup = BeautifulSoup(top_100_web_page, "html.parser")
song_names = soup.select("li ul li h3")
list_of_song_names = []
for loop in song_names:
    song_title = loop.get_text(strip=True)
    list_of_song_names.append(song_title)
song_names = soup.select("li ul li span", class_="c-label")
print(song_names)

print(list_of_song_names)


user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# song_title = soup.find(name="h3", id="title-of-a-story")
# print(song_title)



# from bs4 import BeautifulSoup
# import requests
#
# date = "2012-12-12" # input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#
# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)



