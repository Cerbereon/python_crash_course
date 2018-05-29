'''
Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
'''


def make_album(artist, title, number_of_tracks = ''):
    album = {'artist':artist.title(), 'title':title.title()}
    if number_of_tracks:
        album['number of tracks'] = number_of_tracks
    return album

while True:
    print('\nInput artist, title of album and optionally number of tracks:')
    print("(input 'quit' to quit")
    art = input('Artist: ')
    if art == 'quit':
        break
    title = input('Title: ')
    if title == 'quit':
        break
    number = input('Number of tracks: ')
    if number == 'quit':
        break

    album = make_album(art, title, number)
    print(album)