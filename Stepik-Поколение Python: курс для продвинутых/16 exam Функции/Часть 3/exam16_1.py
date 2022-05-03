'''
Напишите функцию concat(), принимающую переменное количество аргументов и объединяющую их в одну строку через разделитель (sep). Если разделитель не задан, им служит пробел.

Примечание 1. Обратите внимание, что функция concat() должна принимать не список, а именно переменное количество аргументов.
'''
from functools import reduce


def concat(*args, sep=' '):
    result = str(args[0])
    for k, v in enumerate(args):
        if k == 0:
            continue
        result += sep + str(v)
    return result

    # if len(args) == 1:
    #     return args[0]
    # else:
    #     return reduce(lambda x, y: str(x) + sep + str(y), args, '')


print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))
