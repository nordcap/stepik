"""
Ресторан: создайте класс с именем Restaurant. Метод __init__() класса Restaurant дол-
жен содержать два атрибута: restaurant_name и  cuisine_type. Создайте метод describe_
restaurant(), который выводит два атрибута, и  метод open_restaurant(), который выводит
сообщение о том, что ресторан открыт.
Создайте на основе своего класса экземпляр с именем restaurant. Выведите два атрибута по
отдельности, затем вызовите оба метода.
"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("restaurant opened!")


restaurant = Restaurant("7 sky", "new type")
print("\nget attribute")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print("\ncall methods")
restaurant.describe_restaurant()
restaurant.open_restaurant()
