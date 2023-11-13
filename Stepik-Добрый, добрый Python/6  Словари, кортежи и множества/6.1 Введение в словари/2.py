'''
Подвиг 4. На вход программы поступают данные в виде набора строк в формате:

ключ1=значение1
ключ2=значение2
...
ключN=значениеN

Ключами здесь выступают целые числа (см. пример ниже). Необходимо их преобразовать в словарь d (без использования функции dict()) и вывести его на экран командой:

print(*sorted(d.items()))

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
'''

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)


lst = [[a for a in elem.split('=')] for elem in lst_in]
d = dict(list(map(lambda x: [int(x[0]), x[1]], lst)))
print(*sorted(d.items()))
