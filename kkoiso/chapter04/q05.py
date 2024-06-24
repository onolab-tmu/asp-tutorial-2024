import numpy as np
import matplotlib.pyplot as plt


import numpy as np


def synthesis_window(w, S):
    L = len(w)
    Q = L // S
    w_s = np.zeros(L)

    for l in range(L):
        sum_w = 0
        for m in range(-(Q - 1), Q):
            idx = l - m * S
            if 0 <= idx < L:
                sum_w += w[idx] ** 2
        if sum_w > 0:
            w_s[l] = w[l] / sum_w
        else:
            w_s[l] = 0

    return w_s


w = np.ones(6)
print(synthesis_window(w, 2))
