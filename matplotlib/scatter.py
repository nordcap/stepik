import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [6, 3, 9, 2, 7, 0, 2, 4]

plt.scatter(x, y, label='scatterlabel', color='red', marker='*')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('scatter')
plt.legend()

plt.show()
