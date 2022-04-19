'''
Словарь программиста
Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык. Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. Напишите программу создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из этого словаря.

Формат входных данных
В первой строке задано одно целое число nn — количество слов в словаре. В следующих nn строках записаны слова и их определения, разделенные двоеточием и символом пробела. В следующей строке записано целое число mm — количество поисковых слов, чье определение нужно вывести. В следующих mm строках записаны сами слова, по одному на строке.

Формат выходных данных
Для каждого слова, независимо от регистра символов, если оно присутствует в словаре, необходимо вывести его определение. Если слова в словаре нет, программа должна вывести "Не найдено", без кавычек.

Примечание 1. Мини-словарь для начинающих разработчиков можно посмотреть тут.

Примечание 2. Гарантируется, что в определяемом слове или фразе отсутствует двоеточие (:), следом за которым идёт пробел.
'''

n = int(input())
dictionary = {}

for _ in range(n):
    arr = [w for w in input().split(': ')]
    dictionary[arr[0].lower()] = arr[1]

m = int(input())

words = [input() for _ in range(m)]
for word in words:
    print(dictionary.get(word.lower(), "Не найдено"))
