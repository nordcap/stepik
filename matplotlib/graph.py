import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]
x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x, y, label="Первый график")
plt.plot(x2, y2, label='Второй график')
plt.xlabel('Значения Х')
plt.ylabel('Значения У')
plt.title('График какой-то функции')
plt.legend()

plt.show()
