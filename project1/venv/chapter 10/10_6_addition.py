'''
One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int , you’ll get a TypeError . Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
'''

print("Give me 2 number, and I will add them together.")
print("Enter 'q' to exit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Enter a number.\n")
    else:
        print(answer)