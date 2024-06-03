import numpy as np
import matplotlib.pyplot as plt
from q08 import calc_H

fs = 16000
a = np.array([0, 0.3])
b = np.array([0.4, 0])
N = 4000

# グラフ用の配列
omegas = np.zeros(N)
Hs = np.zeros(N, dtype=complex)
for i in range(N):
    f = i / N * fs
    omega = 2 * np.pi * f / fs
    omegas[i] = omega
    Hs[i] = calc_H(a, b, omega)


A = np.abs(Hs)
P = np.rad2deg(np.angle(Hs))
# グラフの中心を調整
omegas = omegas - 3
A = np.roll(A, 2000)
P = np.roll(P, 2000)

fig = plt.figure()
fig.add_subplot(1, 2, 1)
plt.stem(omegas, A)
plt.title('Amplitude Characteristics')
plt.xlabel('omega')
fig.add_subplot(1, 2, 2)
plt.stem(omegas, P)
plt.title('Phase Characteristics')
plt.xlabel('omega')
fig.savefig('q10_graph')

