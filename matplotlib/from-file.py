import matplotlib.pyplot as plt

x = []
y = []

with open('example.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        plots = line.rstrip().split(',')
        x.append(plots[0])
        y.append(plots[1])

plt.plot(x, y, label='load from file')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('import data from file')
plt.legend()

plt.show()
