'''Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: key и value

Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2⋅key. Если и ключа 2⋅key нет, то нужно
добавить ключ 2⋅key в словарь и сопоставить ему список из переданного элемента [value].

Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.
Пример работы функции:

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
'''


def update_dictionary(d, key, value):
    global dict
    if key in d:
        d.get(key).append(value)
    else:
        if 2 * key in d:
            d.get(2 * key).append(value)
        else:
            d[2 * key] = [value]

    dict = d

    return


dict = {}
print(update_dictionary(dict, 1, -1))  # None
print(dict)  # {2: [-1]}
update_dictionary(dict, 2, -2)
print(dict)  # {2: [-1, -2]}
update_dictionary(dict, 1, -3)
print(dict)  # {2: [-1, -2, -3]}
