# 零詰め

import numpy as np


def zeropad(L, S, x):
    zero1 = np.zeros(L - S)
    x_pad = np.concatenate([zero1, x, zero1])  # 1.
    zero2 = x_pad.size % S
    if zero2 != 0:
        x_pad = np.concatenate([x_pad, np.zeros(S - zero2)])  # 2.
    return x_pad


"""
# 確認
x = np.ones(5)
print(x)
x_pad = zeropad(4, 3, x)
print(x_pad)


# [1. 1. 1. 1. 1.]
# [0. 1. 1. 1. 1. 1. 0. 0. 0.]
"""
