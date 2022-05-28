"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.

Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
Sample Output:
zabcz
zzxzz
"""
import re, sys

for line in sys.stdin:
    line = line.rstrip()
    all_includes = re.findall(r"z(\S){3}z", line)
    if len(all_includes) > 0:
        print(line)
