'''
Подвиг 9. (На использование цикла while). Вводятся названия книг (каждое с новой строки). Удалить из введенного списка все названия, состоящие из двух и более слов (слова в названиях разделяются пробелом). Результат вывести на экран в виде строки из оставшихся названий через пробел.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки
'''
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

while True:
    if len(lst_in) == 0:
        break
    elem = lst_in.pop(0)
    if len(elem.split()) < 2:
        print(elem, end=' ')
