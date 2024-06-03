import numpy as np
import matplotlib.pyplot as plt


def circular_conv(x, h):
    N = len(x)
    z = np.zeros(N)
    for n in range(N):
        for k in range(N):
            z[n] = z[n] + x[k] * h[(n - k) % N]
    return z
