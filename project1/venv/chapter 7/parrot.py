prompt = "\nTell me somthing and I will repeat it back to you: "
prompt += "\nEnter 'quit' to exit. "

active = True
message = ""
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)