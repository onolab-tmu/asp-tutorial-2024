import numpy as np

def circular_conv(x, h):
    N = x.size
    z = np.zeros(N, dtype=complex)
    k = np.arange(N)
    for n in range(N):
        z[n] = np.sum(x[k] * h[(n-k) % N])
    return z