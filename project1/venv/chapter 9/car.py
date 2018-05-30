class Car():
    '''A simple attempt to represent a car.'''

    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted name.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''Print a statement showing the car's mileage.'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, miliage):
        '''Set the odometer reading to the given value.
        Reject if it attempts to roll back the odometer.'''
        if miliage >= self.odometer_reading:
            self.odometer_reading = miliage
        else:
            print('You cannot roll back the odometer.')

    def increment_odometer(self, miles):
        '''Add the given amount to the odometer reading.'''
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(22)
my_new_car.read_odometer()
my_new_car.update_odometer(20)

my_used_car = Car('subaru', 'outback', 2013)
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()