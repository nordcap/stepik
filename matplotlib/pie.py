import matplotlib.pyplot as plt

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['m', 'c', 'r', 'y']

plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0, 0.1, 0, 0), autopct='%1.1f%%')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('scatter')
# plt.legend()

plt.show()
