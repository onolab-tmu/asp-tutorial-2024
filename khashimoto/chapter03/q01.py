# 線形畳み込み

import numpy as np


def LinearConv(x, h):
    N = x.size
    z = np.zeros(2 * N - 1)
    for n in range(2 * N - 1):
        for k in range(N):
            if (n - k) < 0 or (n - k) > (N - 1):
                z[n] += 0
            else:
                z[n] += x[k] * h[n - k]
    return z
