'''
Подвиг 6. Вводятся названия городов в одну строчку через пробел. Необходимо преобразовать входные данные в список. Затем, перебрать его циклом for и заменить значения элементов на длину названия соответствующего города. Результат вывести на экран в виде последовательности чисел через пробел в одну строчку.
'''

array = input().split()
for i in range(len(array)):
    array[i] = len(array[i])

print(*array)
