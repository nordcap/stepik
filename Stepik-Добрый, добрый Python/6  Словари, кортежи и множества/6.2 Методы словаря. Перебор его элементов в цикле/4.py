'''
Подвиг 6. Вводятся данные в формате:

<день рождения 1> имя_1
<день рождения 2> имя_2
...
<день рождения N> имя_N

Дни рождений и имена могут повторяться. На их основе сформировать словарь и вывести его в формате (см. пример ниже):

день рождения 1: имя1, ..., имяN1
день рождения 2: имя1, ..., имяN2
...
день рождения M: имя1, ..., имяNM

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
'''

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
# lst_keys = [elem[0] for elem in lst_in]

# dict_result = dict.fromkeys(lst_keys, [])
dict_result = dict()
for elem in lst_in:
    x = elem.split()
    # dict_result[x[0]].append(x[1])
    dict_result.setdefault(x[0], []).append(x[1])

for key, value in dict_result.items():
    print(f"{key}: {', '.join(value)}")
