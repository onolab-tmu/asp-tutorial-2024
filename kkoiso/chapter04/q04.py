import numpy as np
import matplotlib.pyplot as plt
from q03 import stft


fs = 16000
f = 440
a = 1.0
t = np.arange(0, 0.1, 1 / fs)
x = a * np.sin(2 * np.pi * f * t)


L = 1000
S = 500
w = np.hamming(L)

stft_matrix = stft(x, L, S, w)

Amplitude_spectrogram = np.abs(stft_matrix)
phase_spectrogram = np.angle(stft_matrix)


plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.title("Ampliitude Spectrogram")
plt.pcolormesh(Amplitude_spectrogram.T)
plt.ylabel("Frequency")
plt.xlabel("Frame")

plt.subplot(2, 1, 2)
plt.title("Phase Spectrogram")
plt.pcolormesh(phase_spectrogram.T)
plt.ylabel("Frequency")
plt.xlabel("Frame")

plt.tight_layout()
plt.show()
