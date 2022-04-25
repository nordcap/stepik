'''
Сопряженные числа
'''

n = int(input())
z1, z2 = complex(input()), complex(input())

s_z1 = complex(z1.real, -z1.imag)
s_z2 = complex(z2.real, -z2.imag)

print(z1 ** n + z2 ** n + s_z1 ** n + s_z2 ** (n + 1))
