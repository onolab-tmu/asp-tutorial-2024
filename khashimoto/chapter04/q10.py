# 時間周波数のインデクスと物理量との対応

import numpy as np
import matplotlib.pyplot as plt
from q03 import stft


def convert(x, fs, S):
    L = (len(x) - 1) * 2
    f = np.arange(len(x)) * fs / L
    t = np.arange(x.shape[1]) * S / fs
    return f, t


# ４. の結果を再度プロット
A = 1
f = 440
fs = 16000
time = np.arange(fs * 0.1) / fs
x = A * np.sin(2 * np.pi * f * time)  # 正弦波

L = 1000
S = 500
w = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(L) / (L - 1))  # Hamming窓
x_stft = stft(L, S, w, x)


# プロット
fr, t = convert(x_stft.T, fs, S)

plt.subplot(1, 2, 1)
plt.pcolormesh(t, fr, abs(x_stft).T)
plt.xlabel("Time[s]")
plt.ylabel("Frequency[Hz]")
plt.title("Amplitude spectrum")
plt.subplot(1, 2, 2)
plt.pcolormesh(t, fr, np.angle(x_stft).T)
plt.xlabel("Time[s]")
plt.ylabel("Frequency[Hz]")
plt.title("Phase spectrum")
plt.show()
