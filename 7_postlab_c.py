import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 5, 6, 7, 8])
common = np.intersect1d(x, y)
print(common)
