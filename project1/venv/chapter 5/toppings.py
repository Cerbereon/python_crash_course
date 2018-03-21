requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!\n")


requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!\n")


if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!\n")


requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")


for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers rigth now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!\n")


requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!\n")
else:
    print("Are you sure, you want a plain pizza?\n")


available_toppings = ['extra cheese', 'green peppers', 'pepperoni',
                      'mushrooms', 'olives', 'pineapple']
requested_toppings = ['pepperoni', 'olives', 'chicken']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!\n")