# 窓関数とスペクトルの関係: 

import numpy as np
import matplotlib.pyplot as plt

def hamming(N):
    w = np.zeros(N)
    for n in range(N):
        w[n] = 0.54-0.46 * np.cos(2 * np.pi * n / (N-1))
    return w


A = 1    # 振幅
f = 440    # 周波数
fs = 16000    # サンプリング周波数
T = 3
t = np.arange(fs * T) / fs
x = A * np.sin(2 * np.pi * f * t)    # 第１章１. で作成した信号
X = np.fft.fft(x)

w = hamming(fs*T)
Y = np.fft.fft(w)    # ９. の結果

# X[k]とY[k]の巡回畳み込み
Z = np.zeros(fs*T, dtype=complex)
for k in range(fs*T):
    for n in range(fs*T):
        Z[k] += X[n] * Y[k-n]

idft_z = np.fft.ifft(Z) / (fs * T)

plt.plot(t, idft_z.real)
plt.show()