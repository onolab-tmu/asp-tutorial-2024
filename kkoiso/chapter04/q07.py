import numpy as np
import matplotlib.pyplot as plt
from q03 import stft
from q06 import istft
from q05 import synthesis_window

fs = 16000
f = 440
a = 1.0
t = np.arange(0, 0.1, 1 / fs)
x = a * np.sin(2 * np.pi * f * t)


L = 1000
S = 500
w = np.hamming(L)
w_s = synthesis_window(w, S)
stft_matrix = stft(x, L, S, w)
x_reconstructed = istft(stft_matrix, S, w)
plt.figure(figsize=(10, 4))

plt.subplot(2, 1, 1)
plt.plot(x)
plt.title("Original Signal")

plt.subplot(2, 1, 2)
plt.plot(x_reconstructed)
plt.title("Reconstructed Signal")

plt.tight_layout()
plt.show()
