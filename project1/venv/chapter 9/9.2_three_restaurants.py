'''
Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
'''

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('"' + self.restaurant_name.title() + '" with ' +
              self.cuisine_type + ' cuisine.')

    def open_restaurant(self):
        print('"' + self.restaurant_name.title() + '" is now open.\n')


restaurant = Restaurant('MuMu', 'russian')
print("The restaurant's title is " + '"' + restaurant.restaurant_name +
      '"')
print('It has ' + restaurant.cuisine_type + ' cuisine.')
restaurant.describe_restaurant()
restaurant.open_restaurant()

second_restaurant = Restaurant('Teremok', 'russian')
second_restaurant.describe_restaurant()
second_restaurant.open_restaurant()

third_restaurant = Restaurant('SushiWok', 'japanese')
third_restaurant.describe_restaurant()
third_restaurant.open_restaurant()