# 空間スペクトル

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


# 4.
def spatial_correlation_matrix(X):
    M, F, T = X.shape
    R = np.zeros((F, M, M), dtype=complex)
    for f in range(F):
        sum = np.zeros((M, M), dtype=complex)
        for t in range(T):
            # a.
            x_ft = np.zeros(M, dtype=complex)
            for m in range(M):
                x_ft[m] = X[m, f, t]
            x_ft = np.array([x_ft]).T

            # b.
            sum = np.add(sum, x_ft @ np.conj(x_ft.T))
        R[f] = sum / T
    return R


def spatialspec(z_m, M, d, f):
    c = 334
    fs = 16000
    L = 1024
    S = 512
    window = np.hanning(L)

    F = L // 2 + 1
    T = (fs + L - S) // S + 1
    # a.
    Z_m = np.zeros((M, F, T), dtype=complex)
    for m in range(M):
        f_, t_, Z_m[m] = signal.stft(z_m[m], fs, window, L, L - S)

    # b.
    R_z = spatial_correlation_matrix(Z_m)

    # c. d.
    P = np.zeros(361, dtype=complex)
    for theta in range(361):
        theta_rad = theta * np.pi / 180
        tau1 = 0
        tau2 = d * np.sin(theta_rad) / c
        tau3 = 2 * d * np.sin(theta_rad) / c
        w = np.array(
            [
                np.exp(-1j * 2 * np.pi * f_[f] * tau1),
                np.exp(-1j * 2 * np.pi * f_[f] * tau2),
                np.exp(-1j * 2 * np.pi * f_[f] * tau3),
            ]
        )

        P[theta] = np.conj(w.T) @ R_z[f] @ w
    return P


# 6.
fs = 16000
sec = 1
A = 1
f = 440

ts = np.arange(fs * sec) / fs
s = A * np.sin(2 * np.pi * f * ts)  # 正弦波

snr = 10
np.random.seed(0)
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


# 10.
z_m = np.array([x1, x2, x3])
M = 3
d = 0.05
Theta = np.arange(361)

freq = np.arange(20, 31)
for i in range(11):
    P = spatialspec(z_m, M, d, freq[i])
    plt.subplot(6, 2, i + 1)
    plt.plot(20 * np.log10(np.abs(P)))

plt.show()
