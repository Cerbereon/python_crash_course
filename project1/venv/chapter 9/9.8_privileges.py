'''
Write a separate Privileges class. The class should have one
attribute, privileges , that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
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


class Privileges():

    def __init__(self):
        self.privileges = ['Can add post', 'Can delete post', 'Can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):

    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()


admin1 = Admin('max', 'korenev', 19, 'moscow')
admin1.privileges.show_privileges()
