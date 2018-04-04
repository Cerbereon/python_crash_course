'''Write different versions of either Exercise 7-4 or Exercise 7-5 that do each
of the following at least once:
    • Use a conditional test in the while statement to stop the loop.
    • Use an active variable to control how long the loop runs.
    • Use a break statement to exit the loop when the user enters a 'quit' value.
    '''

promt = "\nWrite a topping to add to your pizza."
promt += "\n(Write 'quit' to exit)"

pizza_toppings = {'extra cheese', 'mushrooms', 'green pepper'}

#Using conditional test here in order to exit

topping = ""
while topping != 'quit':
    topping = input(promt).lower().strip()

    if topping != 'quit':
        if topping in pizza_toppings:
            print("Adding " + topping + " to your pizza.")
        else:
            print("Sorry, we don't have " + topping + ".")

#Using active value in order to exit
active = True
while active:
    topping = input(promt).lower().strip()

    if topping != 'quit':
        if topping in pizza_toppings:
            print("Adding " + topping + " to your pizza.")
        else:
            print("Sorry, we don't have " + topping + ".")
    else:
        active = False

#Using break statement in order to exit
while True:
    topping = input(promt).lower().strip()

    if topping != 'quit':
        if topping in pizza_toppings:
            print("Adding " + topping + " to your pizza.")
        else:
            print("Sorry, we don't have " + topping + ".")
    else:
        break