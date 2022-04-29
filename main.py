import spotipy
from spotipy.oauth2 import SpotifyOAuth
from data_access import liked_songs
from data_access import playlist
from time import sleep

SCOPE ='user-library-read'
CLIENT_ID ='CLIENT_ID'
CLIENT_SECRET = 'CLIENT_SECRET'
REDIRECT_URI = 'REDIRECT_URI'

spotify = sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

def remove_unsaved_songs_from_playlist(playlist_id):
    saved_track_ids = liked_songs.get_all_ids(spotify) # Set of ID strings
    playlist_tracks = playlist.get_data(spotify, playlist_id)   # List of dictionaries containing tracks.
                                                                # Fields are: id, track, artist, uri

    to_delete = []

    print('Tracks to delete from playlist: ')
    sleep(2)
    # If a track is in the playlist BUT IS NOT SAVED (/liked) by the user, add it to 'to_delete'
    for track in playlist_tracks:
        if (track['id'] in saved_track_ids) == False:
            to_delete.append(track)
            print(f"{track['artist']} - {track['track']}")

    print()
    print(f"{len(to_delete)} tracks to remove from playlist.")
    response = input("Do you want to go ahead? ")
    if response == "YES":
        playlist.remove_tracks(spotify, playlist_id, to_delete)
        print("DELETED")
    else:
        print("Cancelled")


### MAIN ###
remove_unsaved_songs_from_playlist('PLAYLIST_ID')