'''Modify your program from Exercise 6-2 (page 102) so each person can have
more than one favorite number. Then print each person’s name along with their
favorite numbers.'''

favorite_numbers = {
    'jane' : [11, 100],
    'simon' : [6, 228],
    'dan' : [13, 4, 1101],
    'max' : [37],
    'alice' : [89, 1111]
}

for name, numbers in favorite_numbers.items():
    if len(numbers) < 2:
        print("\n" + name.title() + "'s favorite number is ")
    else:
        print("\n" + name.title() + "'s favorite numbers are ")
    for number in numbers:
        print(number)