import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math


def func(x):
    if x == 0:
        return 1
    return math.sin(x) / x


x_min = -20
x_max = 20
dx = 0.01

xlist = mlab.frange(x_min, x_max, dx)
ylist = [func(x) for x in xlist]
ylist2 = [func(x * 0.2) for x in xlist]

plt.plot(xlist, ylist)
plt.plot(xlist, ylist2)

plt.xlabel('Значения Х')
plt.ylabel('Значения У')
plt.title('График  функции sin(x)/x')
plt.show()
