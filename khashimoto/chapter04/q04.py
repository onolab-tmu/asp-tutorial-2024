# STFTの確認

import numpy as np
import matplotlib.pyplot as plt
from q03 import stft

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
T = np.arange(len(x_stft))  # 時間軸
fr = np.arange(x_stft.shape[1]) / x_stft.shape[1] * fs / 2  # 周波数軸

plt.subplot(1, 2, 1)
plt.pcolormesh(T, fr, abs(x_stft).T)
plt.xlabel("Time[s]")
plt.ylabel("Frequency[Hz]")
plt.title("Amplitude spectrum")
plt.subplot(1, 2, 2)
plt.pcolormesh(T, fr, np.angle(x_stft).T)
plt.xlabel("Time[s]")
plt.ylabel("Frequency[kHz]")
plt.title("Phase spectrum")
plt.show()
