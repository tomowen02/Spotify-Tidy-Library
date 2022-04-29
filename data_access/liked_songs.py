def get_all_ids(spotify):
    response = spotify.current_user_saved_tracks()

    ids = set()
    ids = __add_track_ids_to_set(response, ids)
    while response['next']:
        response = spotify.next(response)
        ids = __add_track_ids_to_set(response, ids)

    return ids

    



# Private functions
def __add_track_ids_to_set(response, id_set):
    for item in response['items']:
        id = item['track']['id']
        id_set.add(id)
    return id_set