# 空間相関行列の確認

import numpy as np
from q04 import spatial_correlation_matrix


def zeropad(L, S, x):
    zero1 = np.zeros(L - S)
    x_pad = np.concatenate([zero1, x])
    zero2 = x_pad.size % S
    if zero2 != 0:
        x_pad = np.concatenate([x_pad, np.zeros(S - zero2)])  # 2.
    x_pad = np.concatenate([x_pad, np.zeros(L - S)])
    return x_pad


def frame(L, S, x):
    x_pad = zeropad(L, S, x)
    T = (x_pad.size - L) // S + 1  # フレーム数
    x_t = np.zeros((T, L))
    for t in range(T):
        for l in range(L):
            x_t[t][l] = x_pad[t * S + l]
    return x_t


def stft(L, S, w, x):
    x_t = frame(L, S, x)
    T = len(x_t)
    x_stft = np.zeros((T, L // 2 + 1), dtype=complex)
    for t in range(T):
        x_stft[t] = np.fft.rfft(x_t[t] * w)
    return x_stft.T


fs = 16000
ts = 5
t = np.arange(ts * fs) / fs
x = np.zeros((ts * fs, 2))
x[:, 0] = np.random.normal(size=ts * fs)
x[:, 1] = np.random.normal(size=ts * fs)

L = 512
S = 256
w = np.hanning(L)

x0_stft = stft(L, S, w, x[:, 0])
x1_stft = stft(L, S, w, x[:, 1])

R_f = spatial_correlation_matrix(x0_stft, x1_stft)
print(R_f[100].real)

# [[191.38231688   5.05200591]
#  [  5.05200591 201.98183266]]
