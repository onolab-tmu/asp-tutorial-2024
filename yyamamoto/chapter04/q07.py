import numpy as np
import matplotlib.pyplot as plt
from q06 import istft
from q03 import stft

def Hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2*np.pi*n/(N-1))
    return w

L = 1000
S = 500
fs = 16000
f = 440
time = 0.1
t = np.arange(fs * time) / fs
sin_wave = np.sin(2 * np.pi * f * t)

H = Hamming(L)
sin_stft = stft(L, S, H, sin_wave).T

# ここからq07
sin_istft = istft(S, sin_stft)


fig = plt.figure()
plt.plot(sin_istft)
fig.savefig("./yyamamoto/chapter04/q07_graph.png")
