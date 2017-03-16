"""
11-1. Город, страна: напишите функцию, которая получает два параметра: название
страны и  название города. Функция должна возвращать одну строку в  формате «Го-
род, Страна», например «Santiago, Chile». Сохраните функцию в модуле с именем city_
functions.py.
Создайте файл test_cities.py для тестирования только что написанной функции (не забудьте
импортировать unittest и  тестируемую функцию). Напишите метод test_city_country() для
проверки того, что вызов функции с такими значениями, как ‘santiago’ и ‘chile’, дает пра-
вильную строку. Запустите test_cities.py и убедитесь в том, что тест test_city_country() про-
ходит успешно.
"""
import unittest
from city_functions import city_country


class NamesTestCase(unittest.TestCase):
    """Тесты для city_functions.py"""

    def test_city_country(self):
        self.assertEqual(city_country("chile", "santiago"), "Santiago, Chile")


unittest.main()
