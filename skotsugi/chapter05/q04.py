import numpy as np


def spatial_correlation_matrix(X_m: np.ndarray):
    M, F, T = X_m.shape
    R = np.zeros((F, M, M), dtype=complex)

    for f in range(F):
        sum_x = np.zeros((M, M), dtype=complex)
        for t in range(T):
            x_ft = np.array([X_m[:, f, t]]).T
            sum_x += x_ft @ np.conjugate(x_ft.T)

        R[f] = sum_x / T

    return np.array(R)


if __name__ == "__main__":
    X = np.array(
        [
            [[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]],
            [[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]],
        ]
    )

    print(spatial_correlation_matrix(X))
    # [[[1.  +0.j 1.25+0.j]
    #  [1.25+0.j 5.25+0.j]]

    #  [[4.  +0.j 1.5 +0.j]
    #  [1.5 +0.j 1.25+0.j]]

    #  [[9.  +0.j 0.75+0.j]
    #  [0.75+0.j 0.75+0.j]]]
