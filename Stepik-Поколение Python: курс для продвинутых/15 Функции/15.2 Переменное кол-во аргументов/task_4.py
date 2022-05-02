'''
Напишите функцию greet(), которая принимает произвольное количество аргументов строк имен (как минимум одно) и возвращает приветствие в соответствии с образцом.

Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.
'''


def greet(name, *args):
    if len(args) == 0:
        ends = name
    elif len(args) == 1:
        ends = name + " and " + args[0]
    else:
        ends = name + " and " + " and ".join(args)
    return "Hello, " + ends + "!"


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
