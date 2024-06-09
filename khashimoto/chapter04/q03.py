# STFTの実装

import numpy as np
from q02 import frame


def stft(L, S, w, x):
    x_t = frame(L, S, x)
    T = len(x_t)
    x_stft = np.zeros((T, L // 2 + 1), dtype=complex)
    for t in range(T):
        x_stft[t] = np.fft.rfft(x_t[t] * w)
    return x_stft
