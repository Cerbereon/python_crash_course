'''Use a dictionary to store information about a person you know. Store their
first name, last name, age, and the city in which they live. You should have
keys such as first_name, last_name, age, and city. Print each piece of
information stored in your dictionary.'''

me = {
    'first name' : 'max',
    'last name' : 'korenev',
    'age' : 19,
    'city' : 'moscow'
}

print("My name is " + me['first name'].title() + ".")
print("My surname is " + me['last name'].title() + ".")
print("I am " + str(me['age']) + " y.o.")
print("I live in " + me['city'].title() + ".")