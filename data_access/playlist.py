def get_data(spotify, playlist_id):

    # Query spotify. The query returns a dictionary. 'items' is a field in the dictionary containing 100 tracks 
    response =  spotify.playlist_items(playlist_id, fields='items.track.id, items.track.name, items.track.artists, items.track.uri, next')

    tracks = []
    tracks = __add_track_to_list(response, tracks)
    # Not all the tracks in the playlist have been returned yet as the query is limited to 100 songs
    while response['next']:
        response = spotify.next(response)
        tracks = __add_track_to_list(response, tracks)
    
    return tracks # List of dictionaries containing id, track, artist, uri


def remove_tracks(spotify, playlist_id, tracks):    
    # The query needs a list of uris without the other info currently in our tracks variable
    uris = []
    for track in tracks:
        uris.append(track['uri'])

    # Only 100 tracks can be removed at once.
    while uris:
        next_to_remove = uris[0:100]
        spotify.playlist_remove_all_occurrences_of_items(playlist_id, next_to_remove)
        uris = uris[100:]




### Private functions ###
def __add_track_to_list(response, tracks):
    for item in response['items']:
        track = item['track']
        artist = track['artists'][0]

        track_to_be_returned = {
            'id':       track['id'],
            'track':     track['name'],
            'artist':   artist['name'],
            'uri':      track['uri']
        }
        tracks.append(track_to_be_returned)

    return tracks