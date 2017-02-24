"""
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w﻿.
Sample Input:
this is a text
"this' !is. ?n1ce,
Sample Output:
htis si a etxt
"htis' !si. ?1nce,
Нажмите, чтобы начать решать ✍

"""
import re, sys


def rep12(m):
    s1 = m.group("s1")
    s2 = m.group("s2")
    other = m.group("other")
    return "{0}{1}{2}".format(s2, s1, other)


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"(?P<s1>\w)(?P<s2>\w)(?P<other>\w*)", rep12, line))
