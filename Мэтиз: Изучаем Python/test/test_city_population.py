"""
11-2. Население: измените свою функцию так, чтобы у  нее был третий обязательный
параметр  — население. В  новой версии функция должна возвращать одну строку вида
«Santiago, Chile — population 5000000.» Снова запустите программу test_cities.py. Убедитесь
в том, что тест test_city_country() на этот раз не проходит.
Измените функцию так, чтобы параметр населения стал необязательным. Снова запустите
test_cities.py и убедитесь в том, что тест test_city_country() проходит успешно.
Напишите второй тест test_city_country_population(), который проверяет вызов функции
со значениями ‘santiago’, ‘chile’ и ‘population=5000000’. Снова запустите test_cities.py и убе-
дитесь в том, что новый тест проходит успешно.
"""
import unittest
from city_functions import city_country_population

class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country_population("chile", "santiago"), "Santiago, Chile")

    def test_city_country_population(self):
        self.assertEqual(city_country_population("chile", "santiago","population=5000000"), "Santiago, Chile, population=5000000")

unittest.main()
