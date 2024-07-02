import numpy as np


def circular_array_manifold_vector(r: float, M: int, theta: float, f: float):
    c = 334
    a = np.zeros(M, dtype=complex)
    u = np.array([np.sin(theta), np.cos(theta), 0])

    for m in range(M):
        phi = 2 * np.pi * m / M
        p = np.array([r * np.sin(phi), r * np.cos(phi), 0])
        a[m] = np.exp(1j * 2 * np.pi * f / c * (u @ p))

    return a


if __name__ == "__main__":
    r = 0.05
    M = 3
    theta = np.pi / 4
    f = 1000
    print(circular_array_manifold_vector(r, M, theta, f))
    # [0.7868537 +0.61713958j 0.97051349+0.2410468j  0.6148926 -0.78861086j]
