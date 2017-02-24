"""
Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:
class Error1(Error2, Error3 ... ErrorK):
    pass

Антон написал код, который выглядит следующим образом.

try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...
Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде будет
 пойман их предок. Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого положения и
 напишите программу, которая будет определять обработку каких исключений можно удалить из кода.

Важное примечание:
В отличие от предыдущей задачи, типы исключений не созданы.
Создавать классы исключений также не требуется
Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее
 где-то поймали их предка.
"""


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


n = int(input())  # n - число классов исключений.
dict_class = {}
while n > 0:
    n -= 1
    head = input().split(':')
    if len(head) > 1:
        dict_class[head[0].strip()] = head[1].split()
    else:
        dict_class[head[0].strip()] = [head[0].strip()]

m = int(input())  # m - количество обрабатываемых исключений.
list_except = []  # Входной список исключений:
while m > 0:
    m -= 1
    list_except.append(input().strip())

output = []  # выходной список исключений
exception_stack = []  # временный стек исключений

for usr_except in list_except:
    exception_stack.append(usr_except)
    if len(exception_stack) > 1:
        for parent_except in exception_stack[0:-1]:
            list_path = find_path(dict_class, usr_except, parent_except)
            if type(list_path) == list:
                if usr_except not in output:
                    output.append(usr_except)

for out in output:
    print(out)