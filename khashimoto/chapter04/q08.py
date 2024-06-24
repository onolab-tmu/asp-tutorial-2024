# 合成窓の確認

import numpy as np
import matplotlib.pyplot as plt
from q03 import stft


def istft_2(S, X):
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
    n = np.arange(N)
    for t in range(T):
        x[t * S + n] = x[t * S + n] + 1 * z[n, t]  # w_s[n] = 1

    return x


A = 1
f = 440
fs = 16000
time = np.arange(fs * 0.1) / fs
x = A * np.sin(2 * np.pi * f * time)  # 正弦波

L = 1000
S = 500
w = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(L) / (L - 1))  # Hamming窓
x_stft = stft(L, S, w, x)  # 4. の結果

x_istft = istft_2(S, x_stft.T)

plt.plot(x_istft)
plt.show()
