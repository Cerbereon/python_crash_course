motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(2, 'harley davidson')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print(motorcycles)
last_owned = motorcycles.pop()
print("The last motorcycle I owned was '" + last_owned + "'.")

print(motorcycles)
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was '" + first_owned + "'.")


motorcycles = ['ducati', 'yamaha', 'harley davidson', 'suzuki', 'honda']

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA '" + too_expensive.title() + "' is too expensive for me.")