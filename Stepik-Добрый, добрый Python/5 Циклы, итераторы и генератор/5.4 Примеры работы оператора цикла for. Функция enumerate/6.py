'''
Подвиг 6. Вводится список в виде вещественных чисел в одну строку через пробел. С помощью цикла for необходимо найти наименьшее значение в этом списке. Полученный результат вывести на экран.  Реализовать программу без использования функции min, max и сортировки.
'''

array = list(map(float, input().split()))
minimum = array[0]
for i, d in enumerate(array):
    if d < minimum:
        minimum = d
print(minimum)
