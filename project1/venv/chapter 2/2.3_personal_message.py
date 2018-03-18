'''Store a person’s name in a variable, and print a message to that person.
 Your message should be simple, such as,
 “Hello Eric, would you like to learn some Python today?”'''

name = input()
name = name.strip()
message = "Hello " + name.title() + ", would you like to learn some Python today?"
print(message)