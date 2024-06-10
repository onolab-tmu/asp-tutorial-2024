# 合成窓

import numpy as np
import matplotlib.pyplot as plt


def window(S, w):
    L = w.size
    Q = L // S  # 1.
    w_s = np.zeros(L)
    for l in range(L):
        sum = 0
        for m in range(-(Q - 1), Q):
            if 0 <= l - m * S < L:
                sum += w[l - m * S] ** 2  # 2.
        w_s[l] = w[l] / sum
    return w_s


"""
# 確認
L = 1024
w = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(L) / (L - 1))  # Hamming窓
plt.plot(window(256, w))
plt.show()


# [0.33333333 0.33333333 0.33333333 0.33333333 0.33333333 0.33333333]
"""
