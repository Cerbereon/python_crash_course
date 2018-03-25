'''Make a dictionary called favorite_places. Think of three names to use as
keys in the dictionary, and store one to three favorite places for each person.
To make this exercise a bit more interesting, ask some friends to name a few of
their favorite places. Loop through the dictionary, and print each person’s
name and their favorite places.'''


people = {
    'max' : ['crimea', 'finland', 'austria'],
    'jane' : ['grand canyon', 'seatle', 'prague'],
    'shelley' : ['new vegas', 'shady sands', 'boneyard'],
}

for name, places in people.items():
    print("\n" + name.title() + "'s favorite places are: ")
    for place in places:
        print(place.title())

