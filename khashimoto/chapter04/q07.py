# ISTFTの確認

import numpy as np
import matplotlib.pyplot as plt
from q06 import istft
from q03 import stft

A = 1
f = 440
fs = 16000
time = np.arange(fs * 0.1) / fs
x = A * np.sin(2 * np.pi * f * time)  # 正弦波

L = 1000
S = 500
w = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(L) / (L - 1))  # Hamming窓
x_stft = stft(L, S, w, x)  # 4. の結果

x_istft = istft(S, x_stft.T)

plt.plot(x_istft)
plt.show()
