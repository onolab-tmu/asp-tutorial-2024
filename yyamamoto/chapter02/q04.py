import matplotlib.pyplot as plt
import numpy as np

def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    n = np.arange(N)
    for k in range(N):
        X[k] = np.sum(x[n] * np.exp(-1j*2*np.pi*k*n/N))
    return X

def idft(X):
    N = len(X)
    x = np.zeros(N, dtype=complex)
    k = np.arange(N)
    for n in range(N):
       x[n] = np.sum(X[k] * np.exp(1j*2*np.pi*k*n/N)) / N
    return x


impulse = np.array([1, 0, 0, 0, 0, 0, 0, 0])
dft_value = dft(impulse)

A = 20 * np.log10(np.abs(dft_value))
P = np.rad2deg(np.angle(dft_value))

fig = plt.figure()
fig.add_subplot(1, 2, 1)
plt.plot(A)
plt.title("Amplitude Spectrum")
fig.add_subplot(1, 2, 2)
plt.plot(P)
plt.title("Phase Spectrum")
fig.savefig('q04_graph')
