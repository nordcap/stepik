import matplotlib.pyplot as plt
import numpy
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def makeData():
    # Строим сетку в интервале от -10 до 10 с шагом 0.1 по обоим координатам
    x = numpy.arange(-10, 10, 0.1)
    y = numpy.arange(-10, 10, 0.1)

    # Создаем двумерную матрицу-сетку
    xgrid, ygrid = numpy.meshgrid(x, y)

    # В узлах рассчитываем значение функции
    zgrid = numpy.sin(xgrid) * numpy.sin(ygrid) / (xgrid * ygrid)
    return xgrid, ygrid, zgrid


x, y, z = makeData()
fig = plt.figure()
axes = Axes3D(fig)
axes.plot_surface(x, y, z, cmap=cm.Spectral) #jet, Spectral

plt.show()
