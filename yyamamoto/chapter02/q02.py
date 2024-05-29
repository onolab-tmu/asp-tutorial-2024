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


# ここからq02
impulse = np.array([1, 0, 0, 0, 0, 0, 0, 0])
print(dft(impulse))