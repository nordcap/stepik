'''
Напишите функцию is_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если переданный аргумент является числом (целым или вещественным) и False в противном случае.
'''
is_num = lambda s: set(s).issubset(set('-.0123456789')) and s.count('.') < 2 and s[1:].count('-') == 0

print(is_num('1-1'))
print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
