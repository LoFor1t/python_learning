def make_album(artist, album_name, number_of_tracks = ''):
    album = {
        'artist': artist,
        'album name': album_name,
    }
    if number_of_tracks:
        album['number of tracks'] = number_of_tracks
    return album


print(make_album('Kizaru', 'Bandana'))
