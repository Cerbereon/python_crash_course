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


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def write_flavors(self):
        for flavor in self.flavors:
            print(flavor)