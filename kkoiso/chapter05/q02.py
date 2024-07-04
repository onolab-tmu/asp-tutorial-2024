import numpy as np


def array_manifold_vector_circular(r, M, theta, f, c=334):
    theta_rad = np.deg2rad(theta)
    u = np.array([np.sin(theta_rad), np.cos(theta_rad), 0])
    a = np.zeros(M, dtype=complex)
    for m in range(M):
        p_m = np.array(
            [r * np.sin(2 * np.pi * m / M), r * np.cos(2 * np.pi * m / M), 0]
        )
        a[m] = np.exp(1j * 2 * np.pi * f / c * np.dot(u, p_m))
    return a


r = 0.05
M = 3
theta = 45
f = 1000


a_circular = array_manifold_vector_circular(r, M, theta, f)
print(a_circular)
