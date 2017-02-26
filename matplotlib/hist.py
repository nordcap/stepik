import matplotlib.pyplot as plt

population_ages = [34, 77, 52, 90, 3, 23, 84, 27, 27, 80, 45, 63, 84, 28, 29, 22]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('histograms')
plt.legend()

plt.show()
