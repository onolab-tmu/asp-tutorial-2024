# DFT/IDFT の実装: N 点の信号の離散フーリエ変換 (DFT)とその逆変換(IDFT)を計算する関数を実装せよ．

import numpy as np

def dft(x):
    N = len(x)
    dft_X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            dft_X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)
    return dft_X

def idft(X):
    N = len(X)
    idft_x = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            idft_x[n] += X[k] * np.exp(1j * 2 * np.pi * k * n / N)
        idft_x[n] /= N
    return idft_x


# --------------- 確認----------------------
x_1 = np.array([1, 0, 0, 0, 0])
X_1 = dft(x_1)
print(X_1)
x_2 = idft(x_1)
print(x_2)
