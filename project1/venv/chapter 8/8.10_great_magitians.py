'''
Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by add-
ing the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
'''


def make_great(magicians):
    for i, magician in enumerate(magicians):
        magicians[i]= 'the Great ' + magician.title()


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ['mage1', 'mage2', 'mage3']
make_great(magicians)
show_magicians(magicians)