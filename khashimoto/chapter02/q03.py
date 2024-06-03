# IDFT の確認: 2.の結果の IDFT を計算しプロットせよ.

import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N = len(x)
    dft_X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            dft_X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)
    return dft_X

def idft(X):
    N = len(X)
    idft_x = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            idft_x[n] += X[k] * np.exp(1j * 2 * np.pi * k * n / N)
        idft_x[n] /= N
    return idft_x



delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])
X = dft(delta)    # 2. の結果
idft_x = idft(X)
plt.stem(idft_x.real)
plt.show()


# ---------------- 確認 ----------------------
'''
x = np.arange(0, 2 * np.pi, 0.1)

fig = plt.figure()
plt.subplot(5,1,1)
y1 = np.sin(x)
plt.plot(y1)

plt.subplot(5,1,2)
Y = dft(y1)
plt.plot(Y.real)

plt.subplot(5,1,3)
plt.plot(Y.imag)

y2 = idft(Y)
plt.subplot(5,1,4)
plt.plot(y2.real)

plt.subplot(5,1,5)
plt.plot(y2.imag)

plt.show()
'''