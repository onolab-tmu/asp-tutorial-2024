import numpy as np
from q05 import window

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
    w = window(S, Hamming(N))
    n = np.arange(N)    # ファンシーインデックス
    for t in range(T):
        x[t*S+n] = x[t*S+n] + w[n] * z[n,t]
    return x
