# 差分方程式（一般系）

import numpy as np


def DifferenceEquation(a, b, x):
    N = a.size - 1
    M = b.size - 1
    L = x.size

    y = np.zeros(L)
    ka = np.arange(1, N + 1)
    kb = np.arange(M + 1)
    for n in range(L):
        y[n] = (-sum(a[ka] * y[n - ka]) + sum(b[kb] * x[n - kb])) / a[0]

    return y
