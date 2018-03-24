'''Use a dictionary to store people’s favorite numbers. Think of five names,
and use them as keys in your dictionary. Think of a favorite number for each
person, and store each as a value in your dictionary. Print each person’s name
and their favorite number. For even more fun, poll a few friends and get some
actual data for your program.'''

favorite_numbers = {
    'jane' : 11,
    'simon' : 6,
    'dan' : 13,
    'max' : 37,
    'alice' : 89,
}

print("Jane's favorite number is " + str(favorite_numbers['jane']) + ".")
print("Simon's favorite number is " + str(favorite_numbers['simon']) + ".")
print("Dan's favorite number is " + str(favorite_numbers['dan']) + ".")
print("Max's favorite number is " + str(favorite_numbers['max']) + ".")
print("Alice's favorite number is " + str(favorite_numbers['alice']) + ".")
