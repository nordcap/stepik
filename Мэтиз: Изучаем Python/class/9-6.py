"""
Киоск с мороженым: киоск с мороженым — особая разновидность ресторана. Напишите
класс IceCreamStand, наследующий от класса Restaurant из упражнения 9-1  (с.  165) или
упражнения 9-4 (с. 169). Подойдет любая версия класса; просто выберите ту, которая вам
больше нравится. Добавьте атрибут с именем flavors для хранения списка сортов мороже-
ного. Напишите метод, который выводит этот список. Создайте экземпляр IceCreamStand
и вызовите этот метод.
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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def get_flavors(self):
        for i, v in enumerate(self.flavors):
            print(i+1,"-", v)


kiosk = IceCreamStand("Num1", "icecream", ['flavor_1', 'flavor_2', 'flavor_3'])
kiosk.get_flavors()
