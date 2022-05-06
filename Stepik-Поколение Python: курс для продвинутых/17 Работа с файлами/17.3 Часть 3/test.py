from functools import reduce

def func(x,y):
    return x[1]+y[1]


arr = [('A', 1), ('new', 3), ('report', 6), ('on', 2)]
num_letters = reduce(func, arr, (0,0))
print(arr)