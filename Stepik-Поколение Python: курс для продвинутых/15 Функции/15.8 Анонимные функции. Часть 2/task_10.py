'''
Список mixed_list содержит целочисленные и строковые значения. Напишите программу его сортировки по неубыванию значений элементов, при этом числа должны следовать до строк.  Элементы отсортированного списка выведите на одной строке, разделив символом пробела.

Примечание 1. Для решения задачи используйте анонимную функцию и необязательный аргумент key  функции sorted().
'''

mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76,
              70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort',
              13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80,
              'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon',
              'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt',
              'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]

sorted_list_1 = sorted(mixed_list, key=lambda x: x if type(x) == int else 0)
sorted_list_2 = sorted(sorted_list_1, key=lambda x: x if type(x) == str else '')
print(*sorted_list_2)
