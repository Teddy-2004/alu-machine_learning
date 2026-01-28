#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

fig, ax = plt.subplots()
x = np.arange(1, 4)
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
labels = ['apples', 'bananas', 'oranges', 'peaches']
for i in range(len(fruit)):
    ax.bar(x, fruit[i], color=colors[i], label=labels[i], width=0.5)
ax.set_ylabel("Quantity of Fruit")
ax.set_title("Number of Fruit per Person")
ax.set_ylim([0, 20])
ax.legend()
plt.show()