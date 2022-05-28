'''
Шпаргалка политика
'''

arr = []
while True:
    s = input()
    if s == '.':
        break
    arr.append(s)

arr_nums = []
length = int(input())
for _ in range(length):
    num_s = int(input())
    arr_nums.append(num_s)

for ind in arr_nums:
    print(arr[ind - 1], end='')
