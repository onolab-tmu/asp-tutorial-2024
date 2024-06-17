import numpy as np

def linear_conv(x, h):
    N = x.size
    z = np.zeros(2*N-1, dtype=complex)
    k = np.arange(N)
    h_addzeros = np.hstack([h, np.zeros(N)])
    for n in range(2*N-1):
        z[n] = np.sum(x[k] * h_addzeros[n-k])
    return z