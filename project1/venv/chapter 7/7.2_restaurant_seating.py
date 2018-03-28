'''Write a program that asks the user how many people are in their dinner
group. If the answer is more than eight, print a message saying they’ll have
to wait for a table. Otherwise, report that their table is ready.'''

number_of_people = input("How many people in their dinner group now? ")
number_of_people = int(number_of_people)

if number_of_people > 8:
    print("\nSorry, you need to wait for the table.")
else:
    print("\nOK. Your table is ready.")