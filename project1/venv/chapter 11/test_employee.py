import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Max', 'Korenev', 29000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 34000)

    def test_give_custom_raise(self):
        self.employee.give_raise(1000)
        self.assertEqual(self.employee.salary, 30000)


unittest.main()