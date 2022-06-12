'''
Ханойская башня
'''


def solve_hanoi(n, start, stop):
    if n == 1:
        print(f"Переносим диск {n} с {start} на {stop}")
    else:
        tmp = 6 - start - stop
        solve_hanoi(n - 1, start, tmp)
        print(f"Переносим диск {n} с {start} на {stop}")
        solve_hanoi(n - 1, tmp, stop)


n = 4
start = 1
stop = 3

solve_hanoi(n, start, stop)
