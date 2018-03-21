'''Ordinal numbers indicate their position in a list, such as 1st or 2nd.
Most ordinal numbers end in th, except 1, 2, and 3.
    • Store the numbers 1 through 30 in a list.
    • Loop through the list. • Use an if-elif-else chain inside the loop to
    print the proper ordinal ending for each number. Your output should read
    "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a
    separate line.'''

numbers = list(range(1,31))

for number in numbers:
    if number % 10 == 1 and number != 11:
        print(str(number) + "st")
    elif number % 10 == 2 and number != 12:
        print(str(number) + "nd")
    elif number % 10 == 3 and number != 13:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")