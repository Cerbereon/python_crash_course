'''Working with one of the programs from Exercises 3-4 through 3-7 (page 46),
use len() to print a message indicating the number of people you are inviting to
dinner.'''

names = ['Max', 'Andrew', 'Egor']

#1st name
print("Greetings " + names[0] + ". I'm inviting you to a dinner.")
#2nd
print("Greetings " + names[1] + ". I'm inviting you to a dinner.")
#3rd
print("Greetings " + names[2] + ". I'm inviting you to a dinner.\n")

print("Now I've invited " + str(len(names)) + " people")
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

print("Now I've invited " + str(len(names)) + " people")
print("Sorry, but now I can only invite two people.\n")

print("Sorry, " + names.pop() + " but I have no room for so much people. Next time I'll definetly invite you.")
print("Sorry, " + names.pop() + " but I have no room for so much people. Next time I'll definetly invite you.")
print("Sorry, " + names.pop() + " but I have no room for so much people. Next time I'll definetly invite you.")
print("Sorry, " + names.pop() + " but I have no room for so much people. Next time I'll definetly invite you.\n")

#1st name
print("Hello " + names[0] + ". I've decided to invite you this time.")
#2nd
print("Hello " + names[1] + ". I've decided to invite you this time.\n")

print("Now I've invited " + str(len(names)) + " people")

del names[1]
del names[0]

print(names)
print("Now I've invited " + str(len(names)) + " people")
