import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft
from q03 import array_manifold_vector_general
from q04 import spatial_correlation_matrix


def compute_spatial_spectrum(z, p, fs):
    F, T, Z = stft(z, fs, window="hann", nperseg=1024, noverlap=512)
    angles = np.linspace(0, 360, 361)
    P = np.zeros((31, len(angles)))
    fs_2 = fs / 2
    for f_bin in range(20, 31):
        R_z = spatial_correlation_matrix(Z[:, f_bin, :])
        for i, theta in enumerate(angles):
            w_theta = array_manifold_vector_general(p, theta, f_bin * fs_2 / (F - 1))
            P[f_bin, i] = np.abs(np.conj(w_theta).dot(R_z).dot(w_theta))

    plt.figure(figsize=(10, 6))
    for f_bin in range(20, 31):
        plt.plot(angles, 20 * np.log10(P[f_bin, :]), label=f"Frequency bin {f_bin}")
    plt.xlabel("Angle [degrees]")
    plt.ylabel("20log10|P(θ)|")
    plt.title("Spatial Spectrum")
    plt.legend()
    plt.show()


# サンプル信号の生成
fs = 16000
T = 1
N = fs * T
t = np.linspace(0, T, N, endpoint=False)
f = 440
a = 1

s = a * np.sin(2 * np.pi * f * t)

np.random.seed(0)
noise = np.random.normal(0, 1, N)
SNR = 10
noise_amplitude = a / (10 ** (SNR / 20))
epsilon = noise_amplitude * noise

x1 = s + epsilon
x2 = np.roll(s, 10) + epsilon
x3 = np.roll(s, 20) + epsilon
x = np.array([x1, x2, x3])

# マイクロホン配置
d = 0.05
M = 3
linear_coords = [(m * d, 0) for m in range(M)]

# 空間スペクトルの計算
compute_spatial_spectrum(x, linear_coords, fs)
