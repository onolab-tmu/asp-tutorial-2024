# 差分方程式（再帰なし）

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
y = np.zeros(10)
n = np.arange(10)
y[n] = 0.2 * x[n] + 0.2 * x[n - 1] + 0.2 * x[n - 2] + 0.2 * x[n - 3] + 0.2 * x[n - 4]

plt.stem(y)
plt.show()
