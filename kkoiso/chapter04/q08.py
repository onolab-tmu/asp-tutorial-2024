import numpy as np
import matplotlib.pyplot as plt
from q03 import stft


def unity_synthesis_window(X, S):
    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N

    x_hat = np.zeros(M)

    for t in range(T):
        z_t = np.fft.irfft(X[:, t], n=N)
        x_hat[t * S : t * S + N] += z_t

    return x_hat


fs = 16000
f = 440
a = 1.0
t = np.arange(0, 0.1, 1 / fs)
x = a * np.sin(2 * np.pi * f * t)


L = 1000
S = 500
w = np.hamming(L)
stft_matrix = stft(x, L, S, w)

x_reconstructed_unity_ws = unity_synthesis_window(stft_matrix, S)


plt.figure(figsize=(10, 4))

plt.subplot(2, 1, 1)
plt.plot(x)
plt.title("Original Signal")

plt.subplot(2, 1, 2)
plt.plot(x_reconstructed_unity_ws)
plt.title("Reconstructed Signal with Unity Synthesis Window")

plt.tight_layout()
plt.show()
