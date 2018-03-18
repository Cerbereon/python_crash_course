'''You just found a bigger dinner table, so now more space is available.
Think of three more guests to invite to dinner.
    • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
    statement to the end of your program informing people that you found a bigger
    dinner table.
    • Use insert() to add one new guest to the beginning of your list.
    • Use insert() to add one new guest to the middle of your list.
    • Use append() to add one new guest to the end of your list.
    • Print a new set of invitation messages, one for each person in your list.'''

names = ['Max', 'Andrew', 'Egor']

#1st name
print("Greetings " + names[0] + ". I'm inviting you to a dinner.")
#2nd
print("Greetings " + names[1] + ". I'm inviting you to a dinner.")
#3rd
print("Greetings " + names[2] + ". I'm inviting you to a dinner.\n")

print(names[1] + " unfortunatly cannot come.\n")

names[1] = 'Vadim'

#1st name
print("Greetings " + names[0] + ". I'm inviting you to a dinner.")
#2nd
print("Greetings " + names[1] + ". I'm inviting you to a dinner.")
#3rd
print("Greetings " + names[2] + ". I'm inviting you to a dinner.\n")

print("I've found a bigger dinner table, so now I can invite more people.\n")

names.insert(0, 'Maria')
names.insert(2, 'Kathrine')
names.append('Anna')

#1st name
print("Greetings " + names[0] + ". I'm inviting you to a dinner.")
#2nd
print("Greetings " + names[1] + ". I'm inviting you to a dinner.")
#3rd
print("Greetings " + names[2] + ". I'm inviting you to a dinner.")
#4th
print("Greetings " + names[3] + ". I'm inviting you to a dinner.")
#5th
print("Greetings " + names[4] + ". I'm inviting you to a dinner.")
#6th
print("Greetings " + names[5] + ". I'm inviting you to a dinner.")

