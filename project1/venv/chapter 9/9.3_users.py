'''
Make a class called User . Create two attributes called first_name
and last_name , and then create several other attributes that are typically
stored in a user profile. Make a method called describe_user() that prints a
summary of the user’s information. Make another method called greet_user()
that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
'''


class User():

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print('First name: ' + self.first_name.title() +
              '; Last name: ' + self.last_name.title() +
              '; Age: ' + str(self.age) +
              '; Location: ' + self.location.title())

    def greet_user(self):
        print('Greetings, ' + self.first_name.title() + ' ' +
              self.last_name.title() + '.\n')


user1 = User('willie', 'wonka', 40, 'somewhere')
user1.describe_user()
user1.greet_user()

user2 = User('max', 'korenev', 19, 'moscow')
user2.describe_user()
user2.greet_user()

user3 = User('mde', 'meh', 30, 'mmm')
user3.describe_user()
user3.greet_user()