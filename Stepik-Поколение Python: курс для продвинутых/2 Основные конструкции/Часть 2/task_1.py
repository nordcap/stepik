'''
Координатные четверти
'''

n = int(input())

count1 = 0
count2 = 0
count3 = 0
count4 = 0
for _ in range(n):
    arr = [int(i) for i in input().split()]
    if arr[0] > 0 and arr[1] > 0:
        count1 += 1
    elif arr[0] < 0 and arr[1] > 0:
        count2 += 1
    elif arr[0] < 0 and arr[1] < 0:
        count3 += 1
    elif arr[0] > 0 and arr[1] < 0:
        count4 += 1

print(f'Первая четверть: {count1}')
print(f'Вторая четверть: {count2}')
print(f'Третья четверть: {count3}')
print(f'Четвертая четверть: {count4}')
