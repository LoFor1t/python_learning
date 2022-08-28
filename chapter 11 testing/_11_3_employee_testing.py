import unittest
from _11_3_employee_function import Employee


class TestEmployee(unittest.TestCase):
    """Проводит тестирование для класса Employee."""

    def setUp(self):
        """Создаём нового сотрудника."""
        self.my_employee = Employee('Vlad', 'Belenkov', 15000)

    def test_give_default_raise(self):
        """Тест со стандартным повышением."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 20_000)

    def test_give_custom_raise(self):
        """Тест с кастомным повышением."""
        self.my_employee.give_raise(10_000)
        self.assertEqual(self.my_employee.salary, 25_000)


if __name__ == '__main__':
    unittest.main()
