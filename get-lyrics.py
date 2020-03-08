import configparser
import webbrowser
import spotipy
import spotipy.util as util

config = configparser.ConfigParser()
config.read("config.ini")

username = config["Authentication"]["username"]
scope = config["Authentication"]["scope"]
client_id = config["Authentication"]["client_id"]
client_secret = config["Authentication"]["client_secret"]
redirect_uri = config["Authentication"]["redirect_uri"]

browser = config["Browser"]["browser"]

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_playing_track()
    is_playing = results["is_playing"]

    if is_playing:
        song = results["item"]["name"]
        artist = results["item"]["artists"][0]["name"]

        genius_url = "https://genius.com/" + artist.replace(" ", "-") + "-" + song.replace(" ", "-") + "-" + "lyrics"
        musixmatch_url = "https://www.musixmatch.com/lyrics/" + artist.replace(" ", "-") + "/" + song.replace(" ", "-")

        print("Song: " + song)
        print("Artist: " + artist)
        print("Genius lyrics URL: " + genius_url)
        print("Musixmatch lyrics URL: " + musixmatch_url)

        webbrowser.get(browser).open_new_tab(genius_url)
        webbrowser.get(browser).open_new_tab(musixmatch_url)

    else:
        print("Not currently playing")
