from nnfs.datasets import spiral_data
import nnfs
import numpy as np

# sets random seed to 0 (by default), creates float32 dtype
# overrides original dotp from numpy. Meant to ensure repeatable results
nnfs.init()

import matplotlib.pyplot as plt

X, y = spiral_data(samples=100, classes=3)

plt.scatter(X[:, 0], X[:, 1])
plt.show()
