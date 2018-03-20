'''You don’t have to limit the number of tests you create to 10. If you want
to try more comparisons, write more tests and add them to conditional_tests.py.
Have at least one True and one False result for each of the following:
    • Tests for equality and inequality with strings
    • Tests using the lower() function
    • Numerical tests involving equality and inequality, greater than and less
    than, greater than or equal to, and less than or equal to
    • Tests using the and keyword and the or keyword
    • Test whether an item is in a list
    • Test whether an item is not in a list'''

string = "Let's Ride Into the Sunset Together"

print("Equality test.")
print(string == "Let's Ride Into the Sunset Together")

print("\nUnequality test.")
print(string == "let's ride into the sunset together")

print("\nlower() test.")
print(string.lower() == "let's ride into the sunset together")

number1 = 25
number2 = 25

print("\nNumber equality test.")
print(number1 == number2)

number2 = 33

print("\nNumber unequality test.")
print(number1 == number2)

print("\nNumber 'greater than' test.")
print(number1 > number2)

print("\nNumber 'less than' test.")
print(number1 < number2)

print("\nNumber 'greater than or equal to' test.")
print(number1 >= number2)

print("\nNumber 'less than or equal to' test.")
print(number1 <= number2)

print("\nThe 'and' word test.")
print(number1 == 25 and number2 == 33)

print("\nThe 'or' word test.")
print(number1 == 25 or number2 == 25)

numbers = list(value ** 2 for value in range(1,11))

print("\nWhether in the list test.")
print(number1 in numbers)

print("\nWhether not in the list test.")
print(number2 not in numbers)