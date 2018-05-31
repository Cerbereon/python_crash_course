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


class Battery():
    '''A simple attemot to model a battery for an electic car.'''

    def __init__(self, battery_size=70):
        '''Initialize the battery's attributes'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print('This car has a ' +  str(self.battery_size) + '-kwh battery.')

    def get_range(self):
        '''Print a statement about the range this battery provides.'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    '''Represent aspects of a car, specific to electic vehicles'''

    def __init__(self, make, model, year):
        '''Initialize attributes of the parent class.'''
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()