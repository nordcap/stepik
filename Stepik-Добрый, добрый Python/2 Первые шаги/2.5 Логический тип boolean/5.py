'''
Подвиг 11. Вводится вещественное число. Нужно проверить, что оно попадает или в диапазон [0; 2] или в диапазон [10; 20] (включительно). На экран вывести True, если попадает и False - в противном случае. Задача делается без использования условного оператора.
'''

x = float(input())

print((x >= 0 and x <= 2) or (x >= 10 and x <= 20))
