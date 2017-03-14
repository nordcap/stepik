"""
Города: напишите функцию describe_city(), которая получает названия города и стра-
ны. Функция должна выводить простое сообщение (например, «Reykjavik is in Iceland»). За-
дайте параметру страны значение по умолчанию. Вызовите свою функцию для трех разных
городов, по крайней мере один из которых не находится в стране по умолчанию.
"""


def describe_city(city, country="Russia"):
    print(city, "is in", country)


describe_city("Kemerovo")
describe_city("Berlin", "Germany")
describe_city("Paris", "France")
