array = [1, 2, 4, 8, 16, 32, 64]

array.reverse()
s_money = int(input())
arr_result = []
for i, nominal in enumerate(array):
    col = s_money // nominal
    if col > 0:
        for k in range(col):
            arr_result.append(nominal)
        s_money = s_money % nominal
print(*arr_result)
