# 空間相関行列の計算

import numpy as np


def spatial_correlation_matrix(*X):
    M = len(X)
    F = X[0].shape[0]
    T = X[0].shape[1]
    R = np.zeros((F, M, M), dtype=complex)
    for f in range(F):
        sum = np.zeros((M, M), dtype=complex)
        for t in range(T):
            # a.
            x_ft = np.zeros((M, 1), dtype=complex)
            for m in range(M):
                x_ft[m][0] = X[m][f][t]

            # b.
            sum = np.add(sum, x_ft @ np.conj(x_ft.T))
        R[f] = sum / T
    return tuple(R)


X_1 = np.array([[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]])
X_2 = np.array([[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]])
R_0, R_1, R_2 = spatial_correlation_matrix(X_1, X_2)
print(R_0)
print(R_1)
print(R_2)

# # [[1.  +0.j 1.25+0.j]
#  [1.25+0.j 5.25+0.j]]
# [[4.  +0.j 1.5 +0.j]
#  [1.5 +0.j 1.25+0.j]]
# [[9.  +0.j 0.75+0.j]
#  [0.75+0.j 0.75+0.j]]
