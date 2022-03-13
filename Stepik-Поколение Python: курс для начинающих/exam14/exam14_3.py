'''
Биномиальный коэффициент 🌶️
'''
import math

# объявление функции
def compute_binom(n, k):
    fact_n = math.factorial(n)
    fact_k = math.factorial(k)
    return int(fact_n / (fact_k * math.factorial(n - k)))


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
