"""
Вы решили написать преобразователь кода на Python в код на Java. Так как на Java принят стандарт
наименования CamelCase, то вы решили научиться преобразовывать имена из underscore в этот формат.
Для начала напишите программу, которая переводит имена переменных из стиля написания underscore
в стиль UpperCamelCase.
Стиль underscore характеризуется тем, что слова в имени пишутся маленькими буквами и разделяются
 между собой символом подчёркивания "_". Стиль UpperCamelCase означает, что каждое слово пишется
 с большой буквы и разделителей между словами нет.
Формат ввода:
Одна строка, содержащая имя, записанное в формате underscore.
Формат вывода:
Строка, содержащая пришедшее имя в формате UpperCamelCase.

Sample Input 1:
my_first_class
Sample Output 1:
MyFirstClass
Sample Input 2:
a
Sample Output 2:
A
"""

arr_s = input().split('_')
for i, v in enumerate(arr_s):
    arr_s[i] = v.capitalize()
print("".join(arr_s))
