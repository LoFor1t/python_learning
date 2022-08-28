import unittest
from _11_2_population_function import get_formatted_city_country


class CitiesTestCase(unittest.TestCase):
    """Тесты для _11_1_city_functions.py"""

    def test_city_country(self):
        formatted_city = get_formatted_city_country('santiago', 'chicago')
        self.assertEqual(formatted_city, 'Santiago, Chicago')

    def test_city_country_population(self):
        formatted_city = get_formatted_city_country('santiago', 'chicago', 5_000_000)
        self.assertEqual(formatted_city, "Santiago, Chicago - population 5000000.")


if __name__ == '__main__':
    unittest.main()
