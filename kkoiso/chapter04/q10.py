import numpy as np
import matplotlib.pyplot as plt
from q03 import stft


def convert(spectrogram, fs, S):
    num_frames, num_freq_bins = spectrogram.shape
    time_axis = np.arange(num_frames) * (S / fs)
    freq_axis = np.linspace(0, fs / 2, num_freq_bins)
    return time_axis, freq_axis


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

time_axis, freq_axis = convert(Amplitude_spectrogram, fs, S)

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.title("Ampliitude Spectrogram")
plt.pcolormesh(time_axis, freq_axis, Amplitude_spectrogram.T)
plt.ylabel("Frequency")
plt.xlabel("Frame")

plt.subplot(2, 1, 2)
plt.title("Phase Spectrogram")
plt.pcolormesh(time_axis, freq_axis, phase_spectrogram.T)
plt.ylabel("Frequency")
plt.xlabel("Frame")

plt.tight_layout()
plt.show()
