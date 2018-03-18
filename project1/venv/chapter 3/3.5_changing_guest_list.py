'''You just heard that one of your guests can’t make the dinner, so you need
to send out a new set of invitations. You’ll have to think of someone else to invite.
    • Start with your program from Exercise 3-4. Add a print statement at the end
    of your program stating the name of the guest who can’t make it.
    • Modify your list, replacing the name of the guest who can’t make it with the
    name of the new person you are inviting.
    • Print a second set of invitation messages, one for each person who is
     still in your list.'''

names = ['Max', 'Andrew', 'Egor']

#1st name
print("Greetings " + names[0] + ". I'm inviting you to a dinner.")
#2nd
print("Greetings " + names[1] + ". I'm inviting you to a dinner.")
#3rd
print("Greetings " + names[2] + ". I'm inviting you to a dinner.")

print(names[1] + " unfortunatly cannot come.")

names[1] = 'Vadim'

#1st name
print("Greetings " + names[0] + ". I'm inviting you to a dinner.")
#2nd
print("Greetings " + names[1] + ". I'm inviting you to a dinner.")
#3rd
print("Greetings " + names[2] + ". I'm inviting you to a dinner.")