'''Ask the user for a number, and then report whether the number is a multiple
of 10 or not.'''

number = input("Type a number and I will say if it is a multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is a multiple of 10.")
else:
    print("\nThe number " + str(number) + " is not a multiple of 10.")