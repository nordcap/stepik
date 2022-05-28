"""
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".
Sample Input:
\w denotes word character
No slashes here
Sample Output:
\w denotes word character
"""
import re, sys

for line in sys.stdin:
    line = line.rstrip()
    all_includes = re.findall(r"\\", line)
    if len(all_includes) > 0:
        print(line)