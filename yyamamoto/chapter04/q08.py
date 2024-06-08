import numpy as np
import matplotlib.pyplot as plt
from q03 import stft

def Hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2*np.pi*n/(N-1))
    return w

def istft(S, X):
    # 手順1
    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    # 手順2
    x = np.zeros(M)
    # 手順3
    z = np.zeros((2*(F-1), T))
    for t in range(T):
        z[:,t] = np.fft.irfft(X[:,t])
    # 手順4
    w = np.full(N, 1)
    n = np.arange(N)    # ファンシーインデックス
    for t in range(T):
        x[t*S+n] = x[t*S+n] + w[n] * z[n,t]
    return x

L = 1000
S = 500
fs = 16000
f = 440
time = 0.1
t = np.arange(fs * time) / fs
sin_wave = np.sin(2 * np.pi * f * t)

H = Hamming(L)
sin_stft = stft(L, S, H, sin_wave).T

sin_istft = istft(S, sin_stft)


fig = plt.figure()
plt.plot(sin_istft)
fig.savefig("./yyamamoto/chapter04/q08_graph.png")