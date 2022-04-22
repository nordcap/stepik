'''
Покупки в интернет-магазине 🌶️
Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем интернет-магазина.

Формат входных данных
На вход программе подается число nn — количество строк в базе данных о продажах интернет-магазина. Далее следует nn строк с записями вида покупатель товар количество, где покупатель — имя покупателя (строка без пробелов), товар — название товара (строка без пробелов), количество — количество приобретенных единиц товара (натуральное число).

Формат выходных данных
Программа должна вывести список всех покупателей в лексикографическом порядке, после имени каждого покупателя — двоеточие, затем список названий всех приобретенных им товаров в лексикографическом порядке, после названия каждого товара — количество единиц товара. Информация о каждом товаре выводится на отдельной строке.

Примечание. Обратите внимание на второй тест. Если позиции товаров повторяются, то в итоговый список попадает суммарное количество товара по данной позиции.
'''

n = int(input())
dictionary = {}

for _ in range(n):
    arr = input().split()  # покупатель товар количество
    name = arr[0]
    tovar = arr[1]
    count = int(arr[2])
    if name not in dictionary:
        dictionary[name] = {tovar: count}
    else:
        if tovar not in dictionary[name]:
            dictionary[name][tovar] = count
        else:
            dictionary[name][tovar] = dictionary[name].get(tovar) + count

for dict_name, dict_sales in sorted(dictionary.items()):
    print(f"{dict_name}:")
    for k, v in sorted(dict_sales.items()):
        print(k, v)
