from scipy.signal import istft, stft
import numpy as np
import matplotlib.pyplot as plt
from q03 import array_manifold_vector_general


def plot_beam_pattern(w_f, p, fs):
    fs_2 = fs / 2
    angles = np.linspace(0, 360, 361)
    F = w_f.shape[0]
    Psi = np.zeros((F, len(angles)), dtype=complex)
    for f in range(F):
        for i, theta in enumerate(angles):
            a_f_theta = array_manifold_vector_general(p, theta, f * (fs_2 / (F - 1)))
            Psi[f, i] = np.conj(w_f[f]).dot(a_f_theta)
    plt.figure(figsize=(10, 6))
    plt.imshow(20 * np.log10(np.abs(Psi)), aspect="auto", extent=[0, 360, 0, fs / 2])
    plt.colorbar(label="Amplitude [dB]")
    plt.xlabel("Angle [degrees]")
    plt.ylabel("Frequency [Hz]")
    plt.title("Beam Pattern")
    plt.show()


d = 0.05
M = 3
theta = 45
F = 1000
linear_coords = [((m - 1) * d, 0) for m in range(M)]
fs = 16000


w_f = np.zeros((F, M), dtype=complex)
for f in range(F):
    fs_2 = fs / 2
    tau = np.array([0, 10 / fs, 20 / fs])
    w_f[f] = 1 / 3 * np.exp(-1j * 2 * np.pi * f * tau * fs_2 / (F - 1))


plot_beam_pattern(w_f, linear_coords, fs)
