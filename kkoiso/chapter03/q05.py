import numpy as np
import matplotlib.pyplot as plt


def difference_equations_no_recursion(x):
    y = np.zeros(len(x))
    for n in range(len(x)):
        y[n] = 0.2 * x[n]
        if n >= 1:
            y[n] = y[n] + 0.2 * x[n - 1]
        if n >= 2:
            y[n] = y[n] + 0.2 * x[n - 2]
        if n >= 3:
            y[n] = y[n] + 0.2 * x[n - 3]
        if n >= 4:
            y[n] = y[n] + 0.2 * x[n - 4]
    return y


x = np.zeros(10)
x[0] = 1
y = difference_equations_no_recursion(x)

plt.stem(y)
plt.title("Difference Equation (Non-recursive)")
plt.grid(True)
plt.show()
