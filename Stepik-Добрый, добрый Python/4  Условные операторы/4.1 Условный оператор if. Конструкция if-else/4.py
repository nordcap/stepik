'''
Подвиг 4. Вводятся три целых положительных числа в одну строку через пробел. Убедиться, что первые два числа - это катеты прямоугольного треугольника, а третье - его гипотенуза. (Подсказка: проверка делается по теореме Пифагора ). Если проверка проходит (истинна), то вывести на экран ДА, иначе - НЕТ.
'''

a, b, c = map(int, input().split())
if a ** 2 + b ** 2 == c ** 2:
    print("ДА")
else:
    print("НЕТ")
