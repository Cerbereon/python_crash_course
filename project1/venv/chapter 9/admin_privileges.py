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
