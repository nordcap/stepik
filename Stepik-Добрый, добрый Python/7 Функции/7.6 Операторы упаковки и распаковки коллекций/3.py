'''
Подвиг 4. Вводятся два целых значения a и b (a < b) в одну строчку через пробел. Необходимо сформировать список из целых чисел от a до b (включительно) с шагом изменения 1, используя функцию range, оператор [] и оператор распаковки *. Вывести полученный список на экран командой:
print(*lst)
'''

arr = list(map(int, input().split()))
arr[-1] = arr[-1] + 1
lst = range(*arr)
print(*lst)
