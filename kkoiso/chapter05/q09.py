import numpy as np
import matplotlib.pyplot as plt
from q08 import plot_beam_pattern


M = 3
theta = 45
F = 1000
fs = 16000


for d in [0.02, 0.05, 0.10]:
    linear_coords = [((m - 1) * d, 0) for m in range(M)]
    w_f = np.zeros((F, M), dtype=complex)
    for f in range(F):
        tau = np.array([0, 10 / fs, 20 / fs])
        w_f[f] = 1 / 3 * np.exp(-1j * 2 * np.pi * f * tau * fs / 2 / F)
    plot_beam_pattern(w_f, linear_coords, fs)
