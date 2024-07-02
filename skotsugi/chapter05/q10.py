import numpy as np
from scipy.signal import stft
from q01 import linear_array_manifold_vector
from q04 import spatial_correlation_matrix


def spatial_spectrum(z: np.ndarray, f: float, fs: float):
    M, N = z.shape
    d = 0.05
    L = 1024
    S = 512

    fbin, _, Z = stft(z, fs, window="hann", nperseg=L, noverlap=L - S)
    R = spatial_correlation_matrix(Z)

    P = np.zeros(360, dtype=complex)

    for deg in range(360):
        theta = deg * np.pi / 180.0
        a = np.array([linear_array_manifold_vector(d, M, theta, fbin[f])])
        w = a.T / M

        P[deg] = (np.conj(w).T @ R[f] @ w).item()

    return P


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from q06 import x, fs

    degs = np.arange(360)

    for k in range(11):
        f = k + 20

        P = spatial_spectrum(x, f, fs)
        plt.plot(degs, 20 * np.log10(np.abs(P)))

    plt.savefig("./skotsugi/chapter05/q10.png")
