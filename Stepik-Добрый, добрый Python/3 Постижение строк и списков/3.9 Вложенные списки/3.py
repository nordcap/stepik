'''
Подвиг 3. Вводится  матрица чисел из трех строк. В каждой строке числа разделяются пробелом. Необходимо вывести на экран последний столбец этой матрицы в виде строки из трех чисел через пробел.
'''

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst3 = list(map(int, input().split()))

lst = []
lst.append(lst1[-1])
lst.append(lst2[-1])
lst.append(lst3[-1])

print(*lst)
