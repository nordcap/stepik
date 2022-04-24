'''
Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.
'''

from decimal import *

s = input()
num = Decimal(s)
t = num.as_tuple().digits
if '0' in s:
    print(max(t))
else:
    print(min(t) + max(t))
