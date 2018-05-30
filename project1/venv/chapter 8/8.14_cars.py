'''
Write a function that stores information about a car in a diction-
ary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this
one: car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.
'''


def make_car(manufacturer, model_name, **characteristics):
    car = {}
    car['manufacturer'] = manufacturer
    car['model name'] = model_name
    for key, value in characteristics.items():
        car[key] = value
    return car


car = make_car('opel', 'astra',
               color='gray',
               tow_package=True,
               serial_number=123456)
print(car)