# 周波数応答の確認（再帰なし）

import numpy as np
import matplotlib.pyplot as plt
from q08 import FreqRes

fs = 16000
N = 10
f = np.arange(0, fs, 1 / N)

a = np.array([0])
b = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
H = np.zeros(f.size, dtype=complex)
for i in range(f.size):
    H[i] = FreqRes(a, b, fs, f[i])

plt.subplot(2, 1, 1)
plt.plot(abs(H))

plt.subplot(2, 1, 2)
plt.plot(np.angle(H))
plt.show()
