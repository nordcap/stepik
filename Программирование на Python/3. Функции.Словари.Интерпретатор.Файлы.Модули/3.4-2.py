'''Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
 слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически
  первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.
Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3
'''
with open('sample_input2.txt', 'r') as file:
    str = file.read()
    lst = str.lower().split()  # перевели строки в список
    lst_one = list(set(lst))

    d = {}  # формируем словарь в котором будут храниться кол-во повторяющихся строк  'abc':12

    for i in lst_one:
        count = lst.count(i)
        d[i] = count

    list_val = list(d.values())  # получаем список значений словаря
    max_val = max(list_val)  # получаем максимальное значение повторений

    output_list = []  # формируем список из элементов словаря с максимальным значением value
    for key in d:
        if d[key] == max_val:
            output_list.append(key)

    output_list.sort()  # сортируем лексикографически

    print(output_list[0], max_val)
