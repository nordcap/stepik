"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents,
которое содержит список имен прямых предков.
Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс
 не наследуется явно от одного класса более одного раза.
Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в
следующем формате.
<имя класса> : <количество потомков>
Выводить классы следует в лексикографическом порядке.

Sample Input:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:
A : 3
B : 1
C : 2
"""
import sys, json

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

dict_class = {}
dict_count = {}
for line in sys.stdin:
    line = line.strip()
    all_obj = json.loads(line)
    for obj in all_obj:
        dict_class[obj["name"]] = obj["parents"]
        dict_count[obj["name"]] = 1 #словарь для счетчика

    arr_parents = [] #список всех родителей
    for parents in dict_class.values():
        for p in parents:
            arr_parents.append(p)

    arr_parents = list(set(arr_parents))
    for start in arr_parents:
        for stop in dict_count:
            path = find_path(dict_class, start, stop)
            if type(path) == list:
                dict_count[stop] +=1

    for key in sorted(dict_count):
        print(key,":",dict_count[key])
'''
A : 3
B : 1
C : 2
'''
