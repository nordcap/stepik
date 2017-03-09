"""
Ханойская башня -- одна из широко известных головоломок, условие которой состоит в следующем:
Имеется три стержня (пронумеруем их числами 1, 2 и 3). На первом стержне находится nn колец с радиусами от 1 до nn. Кольца отсортированы по радиусу, и наибольшее кольцо лежит ниже всех.
Вам требуется найти и записать алгоритм переноса всех nn колец с первого стержня на третий по следующим правилам:
за один ход можно переносить только одно кольцо;
нельзя класть большее кольцо на меньшее.
Программа должна вывести на экран кратчайшую последовательность действий, необходимую для того, чтобы перенести все кольца с первого стержня на третий.
Формат ввода:
Строка, содержащая положительное целое число nn.
Формат вывода:
Порядок действий для решения головоломки. Каждое действие записывается на отдельной строке. Действие записывается в формате "номер стержня, с которого снимаем кольцо" - "номер стержня, на который надеваем кольцо" (см. пример работы программы).
Sample Input 1:
2
Sample Output 1:
1 - 2
1 - 3
2 - 3
Sample Input 2:
1
Sample Output 2:
1 - 3
"""

n = int(input())

from_tower = [i for i in range(1, n + 1)]
to_tower = []
buf = []

d = {'1': from_tower,
     '2': buf,
     '3': to_tower
     }

hist = []


def hanoi(n, from_tower, buf, to_tower):
    global hist
    if n > 0:
        hanoi(n - 1, from_tower, to_tower, buf)
        if from_tower:
            to_tower.append(from_tower.pop())
            a, b = '', ''
            for num_tower in d:
                if d[num_tower] == from_tower:
                    a = num_tower
                if d[num_tower] == to_tower:
                    b = num_tower
                if len(a) > 0 and len(b) > 0:
                    # print("from_tower=", from_tower, "to_tower", to_tower, end=" - ")
                    # print("a=", a, "b=", b)
                    print(d)
                    hist.append((a, b))

        hanoi(n - 1, buf, from_tower, to_tower)



hanoi(n, d["1"], d["2"], d["3"])
print(hist)

print('from_tower=', d["1"])
print('buf=', d["2"])
print('to_tower=', d["3"])
