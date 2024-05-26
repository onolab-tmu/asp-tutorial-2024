# スペクトルの確認: 2.の結果の振幅スペクトルおよび位相スペクトル をプロットせよ．

import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N = len(x)
    dft_X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            dft_X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)
    return dft_X

delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])
X = dft(delta)    # 2. の結果

plt.subplot(2,1,1)
plt.stem(abs(X))

plt.subplot(2,1,2)
plt.stem(np.angle(X))
plt.show()