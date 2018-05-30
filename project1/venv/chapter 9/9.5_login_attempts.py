'''
Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of
login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was
incremented properly, and then call reset_login_attempts() . Print
login_attempts again to make sure it was reset to 0.
'''


class User():

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print('First name: ' + self.first_name.title() +
              '; Last name: ' + self.last_name.title() +
              '; Age: ' + str(self.age) +
              '; Location: ' + self.location.title())

    def greet_user(self):
        print('Greetings, ' + self.first_name.title() + ' ' +
              self.last_name.title() + '.\n')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user2 = User('max', 'korenev', 19, 'moscow')
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
print(user2.login_attempts)
user2.reset_login_attempts()
print(user2.login_attempts)