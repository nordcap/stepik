'''
Обработка списка
﻿  В первой строке вводится натуральное число n, затем n чисел по одному в строке, числа не превышают 10^4. Для переданного набора чисел вычислите контрольное значение M – сумму минимального нечетного и минимального четного элементов. Затем увеличьте все элементы набора, меньшие M, на M. Если отсутствуют четные или нечетные числа, считайте соответствующий минимум равным нулю. Выведите элементы обработанного набора чисел через пробел.
'''

n = int(input())
min_even = 999999999999  # четный
min_odd = 9999999999999  # нечетный
arr = []
count_even = 0
count_odd = 0
for _ in range(n):
    elem = int(input())
    if elem % 2 == 0:
        count_even += 1
        if elem < min_even:
            min_even = elem
    else:
        count_odd += 1
        if elem < min_odd:
            min_odd = elem

    arr.append(elem)

if count_even == 0 or count_odd == 0:
    M = 0
else:
    M = min_odd + min_even
res = list(map(lambda x: x + M if x < M else x, arr))
print(*res)
