'''
Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов, заключенную между первым и последним появлением буквы h, в противоположном порядке.

Формат входных данных: Строка, имеющая две буквы h

Формат выходных данных:  Строка



Sample Input:

In the hole in the ground there lived a hobbit
Sample Output:

In th a devil ereht dnuorg eht ni eloh ehobbit
'''

s = input()

lst1 = s.split('h', 1)
index1 = s.find('h')
index2 = s.rfind('h')

lstLast = s.rsplit('h', 1)

arr = list(s[index1:index2 + 1])

print(lst1[0] + "".join(list(reversed(arr))) + lstLast[1])
