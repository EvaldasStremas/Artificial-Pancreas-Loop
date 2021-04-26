import random
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])

glucose_level = 6

for i in range(100):
    y = glucose_level
    plt.scatter(i, y)
    #glucose_level += random.uniform(0, 0.2)
    glucose_level += (random.choice((-1, 1)) * random.uniform(0, 0.2))
    plt.pause(0.05)

plt.show()