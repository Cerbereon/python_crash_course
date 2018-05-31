'''
Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
'''


filename = 'guest.txt'
with open(filename, 'a') as file_object:

    running = True

    while running:
        name = input('Please enter your name: ')
        if name == 'q':
            break
        else:
            file_object.write(name + '\n')
