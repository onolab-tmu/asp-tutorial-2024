import numpy as np
import matplotlib.pyplot as plt
from q05 import synthesis_window

import numpy as np


def istft(X, S, w):

    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N

    x_hat = np.zeros(M)
    w_s = synthesis_window(w, S)
    for t in range(T):
        z_t = np.fft.irfft(X[:, t], n=N)

        for n in range(N):
            x_hat[t * S + n] += w_s[n] * z_t[n]

    return x_hat
