'''
Подвиг 2. Вводится список городов в одну строчку через пробел. Необходимо создать итератор для этого списка и с помощью итератора вывести на экран в столбик первые два значения (названия городов).
'''

array = input().split()
city = iter(array)
print(next(city))
print(next(city))