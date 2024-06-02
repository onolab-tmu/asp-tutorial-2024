# 零詰め+巡回畳み込み

import numpy as np


def ZeroPaddingCircularConv(x, h):
    N1 = x.size
    x = np.hstack((x, np.zeros(N1 - 1)))
    h = np.hstack((h, np.zeros(N1 - 1)))
    N = 2 * N1 - 1
    z = np.zeros(N)
    for k in range(N):
        z += x[k] * h[(np.arange(N) - k) % N]
    return z
