import numpy as np
import matplotlib.pyplot as plt


def synthesis_window(w, S):
    L = len(w)
    Q = L // S
    w_s = np.zeros(L)

    for l in range(L):
        sum_w = sum((w[(l - m * S)] ** 2 for m in range(-(Q - 1), Q)))
        w_s[l] = w[l] / sum_w

    return w_s
