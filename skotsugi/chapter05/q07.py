import numpy as np
from scipy.signal import stft, istft
from q06 import x, fs


L = 1024
S = 512
fbin, tbin, X = stft(x, fs, window="hann", nperseg=L, noverlap=L - S)

N, F, T = X.shape

Y = np.zeros((F, T), dtype=complex)
tau = np.array([0, 10, 20]) / fs

for i in range(F):
    f = i * fs / 2 / (F - 1)
    w = np.exp(-1j * 2 * np.pi * f * tau) / 3

    for t in range(T):
        Y[i, t] = np.conjugate(w) @ X[:, i, t]

t, y = istft(Y, fs, window="hann", nperseg=L, noverlap=L - S)


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plt.plot(t, y)

    plt.xlim([0, 0.01])
    plt.savefig("./skotsugi/chapter05/q07.png")
