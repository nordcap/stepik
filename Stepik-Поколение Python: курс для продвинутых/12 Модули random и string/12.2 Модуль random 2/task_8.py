'''
Генератор паролей 1
Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
Формат входных данных
На вход программе подаются два числа nn и mm, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести nn паролей длиной mm символов в соответствии с условием задачи, каждый на отдельной строке.

Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые пароли сгенерировать возможно.

Примечание 2. В каждом пароле необязательно должна присутствовать хотя бы одна цифра и буква в верхнем и нижнем регистре.

Примечание 3. Решение задачи удобно оформить в виде двух вспомогательных функций:

функция generate_password(length) – возвращает случайный пароль длиной length символов;
функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.
'''

import string
import random

list_symbols_all = string.ascii_letters+string.digits
list_symbols= list_symbols_all.replace('l','').replace('I','').replace('1','').replace('o','').replace('O','').replace('0','')

n, m = int(input()), int(input())

def generate_password(length):
    for _ in range(length):
        sym = random.choice(list_symbols)
        print(sym, end='')

def generate_passwords(count, length):
    for _ in range(count):
        generate_password(length)
        print()

generate_passwords(n, m)

