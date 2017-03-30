import matplotlib.pyplot as plt
import numpy
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def makeData():
    # Строим неравномерную сетку
    x = numpy.random.rand(500) * 20.0 - 10.0
    y = numpy.random.rand(len(x)) * 20.0 - 10.0

    # В узлах рассчитываем значение функции
    z = numpy.sin(x * 0.3) * numpy.sin(y * 0.75)
    return x, y, z


x, y, z = makeData()
fig = plt.figure()
axes = Axes3D(fig)
axes.plot_trisurf(x, y, z)  # триангуляция точек и постройка поверхности
plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.show()
