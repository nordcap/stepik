"""
9-2. Три ресторана: начните с класса из упражнения 9-1. Создайте три разных экземпляра,
вызовите для каждого экземпляра метод describe_restaurant().
"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, end="-")
        print(self.cuisine_type)

    def open_restaurant(self):
        print("restaurant opened!")


restaurant_1 = Restaurant("7 sky", "new type")
restaurant_2 = Restaurant("tramp tower", "new type")
restaurant_3 = Restaurant("moskou city", "new type")
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
