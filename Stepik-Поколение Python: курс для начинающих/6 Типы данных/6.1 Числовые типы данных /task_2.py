'''
Две старушки
Две старушки идут навстречу друг другу с постоянными скоростями V1 V2 км/ч.
Определите, через какое время старушки встретятся, если расстояние между ними равно SS км.
'''

s = float(input())
v1 = float(input())
v2 = float(input())

t = s / (v1 + v2)
print(t)
