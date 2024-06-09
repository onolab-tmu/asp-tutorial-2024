# 合成窓

import numpy as np


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
w = np.ones(6)
print(window(2, w))


# [0.33333333 0.33333333 0.33333333 0.33333333 0.33333333 0.33333333]
"""
