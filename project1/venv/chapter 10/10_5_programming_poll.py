'''
Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
'''


filename = 'responds.txt'
with open(filename, 'a') as file_object:

    running = True

    while running:
        response = input('Why do you love programming? ')
        if response == 'q':
            break
        else:
            file_object.write(response + '\n')