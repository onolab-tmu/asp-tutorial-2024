# アレイマニフォールドベクトル（直線状アレイ）

import numpy as np


def array_manifold_vector1(d, M, theta, f):
    c = 334
    a = np.zeros(M, dtype=complex)
    u = np.array([np.sin(theta), np.cos(theta), 0]).T
    for m in range(1, M + 1):
        p_m = np.array([((m - 1) - (M - 1) / 2) * d, 0, 0]).T
        a[m - 1] = np.exp(1j * 2 * np.pi * f / c * np.dot(u, p_m))
    return a


d = 0.05
M = 3
theta = np.pi / 4
f = 1000
print(array_manifold_vector1(d, M, theta, f))

# [0.7868537-0.61713958j 1.       +0.j         0.7868537+0.61713958j]
