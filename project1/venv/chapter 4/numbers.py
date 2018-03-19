for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    #square = value ** 2
    #squares.append(square)
    squares.append(value ** 2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))

cubes = [value ** 3 for value in range(1,11)]
print(cubes)