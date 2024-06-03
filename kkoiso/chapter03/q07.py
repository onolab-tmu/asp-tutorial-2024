import numpy as np
import matplotlib.pyplot as plt


def general_difference_equations(a, b, x):
    N = len(a)
    M = len(b)
    L = len(x)
    y = np.zeros(L)
    for n in range(1, L + 1):
        for k in range(1, N + 1):
            if n >= k:
                y[n] = y[n] - a[k] * y[n - k]
        for k in range(M + 1):
            if n >= k:
                y[n] = y[n] + b[k] * x[n - k]
        y[n] = y[n] / a[0]
    return y
