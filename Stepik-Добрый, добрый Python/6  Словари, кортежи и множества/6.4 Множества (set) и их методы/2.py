'''
Подвиг 4. Вводится текст в одну строку, слова разделены пробелом. Необходимо подсчитать число уникальных слов (без учета регистра) в этом тексте. Результат (число уникальных слов) вывести на экран.
'''

s = input().lower().split()
print(len(set(s)))
