'''
Start with your work from Exercise 9-8 (page 178).
Store the classes User , Privileges , and Admin in one module. Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
'''

from user_admin_privileges import Admin

admin1 = Admin('max', 'korenev', 19, 'moscow')
admin1.privileges.show_privileges()