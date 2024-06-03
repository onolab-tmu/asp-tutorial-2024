import numpy as np
import matplotlib.pyplot as plt


def linear_conv(x, h):
    N = len(x)
    z = np.zeros(2 * N - 1)
    for n in range(2 * N - 1):
        for k in range(N):
            if 0 <= n - k <= N - 1:
                z[n] = z[n] + x[k] * h[n - k]
    return z
