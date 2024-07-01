# 遅延和ビームフォーマ

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# 6.
fs = 16000
sec = 1
A = 1
f = 440

ts = np.arange(fs * sec) / fs
s = A * np.sin(2 * np.pi * f * ts)  # 正弦波

snr = 10
noise = np.random.randn(fs * sec)
noise /= np.sqrt(np.sum(noise**2))
noise *= np.sqrt(np.sum(s**2))
a = 10 ** (-snr / 20)
noise = a * noise  # ホワイトノイズ

x1 = np.zeros(fs * sec)
x2 = np.zeros(fs * sec)
x3 = np.zeros(fs * sec)
for n in range(fs * sec):
    x1[n] = s[n] + noise[n]
    x2[n] = s[n - 10] + noise[n]
    x3[n] = s[n - 20] + noise[n]


# 7.
L = 1024
S = 512
window = np.hanning(L)
# a.
f_, t_, X1 = signal.stft(x1, fs, window, L, L - S)
f_, t_, X2 = signal.stft(x2, fs, window, L, L - S)
f_, t_, X3 = signal.stft(x3, fs, window, L, L - S)


F, T = X1.shape
f = np.arange(F) * (fs / 2) / (F - 1)
tau1 = 0
tau2 = 10 / fs
tau3 = 20 / fs

Y = np.zeros((F, T), dtype=complex)
for i in range(F):
    # c.
    w_f = (
        np.array(
            [
                np.exp(-1j * 2 * np.pi * f[i] * tau1),
                np.exp(-1j * 2 * np.pi * f[i] * tau2),
                np.exp(-1j * 2 * np.pi * f[i] * tau3),
            ]
        )
        / 3
    )
    for j in range(T):
        # b.
        x_ft = np.array([X1[i, j], X2[i, j], X3[i, j]]).T
        # d.
        Y[i, j] = np.conj(w_f.T) @ x_ft

# e.
t_Y, Y_istft = signal.istft(Y, fs, window, L, L - S)

plt.plot(t_Y, Y_istft)
plt.xlim(0, 0.01)
plt.show()
