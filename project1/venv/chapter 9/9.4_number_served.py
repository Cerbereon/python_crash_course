'''
Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business.
'''


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('"' + self.restaurant_name.title() + '" with ' +
              self.cuisine_type + ' cuisine.')

    def open_restaurant(self):
        print('"' + self.restaurant_name.title() + '" is now open.')

    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print('You cannot set less customers than it was.')

    def increment_number_served(self, customers):
        if customers >= 0:
            self.number_served += customers
        else:
            print('You cannot increase less than by 0 customers')


restaurant = Restaurant('MuMu', 'russian')
print(restaurant.number_served)
restaurant.number_served = 999
print(restaurant.number_served)

restaurant.set_number_served(1450)
print(restaurant.number_served)

restaurant.set_number_served(1414)
print(restaurant.number_served)

restaurant.increment_number_served(-2)
restaurant.increment_number_served(200)
print(restaurant.number_served)