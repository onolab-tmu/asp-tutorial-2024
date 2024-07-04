import numpy as np


def linear_array_manifold_vector(d: float, M: int, theta: float, f: float):
    c = 334
    a = np.zeros(M, dtype=complex)
    u = np.array([np.sin(theta), np.cos(theta), 0])

    for m in range(M):
        p = np.array([(m - (M - 1) / 2) * d, 0, 0])
        a[m] = np.exp(1j * 2 * np.pi * f / c * (u @ p))

    return a


if __name__ == "__main__":
    d = 0.05
    M = 3
    theta = np.pi / 4
    f = 1000
    print(linear_array_manifold_vector(d, M, theta, f))
    # [(0.7868536952034816-0.617139580925277j), (1+0j), (0.7868536952034816+0.617139580925277j)]
