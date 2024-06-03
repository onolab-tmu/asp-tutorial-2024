import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(14)
x[8] = 1
y = np.zeros(10)
n = np.arange(4, 14)  # ファンシーインデックス
y = 0.2 * (x[n] + x[n-1] + x[n-2] + x[n-3] + x[n-4])

fig = plt.figure()
plt.stem(y)
fig.savefig('q05_graph')