'''
Put the functions for the example print_models.py in a
separate file called printing_functions.py. Write an import statement at the
top of print_models.py, and modify the file to use the imported functions.
'''

def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_design = unprinted_models.pop()
        print("Printing model: " + current_design +  ".")
        completed_models.append(current_design)


def show_completed(completed_models):
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)