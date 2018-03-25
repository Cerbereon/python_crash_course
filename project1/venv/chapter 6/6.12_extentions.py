'''We’re now working with examples that are complex enough that they can be
extended in any number of ways. Use one of the example programs from this
chapter, and extend it by adding new keys and values, changing the context of
the program or improving the formatting of the output.'''

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print("\n" + name.title() + "'s favorite language is: ", end="")
    else:
        print("\n" + name.title() + "'s favorite languages are: ", end="")
    for language in languages:
        print(language.title(), end=" ")