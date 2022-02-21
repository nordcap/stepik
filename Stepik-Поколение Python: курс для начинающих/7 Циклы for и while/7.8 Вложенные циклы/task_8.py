'''
Гипотеза Эйлера о сумме степеней 🌶️🌶️
'''

for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                for e in range(d, 151):
                    if e ** 5 > a ** 5 + b ** 5 + c ** 5 + d ** 5:
                        break
                    if int(a ** 5) + int(b ** 5) + int(c ** 5) + int(d ** 5) == int(e ** 5):
                        print(f"a={a} b={b} c={c} d={d} e={e}")
                        print(a + b + c + d + e)
                        print("end")
                        exit(0)
        print(f"a={a}  b={b}")

