'''
В данном задании вам необходимо провести частотный анализ текста. А именно: вывести самое часто встречаемое слово в тексте и его количество встречаний.

Перед тем, как обрабатывать строку, учтите:

1) Слова с маленькой и большой заглавной буквы эквивалентны. Т.е  слово "Weather" и "weather" считаются одинаковыми.

2) Словом считается последовательность символов, ограниченная пробелами и(или) знаками препинания("." , ",", "!", "?", ";", ":").

3) Если самых частых слов несколько, выбирается то, которое стоит первым в лексикографическом порядке.

Примечание: Возможно Вам помогут такие функции обработки строк, такие как split, strip, replace и lower, а также знание функции max.

Формат входных данных: Число строк, затем сами строки.

Формат выходных данных: Слово и число

Sample Input 1:

4
She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are seaside shore shells.
Sample Output 1:

shells 6
Sample Input 2:

6
Children are skiing,
Children are skating,
Sledging down the hills.
Winter is charming,
When it was coming
With snow and frost that all are around
.
Sample Output 2:

are 3
'''


def func(val):
    val = val.replace(".", " ").strip()
    val = val.replace(",", " ").strip()
    val = val.replace("!", " ").strip()
    val = val.replace("?", " ").strip()
    val = val.replace(";", " ").strip()
    val = val.replace(":", " ").strip()
    return val.lower()


n = int(input())
all = []
while n > 0:
    arr = input().split()
    all.extend(arr)
    n = n - 1
listList = list(map(func, all))
setList = set(listList)
mapList = dict()
for i in setList:
    countList = listList.count(i)
    mapList[i] = countList

maxValue = max(list(mapList.values()))  # макс.значение элемента

for key in sorted(mapList):
    if (mapList[key] == maxValue):
        print(key, maxValue)
        exit()
