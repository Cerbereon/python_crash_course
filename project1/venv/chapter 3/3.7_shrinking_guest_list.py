'''You just found out that your new dinner table won’t arrive in time for the
dinner, and you have space for only two guests.
    • Start with your program from Exercise 3-6. Add a new line that prints
    a message saying that you can invite only two people for dinner.
    • Use pop() to remove guests from your list one at a time until only two
    names remain in your list. Each time you pop a name from your list, print
    a message to that person letting them know you’re sorry you can’t invite
    them to dinner.
    • Print a message to each of the two people still on your list,
    letting them know they’re still invited.
    • Use del to remove the last two names from your list, so you have an empty list.
    Print your list to make sure you actually have an empty list at the end of your
    program.'''

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
print("Greetings " + names[5] + ". I'm inviting you to a dinner.\n")

print("Sorry, but now I can only invite two people.\n")

print("Sorry, " + names.pop() + " but I have no room for so much people. Next time I'll definetly invite you.")
print("Sorry, " + names.pop() + " but I have no room for so much people. Next time I'll definetly invite you.")
print("Sorry, " + names.pop() + " but I have no room for so much people. Next time I'll definetly invite you.")
print("Sorry, " + names.pop() + " but I have no room for so much people. Next time I'll definetly invite you.\n")

#1st name
print("Hello " + names[0] + ". I've decided to invite you this time.")
#2nd
print("Hello " + names[1] + ". I've decided to invite you this time.\n")

del names[1]
del names[0]

print(names)
