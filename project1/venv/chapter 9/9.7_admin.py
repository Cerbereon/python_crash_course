'''
An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges , that stores a list
of strings like "can add post" , "can delete post" , "can ban user" , and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin , and call your method.
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


class Admin(User):

    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


admin1 = Admin('max', 'korenev', 19, 'moscow')
admin1.show_privileges()
