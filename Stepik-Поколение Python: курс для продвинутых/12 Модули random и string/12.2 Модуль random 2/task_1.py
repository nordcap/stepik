'''
IP адрес состоит из четырех чисел из диапазона от 00 до 255255 (включительно) разделенных точкой.

Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.
'''
import random


def generate_ip():
    arr = [i for i in range(255)]
    num1 = random.choice(arr)
    num2 = random.choice(arr)
    num3 = random.choice(arr)
    num4 = random.choice(arr)
    return f"{num1}.{num2}.{num3}.{num4}"


print(generate_ip())
