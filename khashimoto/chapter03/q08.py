# 周波数応答

import numpy as np


def FreqRes(a, b, fs, f):
    N = a.size - 1
    M = b.size - 1

    ka = np.arange(1, N + 1)
    kb = np.arange(M + 1)
    H = sum(b[kb] * np.exp(-1j * 2 * np.pi * f / fs * kb)) / (
        1 + sum(a[ka] * np.exp(-1j * 2 * np.pi * f / fs * ka))
    )
    return H
