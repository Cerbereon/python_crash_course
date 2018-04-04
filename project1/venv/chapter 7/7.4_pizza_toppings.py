'''Write a loop that prompts the user to enter a series of pizza toppings until
they enter a 'quit' value. As they enter each topping, print a message saying
you’ll add that topping to their pizza.'''

promt = "\nWrite a topping to add to your pizza."
promt += "\n(Write 'quit' to exit)"

pizza_toppings = {'extra cheese', 'mushrooms', 'green pepper'}

topping = ""
while topping != 'quit':
    topping = input(promt).lower().strip()

    if topping != 'quit':
        if topping in pizza_toppings:
            print("Adding " + topping + " to your pizza.")
        else:
            print("Sorry, we don't have " + topping + ".")
