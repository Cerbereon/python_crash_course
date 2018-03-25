'''Start with the program you wrote for Exercise 6-1 (page 102). Make two new
dictionaries representing different people, and store all three dictionaries
in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person.'''

me = {
    'first name' : 'max',
    'last name' : 'korenev',
    'age' : 19,
    'city' : 'moscow',
}

jane = {
    'first name' : 'jane',
    'last name' : 'aldridge',
    'age' : 18,
    'city' : 'portland',
}

shelley = {
    'first name' : 'shelley',
    'last name' : 'abramson',
    'age' : 19,
    'city' : 'reno',
}

people = [me, jane, shelley]

for person in people:
    full_name = person['first name'] + " " + person['last name']

    print("\nFull name is " + full_name.title())
    print(str(person['age']) + " y.o.")
    print("Lives in " + person['city'].title())