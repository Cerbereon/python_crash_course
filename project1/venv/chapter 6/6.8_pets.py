'''Make several dictionaries, where the name of each dictionary is the name
of a pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.'''

luminarie = {
    'name' : 'luminarie',
    'species' : 'cat',
    'owner_name' : 'nechtan',
}

wiggles = {
    'name' : 'wiggles',
    'species' : 'hamster',
    'owner_name' : 'gunnvaldr',
}

eleuia = {
    'name' : 'eleuia',
    'species' : 'horse',
    'owner_name' : 'gisila',
}

pets = [luminarie, wiggles, eleuia]

for pet in pets:
    print(pet['name'].title() + " is " + pet['owner_name'].title() + "'s " +
          pet['species'] + ".")