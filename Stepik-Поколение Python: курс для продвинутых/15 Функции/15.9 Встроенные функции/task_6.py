'''
Хороший пароль
Хороший пароль по условиям этой задачи состоит как минимум из 77 символов, содержит хотя бы одну цифру, заглавную и строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

Формат входных данных
На вход программе подаётся одна строка текста.

Формат выходных данных
Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.
'''
import string

password = input()

result = all([any(map(lambda x: x in string.digits, password)),
             any(map(lambda x: x in string.ascii_uppercase, password)),
             any(map(lambda x: x in string.ascii_lowercase, password)),
             len(password) >= 7])
if result:
    print('YES')
else:
    print('NO')
