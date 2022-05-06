'''
Random name and surname
Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

Напишите программу, которая c помощью модуля random создает 33 случайные пары имя + фамилия, а затем выводит их, каждую на отдельной строке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести текст в формате, приведенном в примере.
'''
import random

with open('first_names.txt', encoding='utf-8') as file_f, open('last_names.txt', encoding='utf-8') as file_l:
    first = file_f.readlines()
    last = file_l.readlines()
    arr_first = [x.strip() for x in first]
    arr_last = [x.strip() for x in last]

    for _ in range(3):
        print(random.choice(arr_first), random.choice(arr_last))
