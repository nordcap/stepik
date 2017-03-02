n = int(input())
koch_lst = []


def koch(n):
    if n == 1:
        return ["turn 60", "turn -120", "turn 60"]
    else:
        return koch(n - 1).append("turn 60")

print(koch(n))