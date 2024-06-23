import numpy as np

def correlation_matrix(X):
    M, F, T = X.shape
    x = np.zeros((F, T, M), dtype=complex)
    for f in range(F):
        for t in range(T):
            x[f, t] = X[:, f, t].T
    R = np.zeros((F, M, M), dtype=complex)
    t = np.arange(T)    # ファンシーインデックス
    for f in range(F):
        R[f] = 1 / T * np.sum(np.dot(x[f][t], np.conjugate(x[f][t].T)))
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
# [[[7.25+0.j 7.25+0.j]
#   [7.25+0.j 7.25+0.j]]

#  [[1.25+0.j 1.25+0.j]
#   [1.25+0.j 1.25+0.j]]

#  [[1.25+0.j 1.25+0.j]
#   [1.25+0.j 1.25+0.j]]]