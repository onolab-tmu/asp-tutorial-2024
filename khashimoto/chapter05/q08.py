# ビームパターン

import numpy as np
import matplotlib.pyplot as plt


# 3.
def array_manifold_vector3(p, theta, f):
    c = 334
    M = p.shape[0]
    a = np.zeros(M, dtype=complex)
    u = np.array([np.sin(theta), np.cos(theta), 0]).T
    for m in range(1, M + 1):
        p_m = p[m - 1]
        a[m - 1] = np.exp(1j * 2 * np.pi * f / c * (u.T @ p_m))
    return a


def beampattern(w_f, p_m, fs):
    F = w_f.shape[0]
    f = np.arange(F) * (fs / 2) / (F - 1)
    psi = np.zeros((F, 361), dtype=complex)

    for i in range(F):
        for theta in range(361):
            theta_rad = theta * np.pi / 180
            # a.
            a_f = array_manifold_vector3(p_m, theta_rad, f[i])
            # b.
            psi[i, theta] = np.conj(w_f[i, :].T) @ a_f

    Theta = np.arange(361)
    # c.
    plt.pcolormesh(Theta, f, 20 * np.log10(np.abs(psi)))
    plt.xlabel("Angle[°]")
    plt.ylabel("Frequency[Hz]")
    plt.show()


c = 334
fs = 16000
L = 1024
F = L // 2 + 1
f = np.arange(F) * (fs / 2) / (F - 1)

# 1. の直線状アレイにおける遅延和ビームフォーマのビームパターンをプロット
d = 0.05
M = 3
theta = np.pi / 4
tau1 = 0
tau2 = d * np.sin(theta) / c
tau3 = 2 * d * np.sin(theta) / c

w_f = np.zeros((F, M), dtype=complex)
for i in range(F):
    w_f[i] = np.array(
        [
            np.exp(-1j * 2 * np.pi * f[i] * tau1),
            np.exp(-1j * 2 * np.pi * f[i] * tau2),
            np.exp(-1j * 2 * np.pi * f[i] * tau3),
        ]
    )
p_m = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])
beampattern(w_f, p_m, fs)
