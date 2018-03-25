'''Make a dictionary called cities. Use the names of three cities as keys in
your dictionary. Create a dictionary of information about each city and include
the country that the city is in, its approximate population, and one fact about
that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the
information you have stored about it.'''

cities = {
    'vienna' : {
        'country' : 'austria',
        'population' : 1889000,
        'fact' : 'The most musical city in the World'
    },

    'rotterdam' : {
        'country' : 'the netherlands',
        'population' : 631000,
        'fact' : 'Has been fully rebuild after WW2'
    },

    'shady sands' : {
        'country' : 'ncr',
        'population' : 120,
        'fact' : 'The first city of NCR',
    }
}

for city_name, city_info in cities.items():
    print(city_name.title() + " is located in " + city_info['country'].title()
          + ".")
    print("It has a population of " + str(city_info['population']) + " people.")
    print("Fact about the city: " + city_info['fact'] + ".\n")