'''
Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate
list. Call show_magicians() with each list to show that you have one list of
the original names and one list with the Great added to each magician’s name.
'''


def make_great(magicians):
    for i, magician in enumerate(magicians):
        magicians[i]= 'the Great ' + magician.title()
    return magicians


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ['mage1', 'mage2', 'mage3']
great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)