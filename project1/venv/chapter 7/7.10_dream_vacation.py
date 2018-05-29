'''Write a program that polls users about their dream vacation. Write a prompt
similar to If you could visit one place in the world, where would you go?
Include a block of code that prints the results of the poll.'''

poll_results = {}

next_poll = True

while next_poll:
    name = input('What is your name?')
    answer = input('If you could visit one place in the world, where would you go?')
    poll_results[name] = answer

    next_poll_question = input('Would you plese give another person to answer?(yes/no)')
    if next_poll_question == 'no':
        next_poll = False

for name, answer in poll_results.items():
    print(name + ' would visit ' + answer + '.')