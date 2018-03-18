'''Think of something you could store in a list. For example, you could make a
list of mountains, rivers, countries, cities, languages, or anything else you’d like.
Write a program that creates a list containing these items and then uses each
function introduced in this chapter at least once.'''

languages = ['Russian', 'English', 'German', 'Dutch', 'French']

#Reverse temporarly
print(sorted(languages, reverse = True))
print(languages)

#Reverse permanently
languages.reverse()
print(languages)

#Sort temporarly
print(sorted(languages))
print(languages)

#Sort permanently
languages.sort()
print(languages)

#Permanently sorted in reversed order
languages.sort(reverse = True)
print(languages)

#Length
print(len(languages))

#Append
languages.append('Spanish')
print(languages)

#insert
languages.insert(3, 'Chineese')
print(languages)

#Remove
languages.remove('French')
print(languages)

#Pop
languages.pop()
print(languages)

#Del
del languages[2]
print(languages)