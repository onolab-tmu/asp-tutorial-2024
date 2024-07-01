import numpy as np
import matplotlib.pyplot as plt
from q03 import array_manifold_vector
from q07 import F


def beam_pattern(w: np.ndarray, p: np.ndarray, fs):
    F, M = w.shape

    theta = np.arange(360) * np.pi / 180.0
    freq = np.arange(F) * fs / 2 / (F - 1)

    Phi = np.zeros((F, 360), dtype=complex)

    for i, f in enumerate(freq):
        for j, th in enumerate(theta):
            a = np.array([array_manifold_vector(p, th, f)]).T
            w_f = np.array([w[i]]).T

            Phi[i, j] = (w_f.T @ a)[0, 0]

    A = 20 * np.log10(np.abs(Phi))
    return A


if __name__ == "__main__":
    d = 0.05
    fs = 16000
    M = 3
    c = 334

    # ステアリングベクトル
    w = np.zeros((F, M), dtype=complex)
    tau = (np.arange(M) - (M - 1) / 2) * d / c / fs
    for f in range(F):
        w[f, :] = np.exp(-1j * 2 * np.pi * f * tau) / M

    # 直線状アレイ
    p = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])

    A = beam_pattern(w, p, fs)
    plt.imshow(A)
    plt.savefig("./skotsugi/chapter05/q08.png")
