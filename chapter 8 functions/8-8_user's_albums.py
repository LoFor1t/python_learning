def make_album(artist, album_name):
    album_information = {
        'artist': artist,
        'album name': album_name,
    }
    return album_information


while True:
    print("\nPlease, write an information about your album:")
    print("(if you want to quit, enter 'q' in any time)")
    artist_name = input("Name of the artist: ")
    if artist_name == 'q':
        break

    album = input("Name of the album: ")
    if album == 'q':
        break

    print('Information about your album:')
    print(make_album(artist_name, album))
