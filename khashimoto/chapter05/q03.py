# アレイマニフォールドベクトル（一般）

import numpy as np


def array_manifold_vector3(p, theta, f):
    c = 334
    M = len(p)
    a = np.zeros(M, dtype=complex)
    u = np.array([np.sin(theta), np.cos(theta), 0]).T
    for m in range(1, M + 1):
        p_m = p[m - 1].T
        a[m - 1] = np.exp(1j * 2 * np.pi * f / c * np.dot(u, p_m))
    return a


# 1.
p = np.array([[-0.05, 0, 0], [0, 0, 0], [0.05, 0, 0]])
theta = np.pi / 4
f = 1000
print(array_manifold_vector3(p, theta, f))

# [0.7868537-0.61713958j 1.       +0.j         0.7868537+0.61713958j]

# 2.
p = np.array(
    [
        [0, 0.05, 0],
        [0.05 * (np.sqrt(3) / 2), 0.05 * (-1 / 2), 0],
        [0.05 * (-np.sqrt(3) / 2), 0.05 * (-1 / 2), 0],
    ]
)
theta = np.pi / 4
f = 1000
print(array_manifold_vector3(p, theta, f))

# [0.7868537 +0.61713958j 0.97051349+0.2410468j  0.6148926 -0.78861086j]
