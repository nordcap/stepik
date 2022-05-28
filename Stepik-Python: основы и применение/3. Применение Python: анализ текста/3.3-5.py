"""
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

Sample Input:
blabla is a tandem repetition
123123 is good too
go go
aaa
Sample Output:
blabla is a tandem repetition
123123 is good too
"""
import re, sys

for line in sys.stdin:
    line = line.rstrip()
    all_includes = re.findall(r"\b(?P<word>\S+)(?P=word)\b", line)
    if len(all_includes) > 0:
        print(line)

