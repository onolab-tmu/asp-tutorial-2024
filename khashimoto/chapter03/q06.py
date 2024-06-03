# 差分方程式（再帰あり）

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
y = np.zeros(10)
for n in range(10):
    y[n] = 0.3 * y[n - 1] + 0.4 * x[n]

plt.stem(y)
plt.show()
