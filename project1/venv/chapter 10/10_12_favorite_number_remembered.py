'''
Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
'''

import json


filename = 'favorite_number10_12.json'

try:
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)
except FileNotFoundError:
    favorite_number = input("Enter your favorite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
        print("Your favorite number is now remembered")
else:
    print("I know your favorite number! It's " + favorite_number + ".")