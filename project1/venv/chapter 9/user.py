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