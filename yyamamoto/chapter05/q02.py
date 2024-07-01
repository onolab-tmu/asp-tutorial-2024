import numpy as np

def circular_array_manifold_vector(r, M, theta, f):
    c = 334
    u = np.array([np.sin(theta), np.cos(theta), 0]).T
    p = np.zeros((M, 3))
    a = np.zeros(M, dtype=complex)
    for m in range(1, M + 1):
        p[m - 1] = np.array([r * np.sin(2 * np.pi / M * (m - 1)), r * np.cos(2 * np.pi / M * (m - 1)), 0]).T
        a[m - 1] = np.exp(1j * 2 * np.pi * f / c * np.dot(u.T, p[m - 1]))
    return a

# 確認
d = 0.05
M = 3
theta = np.pi / 4
f = 1000
print(circular_array_manifold_vector(d, M, theta, f))

# 結果
# [0.7868537 +0.61713958j 0.97051349+0.2410468j  0.6148926 -0.78861086j]