'''
Фонарные столбы
    Правительство выделило определенный бюджет M на постройку фонарных столбов вдоль дороги длиной N. Подсчитано, что один фонарный столб стоит K. Строителям нужно поставить как можно больше столбов на равном расстоянии друг от друга. Выведите координаты каждого столба, принимая, что ось Х идет вдоль дороги и координата первого столба – 0.

    Формат ввода: целые числа N, M, K через пробел.

    Формат вывода: numpy-массив координат.

    Подсказка: для решения используйте функцию, которая разбивает промежуток [from, to).
'''
import numpy as np

array = [int(i) for i in input().split()]
N, M, K = array[0], array[1], array[2]

count = M // K  # количество столбов
diff = N / count  # расстояние между столбами
arr_column = np.arange(start=0, stop=N, step=diff).astype(int)
print(arr_column)
