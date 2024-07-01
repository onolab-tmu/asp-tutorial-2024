import numpy as np

def correlation_matrix(X):
    M, F, T = X.shape
    R = np.zeros((F, M, M), dtype=complex)
    for f in range(F):
        for t in range(T):
            x_ft = np.array([X[:, f, t]]).T
            R[f] += np.dot(x_ft, np.conjugate(x_ft.T))
    return R

X1 = np.array([[1, -1j, -1, 1j],
               [2, -2j, -2, 2j],
               [3, -3j, -3, 3j]])
X2 = np.array([[4, -2j, 1, 0],
               [2, -1j, 0, 0],
               [1, -1j, 1, 0]])
X = np.stack([X1, X2])

print(correlation_matrix(X))


# 結果の確認
# [[[ 4.+0.j  5.+0.j]
#   [ 5.+0.j 21.+0.j]]

#  [[16.+0.j  6.+0.j]
#   [ 6.+0.j  5.+0.j]]

#  [[36.+0.j  3.+0.j]
#   [ 3.+0.j  3.+0.j]]]