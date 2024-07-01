import numpy as np
import matplotlib.pyplot as plt
from q05 import stft
from q06 import white_noise

def window(S, w):
    L = len(w)
    Q = L // S
    w_s = np.zeros(L)
    for l in range(L):
        den = 0
        for m in range(-(Q-1), Q):
            if 0 <= l - m * S & l - m * S < L:
                den += w[l-m*S] ** 2
        w_s[l] = w[l] / den
    return w_s

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
    w = window(S, np.hanning(N))

    n = np.arange(N)    # ファンシーインデックス
    for t in range(T):
        x[t*S+n] = x[t*S+n] + w[n] * z[n,t]
    return x

fs = 16000
time = 1
f = 440
t = np.arange(-20, fs * time) / fs      # 20サンプル分手前に作っておく
s = np.sin(2 * np.pi * f * t)
epsilon = white_noise(s[20::], 10)
x1 = s[20:] + epsilon
x2 = s[10:len(s) - 10] + epsilon
x3 = s[:len(s) - 20] + epsilon

# ここからq07
L = 1024
S = 512
han = np.hanning(L)
X1 = stft(L, S, han, x1).T
X2 = stft(L, S, han, x2).T
X3 = stft(L, S, han, x3).T
F, T = X1.shape
Y = np.zeros((X1.shape), dtype=complex)
for f_idx in range(F):
    f = fs / 2 / (F - 1) * f_idx
    w_f = np.exp(np.array([0, -1j * 2 * np.pi * f * 10 / fs, -1j * 2 * np.pi * f * 20 / fs])) / 3
    for t in range(T):
        x_ft = np.array([[X1[f_idx][t], X2[f_idx][t], X3[f_idx][t]]]).T
        Y[f_idx][t] = (np.conjugate(w_f) @ x_ft)[0]
        
print(Y)
Y_istft = istft(S, Y)

print("\n\n\n\n")
print(Y_istft)

t = np.arange(len(Y_istft)) / fs
fig = plt.figure()
plt.plot(t, Y_istft)
plt.xlim([0.5, 0.51])
plt.xlabel("time[s]")
fig.savefig('./yyamamoto/chapter05/q07_graph.png')

