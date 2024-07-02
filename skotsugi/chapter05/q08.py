import numpy as np
import matplotlib.pyplot as plt
from q03 import array_manifold_vector
from q07 import F


def beam_pattern(w: np.ndarray, p: np.ndarray, fs):
    F, M = w.shape

    angle = np.arange(360)
    theta = angle * np.pi / 180.0
    freq = np.arange(F) * fs / 2 / (F - 1)

    Phi = np.zeros((F, 360), dtype=complex)

    for i, f in enumerate(freq):
        for j, th in enumerate(theta):
            a = array_manifold_vector(p, th, f)
            w_f = w[i]

            Phi[i, j] = w_f.T @ a

    A = 20 * np.log10(np.abs(Phi))
    return angle, freq, A


if __name__ == "__main__":
    d = 0.05
    fs = 16000
    M = 3
    c = 334

    # 直線状アレイ
    p = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])

    # ステアリングベクトル
    w = np.zeros((F, M), dtype=complex)
    for f in range(F):
        a_w = array_manifold_vector(p, 0, f)
        w[f, :] = np.conj(a_w) / M

    plt.pcolormesh(*beam_pattern(w, p, fs))
    plt.savefig("./skotsugi/chapter05/q08.png")
