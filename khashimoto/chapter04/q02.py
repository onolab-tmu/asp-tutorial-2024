# フレーム分割

import numpy as np
from q01 import zeropad


def frame(L, S, x):
    x_pad = zeropad(L, S, x)
    T = (x_pad.size - L) // S + 1  # フレーム数
    x_t = np.zeros((T, L))
    for t in range(T):
        for l in range(L):
            x_t[t][l] = x_pad[t * S + l]
    return x_t


"""
# 確認
x = np.ones(5)
print(x)
print(zeropad(4, 2, x))
x_2 = frame(4, 2, x)
print(x_2)


# [1. 1. 1. 1. 1.]
# [[0. 1. 1. 1.]
# [1. 1. 1. 0.]]
"""
