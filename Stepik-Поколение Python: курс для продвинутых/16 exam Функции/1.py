from functools import reduce
import operator

def flatten(data):
    return reduce(operator.concat, data, [])

result = flatten([[1, 2], [3, 4], [], [5]])

print(result)