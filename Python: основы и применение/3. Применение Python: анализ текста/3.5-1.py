"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго
с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз
в 2015 году.
"""
import csv, re

out_dict = dict()
arr_primary_type = []
with open("Crimes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        year = re.findall(r"\d{2}/\d{2}/(\d{4})", row['Date'])
        if year[0] == '2015':
            arr_primary_type.append(row['Primary Type'])

    uniq_type = list(set(arr_primary_type))
    for u_type in uniq_type:
        out_dict[u_type] = arr_primary_type.count(u_type)
    print(sorted(out_dict.items(), key=lambda v: v[1], reverse=True)[0][0])

