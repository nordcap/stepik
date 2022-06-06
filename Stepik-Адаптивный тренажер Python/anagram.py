"""
Напишите программу, которая проверяет, являются ли два введённых слова анаграммами.
Программа должна вывести True в случае, если введённые слова являются анаграммами, и False
 в остальных случаях.

Формат ввода:
Два слова, каждое на отдельной строке.
Слово может состоять только из латинских символов произвольного регистра. Регистр символов не должен влиять на ответ.
Формат вывода:
True или False.

Sample Input 1:
silent
listen
Sample Output 1:
True
Sample Input 2:
AbaCa
AcaBa
Sample Output 2:
True
Sample Input 3:
abaca
acada
Sample Output 3:
False
"""

s1 = list(input().lower())
s2 = list(input().lower())
set_uniq = set(s1)
flag = True
for sym in set_uniq:
    if (s1.count(sym) != s2.count(sym)):
        flag = False
if ((len(s1) != len(s2)) or (flag == False)):
    print('False')
else:
    print('True')

