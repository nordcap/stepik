import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Ivan', 'Ivanov', 10000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 15000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, 20000)


unittest.main()
