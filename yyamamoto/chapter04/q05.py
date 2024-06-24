import numpy as np
import matplotlib.pyplot as plt

def Hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2*np.pi*n/(N-1))
    return w

def window(S, w):
    L = len(w)
    Q = L // S
    w_s = np.zeros(L)
    for l in range(L):
        den = 0
        for m in range(-(Q-1), Q):
            if 0 <= l - m * S & l - m * S < L:
                den += w[l-m*S] ** 2
        w_s[l] = w[l] / den
    return w_s

# 結果の確認
# w = Hamming()
# fig = plt.figure()
# plt.plot(window(500, w))
# fig.savefig("./yyamamoto/chapter04/q05_graph.png")