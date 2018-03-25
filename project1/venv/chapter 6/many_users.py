users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for user, user_info in users.items():
    print("\nUsername : " + user)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("Full name: " + full_name.title())
    print("Location: " + location.title())