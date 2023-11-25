'''
Большой подвиг 6. (Для закрепления предыдущего материала). Вводится таблица целых чисел (см. пример ниже) размером N x N элементов (N определяется по входным данным). Эта таблица содержит нули, но кое-где - единицы. С помощью функции с именем verify, на вход которой передается двумерный список чисел, необходимо проверить, являются ли единицы изолированными друг от друга, то есть, вокруг каждой единицы должны быть нули.

Рекомендуется следующий алгоритм. В функции verify производить перебор двумерного списка. Для каждого элемента (списка) со значением 1 вызывать еще одну вспомогательную функцию is_isolate для проверки изолированности единицы. То есть, функция is_isolate должна возвращать True, если единица изолирована и False - в противном случае.

Как только встречается не изолированная единица, функция verify должна возвращать False. Если успешно доходим (по элементам списка) до конца, то возвращается значение True.

Функцию выполнять не нужно, только определить.
'''

import sys


def is_isolate(i, j, N, lst_in):
    if i < N - 1 and j < N - 1:
        if 1 + lst_in[i + 1][j] + lst_in[i + 1][j + 1] + lst_in[i][j + 1] > 1:
            return False
    return True


def verify(lst):
    N = len(lst)
    for i, row in enumerate(lst):
        for j, elem in enumerate(row):
            if elem == 1 and not is_isolate(i, j, N, lst):
                return False
    return True


# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

print(verify(lst_in))
