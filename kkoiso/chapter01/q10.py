import numpy as np
import matplotlib.pyplot as plt
import wave
from scipy.io import wavfile

output_noise = 'sin_wave_with_noise_6dB.wav'
rate, data = wavfile.read(output_noise)


downsampled_data = data[::2]
#1-10
filtered_signal = np.convolve(downsampled_data, np.ones(5)/5, mode='valid')

plt.figure(figsize=(14, 6))
plt.subplot(2, 1, 1)
plt.plot(downsampled_data[:1000])
plt.title("Original Downsampled Signal (8 kHz)")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(filtered_signal[:1000])
plt.title("Filtered Signal (5-point Moving Average)")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
