'''
Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.
'''

from collections import OrderedDict

glossary = OrderedDict()

glossary['str'] = 'string'
glossary['lib'] = 'library'
glossary['int'] = 'integer'
glossary['del'] = 'delete'
glossary['app'] = 'application'
glossary['bool'] = 'boolean'
glossary['elif'] = 'else if'


for word, meaning in glossary.items():
    print("'" + word + "' means " + meaning)