"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
Sample Input:
attraction
buzzzz
Sample Output:
atraction
buz
"""

import re, sys


def rep1(m):
    s1 = m.group("s1")
    return "{0}".format(s1)


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"(?P<s1>\w)(?P=s1)+", rep1, line))
