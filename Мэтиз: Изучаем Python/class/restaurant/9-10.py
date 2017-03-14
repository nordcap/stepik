"""
Импортирование класса Restaurant: возьмите последнюю версию класса Restaurant
и  сохраните ее в  модуле. Создайте отдельный файл, импортирующий класс Restaurant.
Создайте экземпляр Restaurant и вызовите один из методов Restaurant, чтобы показать, что
команда import работает правильно.
"""
import restaurant

restaurant = restaurant.Restaurant("7 sky", "new type")
restaurant.describe_restaurant()
restaurant.open_restaurant()
