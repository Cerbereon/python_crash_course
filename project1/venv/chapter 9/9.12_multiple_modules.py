'''
Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
'''


from user import User
from admin_privileges import Admin

admin1 = Admin('max', 'korenev', 19, 'moscow')
admin1.privileges.show_privileges()