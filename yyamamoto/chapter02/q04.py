import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N = len(x)
    X = [0] * N
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * cmath.exp(-1j*2*math.pi*k*n/N)
    return X

def idft(X):
    N = len(X)
    x = [0] * N
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * cmath.exp(1j*2*math.pi*k*n/N) / N
    return x


# ここからq02
impulse = [1, 0, 0, 0, 0, 0, 0, 0]
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
