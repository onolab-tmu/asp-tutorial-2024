from scipy.signal import chirp
import numpy as np
import matplotlib.pyplot as plt
from q03 import stft

fs = 16000
t = np.linspace(0, 1, fs)
chirp_signal = chirp(t, f0=100, f1=16000, t1=1, method="linear")


params = [(100, 50), (200, 100), (400, 200), (800, 400)]


plt.figure(figsize=(10, 8))
for i, (L, S) in enumerate(params):
    w = np.hamming(L)
    stft_matrix = stft(chirp_signal, L, S, w)
    Amplitude_spectrogram = 2 * np.log(np.abs(stft_matrix))

    plt.subplot(len(params), 1, i + 1)
    plt.pcolormesh(Amplitude_spectrogram.T)
    plt.title(f"Spectrogram Window Size {L} and Shift {S}")
    plt.ylabel("Frequency Bin")
    plt.xlabel("Frame")

plt.tight_layout()
plt.show()
