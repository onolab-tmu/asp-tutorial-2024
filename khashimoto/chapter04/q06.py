# ISTFTの実装

import numpy as np
from q05 import window


def istft(S, X):
    F = len(X)
    T = X.shape[1]

    # 1.
    N = 2 * (F - 1)
    M = S * (T - 1) + N

    # 2.
    x = np.zeros(M)

    # 3.
    z = np.zeros((N, T))
    for t in range(T):
        z[:, t] = np.fft.irfft(X[:, t])

    # 4.
    w = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(N) / (N - 1))  # Hamming窓
    w_s = window(S, w)
    n = np.arange(N)
    for t in range(T):
        x[t * S + n] = x[t * S + n] + w_s[n] * z[n, t]

    return x
