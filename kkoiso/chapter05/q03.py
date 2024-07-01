import numpy as np


def array_manifold_vector_general(array_add, theta, f, c=334):
    theta_rad = np.deg2rad(theta)
    u = np.array([np.sin(theta_rad), np.cos(theta_rad), 0])
    M = len(array_add)
    a = np.zeros(M, dtype=complex)
    for m in range(M):
        p_m = np.array([array_add[m][0], array_add[m][1], 0])
        a[m] = np.exp(1j * 2 * np.pi * f / c * np.dot(u, p_m))
    return a


d = 0.05
M = 3
theta = 45
f = 1000
linear_add = [((m - 1) * d, 0) for m in range(M)]

r = 0.05
circular_add = [
    (r * np.sin(2 * np.pi * m / M), r * np.cos(2 * np.pi * m / M)) for m in range(M)
]


a_linear_general = array_manifold_vector_general(linear_add, theta, f)
print(a_linear_general)

a_circular_general = array_manifold_vector_general(circular_add, theta, f)
print(a_circular_general)
