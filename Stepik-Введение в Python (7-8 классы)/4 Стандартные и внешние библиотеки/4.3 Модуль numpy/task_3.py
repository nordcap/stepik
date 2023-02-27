'''
Изменить форму
    На вход программе передается матрица размером N*M, а затем два числа – новая форма этой матрицы. Если преобразование формы возможно, выведите матрицу с новой формой, если нет – выведите строку "Невозможно".
'''
import numpy as np

a = [int(i) for i in input().split()]
N = a[0]
M = a[1]

matrix = []
for i in range(N):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

array = np.array(matrix)

new_a = [int(i) for i in input().split()]
new_N = new_a[0]
new_M = new_a[1]

# проверяем возможность преобразования
if N * M == new_N * new_M:
    res = array.reshape(new_N, new_M)
    print(res)
else:
    print("Невозможно")
