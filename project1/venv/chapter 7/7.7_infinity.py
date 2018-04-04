'''Write a loop that never ends, and run it. (To end the loop, press ctrl-C or
close the window displaying the output.)'''

promt = ("\nPlese eanter your age: ")

age = 0
while True:
    age = int(input(promt))

    if age >= 0 and age < 3:
        print("Your ticket is free.")
    elif age >= 3 and age < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")