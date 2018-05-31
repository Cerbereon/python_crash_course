'''
Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
'''

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.readlines()
    except FileNotFoundError:
        pass
    else:
        print(contents)
