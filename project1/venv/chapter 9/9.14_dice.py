'''
The module random contains functions that generate random num-
bers in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
from random import randint
x = randint(1, 6)
Make a class Die with one attribute called sides , which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
'''

from random import randint


class Die():

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        print(str(randint(1, self.sides)))


class TenSidedDie(Die):
    def __init__(self):
        self.sides = 10


class TwentySidedDie(Die):
    def __init__(self):
        self.sides = 20


six_die = Die()
print('Rolling 6-sided die:')
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()

ten_die = TenSidedDie()
print('\nRolling 10-sided die:')
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()

twenty_die = TwentySidedDie()
print('\nRolling 20-sided die:')
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()