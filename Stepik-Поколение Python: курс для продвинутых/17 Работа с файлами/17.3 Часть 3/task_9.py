'''
CSV-файл
Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна содержать реализованную функцию read_csv.

Примечание 1. Вызывать функцию read_csv не нужно.

Примечание 2. Функция read_csv не должна принимать аргументов.

Примечание 2. Подробнее прочитать про CSV-файлы можно тут.

Примечание 3. Считайте, что все ключи и значения по этим ключам в результирующем словаре имеют строковый тип (str).
'''


def read_csv():
    result = []
    with open('data.csv', encoding='utf-8') as file:
        headers = [head.strip() for head in file.readline().split(',')]
        for line in file:
            one_line = [l.strip() for l in line.split(',')]

            create_tuple_list = list(zip(headers, one_line))
            dictionary = dict(create_tuple_list)
            result.append(dictionary)
    return result


read_csv()
