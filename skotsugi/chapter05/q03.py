import numpy as np


def array_manifold_vector(X: np.ndarray, theta: float, f: float):
    c = 334

    M, _ = X.shape
    a = np.zeros(M, dtype=complex)
    u = np.array([np.sin(theta), np.cos(theta), 0])

    for m in range(M):
        p = X[m]
        a[m] = np.exp(1j * 2 * np.pi * f / c * u @ p)

    return a


if __name__ == "__main__":
    theta = np.pi / 4
    r = 0.05
    f = 1000

    X = np.array([[-r, 0, 0], [0, 0, 0], [r, 0, 0]])
    print(array_manifold_vector(X, theta, f))
    # [0.7868537-0.61713958j 1.       +0.j         0.7868537+0.61713958j]

    M = 3
    Y = np.zeros((M, 3))
    for m in range(M):
        phi = 2 * np.pi * m / M
        s = r * np.sin(phi)
        t = r * np.cos(phi)
        Y[m] = [s, t, 0]

    print(array_manifold_vector(Y, theta, f))
    # [0.7868537 +0.61713958j 0.97051349+0.2410468j  0.6148926 -0.78861086j]
