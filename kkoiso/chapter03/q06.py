import numpy as np
import matplotlib.pyplot as plt


def difference_equations_recursion(x):
    y = np.zeros(len(x))
    for n in range(len(x)):
        if n == 0:
            y[n] = 0.4 * x[n]
        else:
            y[n] = 0.3 * y[n - 1] + 0.4 * x[n]
    return y


x = np.zeros(10)
x[0] = 1
y = difference_equations_recursion(x)

plt.stem(y)
plt.title("Difference Equation (Recursive)")
plt.grid(True)
plt.show()
