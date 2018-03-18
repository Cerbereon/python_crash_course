# Let's take task 2.3 and comment it

# Here we ask user to input his name
name = input()
#In case user wrote extra spaces, we get rid of them
name = name.strip()
#Then we store message, which we'll print later in variable. Alse, on this step
#we make name look properly, with a capital first letter
message = "Hello " + name.title() + ", would you like to learn some Python today?"

print(message)