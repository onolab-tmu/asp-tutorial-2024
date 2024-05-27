import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

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

impulse = [1, 0, 0, 0, 0, 0, 0, 0]
dft_value = dft(impulse)

# ここからq03
idft_value = idft(dft_value)
t = np.arange(0, 8, 1)
fig = plt.figure()
plt.plot(idft_value)
fig.savefig('q03_graph')