'''
Дополните приведенный код, используя списочное выражение так, чтобы получить новый список, содержащий строки исходного списка с удаленным первым символом.
'''
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [m[1:] for m in keywords]

print(new_keywords)
