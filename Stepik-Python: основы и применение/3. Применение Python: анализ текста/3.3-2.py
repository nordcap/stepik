"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.
Sample Input:
cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?
Sample Output:
cat
catapult and cat
"cat"
!cat?
"""

import re, sys

for line in sys.stdin:
    line = line.rstrip()
    all_includes = re.findall(r"\bcat\b", line)
    if len(all_includes) > 0:
        print(line)
