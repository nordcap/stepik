"""
9-4. Посетители: начните с  программы из упражнения 9-1 (с.  165). Добавьте атрибут
number_served со значением по умолчанию 0; он представляет количество обслуженных
посетителей. Создайте экземпляр с именем restaurant. Выведите значение number_served,
потом измените и выведите снова.
Добавьте метод с именем set_number_served(), позволяющий задать количество обслужен-
ных посетителей. Вызовите метод с новым числом, снова выведите значение.
Добавьте метод с  именем increment_number_served(), который увеличивает количество
обслуженных посетителей на заданную величину. Вызовите этот метод с любым числом,
которое могло бы представлять количество обслуженных клиентов — скажем, за один день
"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("restaurant opened!")

    def set_number_served(self, cnt):
        self.number_served = cnt

    def increment_number_served(self, cnt):
        self.number_served += cnt


restaurant = Restaurant("7 sky", "new type")
print(restaurant.number_served)
restaurant.number_served = 90
print(restaurant.number_served)
restaurant.set_number_served(600)
print(restaurant.number_served)
restaurant.increment_number_served(400)
print(restaurant.number_served)
