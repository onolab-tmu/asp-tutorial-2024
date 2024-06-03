import numpy as np
import matplotlib.pyplot as plt

def difference_equation(x, y, n):
    if n == 0:
        return 0.4 * x[n]
    else:
        return 0.3 * y[n-1] + 0.4 * x[n]

x = np.zeros(10)
x[5] = 1
y = np.zeros(10)

for n in range(10):
    y[n] = difference_equation(x, y, n)

fig = plt.figure()
plt.stem(y)
fig.savefig('q06_graph')