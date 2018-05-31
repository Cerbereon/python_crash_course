'''
Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
'''

import json


filename = 'favorite_number.json'

with open(filename) as f_obj:
    favorite_number = json.load(f_obj)

print("I know you favorite number! It's " + favorite_number + ".")