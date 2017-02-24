"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
Sample Input:
catcat
cat and cat
catac
cat
ccaatt
Sample Output:
catcat
cat and cat
"""
import sys, re

for line in sys.stdin:
    line = line.rstrip()
    all_includes = re.findall(r"cat", line)
    if len(all_includes) >= 2:
        print(line)
