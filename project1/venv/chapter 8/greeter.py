def greet_user():
    print('Hello!')


greet_user()


def greet_user(username):
    print('Hello, ' + username.title() + '!')


name = input('Write you username')
greet_user(name)