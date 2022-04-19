'''
Анаграммы 1
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание). Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае.
'''

word1 = input()
word2 = input()

dict1 = {}
dict2 = {}
for i in word1:
    dict1[i] = dict1.get(i, 0) + 1

for j in word2:
    dict2[j] = dict2.get(j, 0) + 1

if dict1 == dict2:
    print("YES")
else:
    print("NO")
