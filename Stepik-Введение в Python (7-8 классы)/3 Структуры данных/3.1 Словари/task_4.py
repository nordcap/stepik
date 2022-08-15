'''
Права доступа
    Вася написал собственную операционную систему и теперь делает для нее систему прав доступа. Он решил, что в его системе будет 3 категории пользователей, обладающих разными правами:

администраторы (admin) могут открывать и редактировать все файлы

опытные пользователи (experienced) могут открывать все файлы, кроме конфиденциальных (confidential), но не могут редактировать файлы с настройками (settings) и системные файлы (system)

обычные пользователи (user) не могут открывать и/или редактировать конфиденциальные и системные файлы, а также файлы с настройками.

    Все категории пользователей могут открывать и редактировать обычные файлы (ordinary). При этом, если пользователь не имеет права открыть какой-либо файл, то, следовательно, он не имеет права его отредактировать.

    Напишите программу, которая сначала принимает имена файлов и их тип до символа точки, а затем запросы вида

    имя_файла действие категория_пользователя

    Действие может принимать одно из двух значений – read или edit, категория пользователя – одно из трех вышеперечисленных. После каждого действия программа должна выводить "Access granted" или "Access denied" в зависимости от успешности действия. Ввод запросов также происходит до точки.
'''


def check_access(filetype, access, cat_user):
    if cat_user == 'admin':
        return 'Access granted'

    if cat_user == 'experienced':
        if (filetype == 'settings' or filetype == 'system') and access == 'edit':
            return 'Access denied'
        elif filetype == 'confidential':
            return 'Access denied'
        else:
            return 'Access granted'

    if cat_user == 'user':
        if filetype == 'confidential' or filetype == 'settings' or filetype == 'system':
            return 'Access denied'
        else:
            return 'Access granted'


dict_file = {}
while True:
    s = input()
    if s == '.':
        break
    arr = s.split()
    name_file = arr[0]
    type_file = arr[1]
    dict_file[name_file] = type_file

arr_access = []
while True:
    s = input()
    if s == '.':
        break
    arr = s.split()
    name_file = arr[0]
    access = arr[1]
    cat_user = arr[2]
    arr_access.append((name_file, access, cat_user))

# администраторы (admin)
# опытные пользователи (experienced)
# обычные пользователи (user)
for elem in arr_access:
    print(check_access(dict_file[elem[0]], elem[1], elem[2]))
