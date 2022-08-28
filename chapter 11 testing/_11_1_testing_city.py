import unittest
from _11_1_city_functions import get_formatted_city_country


class CitiesTestCase(unittest.TestCase):
    """Тесты для _11_1_city_functions.py"""

    def test_city_country(self):
        formatted_city = get_formatted_city_country('santiago', 'chicago')
        self.assertEqual(formatted_city, 'Santiago, Chicago')


if __name__ == '__main__':
    unittest.main()
