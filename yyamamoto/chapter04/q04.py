import numpy as np
import matplotlib.pyplot as plt
from q03 import stft

def Hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2*np.pi*n/(N-1))
    return w

fs = 16000
f = 440
time = 0.1
t = np.arange(fs * time) / fs
sin_wave = np.sin(2 * np.pi * f * t)

H = Hamming(1000)
sin_stft = stft(1000, 500, H, sin_wave)

# スペクトログラムの準備
# T = np.shape(sin_stft)[0]
A = 20 * np.log10(np.abs(sin_stft))
P = np.angle(sin_stft)

A = A.T
P = P.T
fig = plt.figure()
fig.add_subplot(1, 3, 1)
plt.pcolormesh(np.log10(np.abs(sin_stft) ** 2).T)
plt.title("Spectrogram")
fig.add_subplot(1, 3, 2)
plt.pcolormesh(A)
plt.title("Amplitude Spectrogram")
fig.add_subplot(1, 3, 3)
plt.pcolormesh(P)
plt.title("Phase Spectrogram")
plt.show()
fig.savefig("./yyamamoto/chapter04/q04_graph.png")