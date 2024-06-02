# 巡回畳み込み

import numpy as np


def CircularConv(x, h):
    N = x.size
    z = np.zeros(N)
    for k in range(N):
        z += x[k] * h[(np.arange(N) - k) % N]
    return z
