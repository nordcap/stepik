'''
Змеиный регистр
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно тут.
'''


# объявление функции
def convert_to_python_case(text):
    arr = []
    for i in range(len(text)):
        if text[i].isupper():
            arr.extend(['_', text[i].lower()])
        else:
            arr.append(text[i])
    if arr[0] == '_':
        del arr[0]
    return ''.join(arr)


print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))
