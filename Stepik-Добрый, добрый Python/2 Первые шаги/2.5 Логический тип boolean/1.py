'''
Подвиг 5. Вводится вещественное число. Нужно определить, что его целая часть кратна 3. На экран вывести True, если кратно и False - в противном случае. Задача делается без использования условного оператора.
'''
import math
x = float(input())
print(math.floor(x) % 3 == 0)
