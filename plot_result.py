import numpy as np
import matplotlib.pyplot as plt


x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
y1 = [0.87495, 0.89691, 0.91029, 0.92091, 0.93221, 0.94060, 0.95100, 0.95694, 0.96832, 0.97585]
y2 = [0.68316, 0.73777, 0.78941, 0.83060, 0.85989, 0.88582, 0.90809, 0.93483, 0.95964, 0.98452]
y3 = [0.54875, 0.61845, 0.66855, 0.70798, 0.74630, 0.77765, 0.81372, 0.83967, 0.88378, 0.91460]
y4 = [0.78775, 0.81979, 0.84149, 0.85895, 0.87709, 0.89141, 0.90898, 0.91949, 0.93984, 0.95360]
plt.title('Result Analysis')
plt.plot(x, y1, color='green', label='overall acc.')
plt.plot(x, y2, color='red', label='mean acc.')
plt.plot(x, y3, color='yellow', label='IU')
plt.plot(x, y4, color='blue', label='fwavacc')
plt.legend()


plt.xlabel('percent')
plt.ylabel('rate')

for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=6)
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=6)
for a, b in zip(x, y3):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=6)
for a, b in zip(x, y4):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=6)
plt.savefig('G://8598_increasingLaw.jpg')
plt.show()
