'''
Run-length encoding
    Реализуйте кодирование длин серий (Run-length encoding) – алгоритм сжатия данных. Он заменяет серию повторяющихся символов одним символом и числом его повторений.

    Формат ввода: строка, содержащая целые числа через пробел.

    Формат вывода: два numpy-массива одинаковой длины: первый содержит элементы, второй – количество повторений соответствующего элемента.
'''

import numpy as np

a = np.array([int(i) for i in input().split()])
arr_elements = []
arr_counts = []
cn = 1  # счетчик совпадений
for key, value in np.ndenumerate(a):
    if key[0] == a.size - 1:  ##если последний элемент списка, то выход
        arr_elements.append(value)
        arr_counts.append(cn)
        break
    if value == a[key[0] + 1]:  # значение совпадает с последующим
        cn += 1
    else:
        arr_elements.append(value)
        arr_counts.append(cn)
        cn = 1

print(*np.array(arr_elements))
print(*np.array(arr_counts))
