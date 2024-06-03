import numpy as np

def linear_conv2(x, h):
    N = x.size
    z = np.zeros(N, dtype=complex)
    k = np.arange(N)
    h_addzeros = np.hstack([h, np.zeros(N)])
    for n in range(N):
        z[n] = np.sum(x[k] * h_addzeros[n-k])
    return z