pizza = {
    'crust' : 'thick',
    'toppings' : ['extra cheese', 'mushrooms'],
}

print("You've ordered a " + pizza['crust'] + "-crust pizza "
        "with folowwing toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping)