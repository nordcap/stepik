'''
Дан список слов words. Допишите код после оператора распаковки (*), который оборачивает в двойные кавычки все элементы списка words, а затем печатает результат на одной строке через пробел.
'''

words = 'the world is mine take a look what you have started'.split()

print(*map(lambda x: '"' + x + '"', words))
