"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Sample Input 1:
abababa
aba
Sample Output 1:
3
"""

s = input().lower()
t = input().lower()

cnt = 0
end = len(t)
start = 0
while end <= len(s):
    k = s[start:end]
    if s[start:end] == t:
        cnt += 1
    start += 1
    end += 1
print(cnt)
