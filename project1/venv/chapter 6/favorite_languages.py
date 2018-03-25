favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

print("Edward's favorite language is " +
      favorite_languages['edward'].title() +
      ".\n")


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print()


for name in favorite_languages.keys():
    print(name.title())

print()


friends = ['sarah', 'phil']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print("Oh, hey " + name.title() + ", I see your favorite language is "
                + favorite_languages[name].title() + "!")


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print()


for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thanks for taking the poll.")


print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(name.title() + "'s favorite language is: ")
    else:
        print(name.title() + "'s favorite languages are: ")
    for language in languages:
        print("\t" + language.title())