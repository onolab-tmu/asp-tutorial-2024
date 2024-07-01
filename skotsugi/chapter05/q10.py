import numpy as np
from scipy.signal import stft
from q01 import linear_array_manifold_vector
from q04 import spatial_correlation_matrix
from q06 import x, fs


def spatial_spectrum(z: np.ndarray, f: float, fs: float):
    M, N = z.shape
    d = 0.05
    L = 1024
    S = 512

    _, __, Z = stft(z, fs, window="hann", nperseg=L, noverlap=L - S)
    R = spatial_correlation_matrix(Z)

    P = np.zeros(360, dtype=complex)

    for deg in range(360):
        theta = deg * np.pi / 180.0
        a = linear_array_manifold_vector(d, M, theta, f)
        w = np.array([a]).T / M

        P[deg] = np.conjugate(w.T) @ R[f] @ w

    return P


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    degs = np.arange(360)

    fig, ax = plt.subplots(2, 6, sharey=True)
    for k in range(11):
        i = k // 6
        j = k % 6
        f = k + 20

        P = spatial_spectrum(x, f, fs)
        ax[i][j].plot(degs, 20 * np.log10(np.abs(P)))

    plt.tight_layout()
    plt.savefig("./skotsugi/chapter05/q10.png")
