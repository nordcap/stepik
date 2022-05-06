'''
Сумма чисел в строках
Вам доступен текстовый файл numbers.txt, каждая строка которого может содержать одно или несколько целых чисел, разделенных одним или несколькими пробелами.

Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит эту сумму на экран (для каждой строки выводится сумма чисел в этой строке).

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму чисел в каждой строке.
'''
from functools import reduce
import operator

with open('numbers.txt', encoding='utf-8') as file:
    for line in file:
        arr = [x.strip() for x in line.split(' ')]
        filter_result = list(filter(lambda x: x.isdigit(), arr))
        print(reduce(operator.add, [int(x) for x in filter_result], 0))
