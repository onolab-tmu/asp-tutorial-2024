# 不確定性原理の確認

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp
from q03 import stft

fs = 16000
t = np.arange(0, fs) / fs
sig = chirp(t, f0=100, f1=16000, t1=1)

# スペクトログラムのプロット

# 100/50
L = 100
S = 50
w = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(L) / (L - 1))  # Hamming窓
sig_stft = stft(L, S, w, sig)

plt.subplot(4, 2, 1)
plt.pcolormesh(abs(sig_stft).T)
plt.title("Amplitude spectrum (100/50)")
plt.subplot(4, 2, 2)
plt.pcolormesh(np.angle(sig_stft).T)
plt.title("Phase spectrum (100/50)")

# 200/100
L = 200
S = 100
w = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(L) / (L - 1))  # Hamming窓
sig_stft = stft(L, S, w, sig)

plt.subplot(4, 2, 3)
plt.pcolormesh(abs(sig_stft).T)
plt.title("Amplitude spectrum (200/100)")
plt.subplot(4, 2, 4)
plt.pcolormesh(np.angle(sig_stft).T)
plt.title("Phase spectrum (200/100)")

# 400/200
L = 400
S = 200
w = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(L) / (L - 1))  # Hamming窓
sig_stft = stft(L, S, w, sig)

plt.subplot(4, 2, 5)
plt.pcolormesh(abs(sig_stft).T)
plt.title("Amplitude spectrum (400/200)")
plt.subplot(4, 2, 6)
plt.pcolormesh(np.angle(sig_stft).T)
plt.title("Phase spectrum (400/200)")

# 800/400
L = 800
S = 400
w = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(L) / (L - 1))  # Hamming窓
sig_stft = stft(L, S, w, sig)

plt.subplot(4, 2, 7)
plt.pcolormesh(abs(sig_stft).T)
plt.title("Amplitude spectrum (800/400)")
plt.subplot(4, 2, 8)
plt.pcolormesh(np.angle(sig_stft).T)
plt.title("Phase spectrum (800/400)")
plt.show()
