"""
9-14. Кубики: модуль random содержит функции для генерирования случайных чисел раз-
ными способами. Функция randint() возвращает целое число в заданном диапазоне. Следу-
ющий код возвращает число от 1 до 6:
from random import randint
x = randint(1, 6)
Создайте класс Die с одним атрибутом с именем sides, который содержит значение по умол-
чанию 6. Напишите метод roll_die() для вывода случайного числа от 1 до количества сторон
кубика. Создайте экземпляр, моделирующий 6-гранный кубик, и  имитируйте 10 бросков.
Создайте модели 10- и 20-гранного кубика. Имитируйте 10 бросков каждого кубика.
"""
from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)

print("6 гранный кубик")
kubik_6 = Die()
for i in range(10):
    kubik_6.roll_die()
print("10 гранный кубик")
kubik_10 = Die(10)
for i in range(10):
    kubik_10.roll_die()
print("20 гранный кубик")
kubik_20 = Die(20)
for i in range(10):
    kubik_20.roll_die()