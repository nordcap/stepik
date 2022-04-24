'''
Математическое выражение
'''
from decimal import *

d = Decimal(input())

solve = d.exp() + d.ln() + d.log10() + d.sqrt()
print(solve)
