import numpy as np
import matplotlib.pyplot as plt
from q03 import array_manifold_vector

def show_beam_pattern(w, p, fs):
    # 手順a
    F = w.shape[0]
    M = p.shape[0]
    a = np.zeros((F, 361, M), dtype=complex)
    for f_idx in range(F):
        f = fs / 2 / (F - 1) * f_idx
        for theta_idx in range(361):
            theta = theta_idx / 180 * np.pi     # ラジアンに変換
            a[f_idx][theta_idx] = array_manifold_vector(p, M, theta, f)
    # 手順b
    psi = np.zeros((F, 361), dtype=complex)
    for f_idx in range(F):
        for theta_idx in range(361):
            psi[f_idx][theta_idx] = w[f_idx] @ a[f_idx][theta_idx].T
            
    psi_db = 20 * np.log10(np.abs(psi)).T
    thetas = np.arange(361)
    freqs = np.arange(F) * fs / 2 / (F - 1)
    fig = plt.figure()
    plt.pcolormesh(thetas, freqs, psi_db.T)
    plt.xlabel('angle[deg]')
    plt.ylabel('frequency[Hz]')
    fig.savefig('./yyamamoto/chapter05/q08_graph.png')

d = 0.05
M = 3
F = 1000
fs = 16000
p = np.zeros((M, 3))
w = np.zeros((F, 3), dtype=complex)
for m in range(1, M + 1):
    p[m - 1] = np.array([((m - 1) - (M - 1) / 2) * d, 0, 0]).T
tau = np.array([0, 10 / fs, 20 / fs])
for f in range(F):
    w[f] = np.exp(-1j * 2 * np.pi * f * tau) / 3

show_beam_pattern(w, p, fs)