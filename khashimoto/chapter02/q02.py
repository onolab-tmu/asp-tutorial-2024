# DFT の確認: 1.で実装した関数を用いて 8 点の単位インパルス信号 の DFT を計算せよ.

import numpy as np

def dft(x):
    N = len(x)
    dft_X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            dft_X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)
    return dft_X

delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])
X = dft(delta)
print(X)