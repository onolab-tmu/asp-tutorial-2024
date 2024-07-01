# 空間サンプリング定理

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


# 8.
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

    return psi


c = 334
fs = 16000
L = 1024
F = L // 2 + 1
f = np.arange(F) * (fs / 2) / (F - 1)
M = 3
theta = np.pi / 4


# マイク間隔2[cm]
d = 0.02
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
psi1 = beampattern(w_f, p_m, fs)

# マイク間隔5[cm]
d = 0.05
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
psi2 = beampattern(w_f, p_m, fs)

# マイク間隔10[cm]
d = 0.1
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
psi3 = beampattern(w_f, p_m, fs)

Theta = np.arange(361)

plt.subplot(1, 3, 1)
plt.pcolormesh(Theta, f, 20 * np.log10(np.abs(psi1)))
plt.xlabel("Angle[°]")
plt.ylabel("Frequency[Hz]")

plt.subplot(1, 3, 2)
plt.pcolormesh(Theta, f, 20 * np.log10(np.abs(psi2)))
plt.xlabel("Angle[°]")
plt.ylabel("Frequency[Hz]")

plt.subplot(1, 3, 3)
plt.pcolormesh(Theta, f, 20 * np.log10(np.abs(psi3)))
plt.xlabel("Angle[°]")
plt.ylabel("Frequency[Hz]")

plt.show()
