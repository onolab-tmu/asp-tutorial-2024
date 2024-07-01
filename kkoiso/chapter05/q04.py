import numpy as np


def spatial_correlation_matrix(X):
    M, F, T = X.shape
    R = np.zeros((F, M, M), dtype=complex)
    for f in range(F):
        for t in range(T):
            x_ft = X[:, f, t]
            R[f] += np.power(t, T - 1) * x_ft * np.conj(x_ft).T
        R[f] /= T
    return R


X1 = np.array([[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]])
X2 = np.array([[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]])
X = np.stack((X1, X2), axis=0)


R = spatial_correlation_matrix(X)
print(R)
