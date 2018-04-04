prompt = "\nPlease enter a name of a city you have visited: "
prompt += "\n(Enter 'quit' to exit.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")