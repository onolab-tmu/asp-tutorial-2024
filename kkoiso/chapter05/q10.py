import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft
from q04 import spatial_correlation_matrix


def compute_spatial_spectrum(z, p, fs):
    F, T, Z = stft(z, fs, window="hann", nperseg=1024, noverlap=512)
    angles = np.linspace(0, 360, 361)
    P = np.zeros((31, len(angles)))
    R_z = spatial_correlation_matrix(Z)
    tau = np.array([0, 10 / fs, 20 / fs])

    for i, theta in enumerate(angles):
        w = 1 / 3 * np.exp(-1j * 2 * np.pi * np.cos(np.deg2rad(theta)) * tau[:, None])
        for f_bin in range(20, 31):
            P[f_bin, i] = np.abs(np.conj(w.T).dot(R_z[f_bin]).dot(w))

    plt.figure(figsize=(10, 6))
    for f_bin in range(20, 31):
        plt.plot(angles, 20 * np.log10(P[f_bin, :]), label=f"Frequency bin {f_bin}")
    plt.xlabel("Angle [degrees]")
    plt.ylabel("20log10|P(θ)|")
    plt.title("Spatial Spectrum")
    plt.legend()
    plt.show()


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


d = 0.05
M = 3
linear_coords = [(m * d, 0) for m in range(M)]

compute_spatial_spectrum(x, linear_coords, fs)
