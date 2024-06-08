import numpy as np

def window(S, w):
    L = len(w)
    Q = L // S
    m = np.arange(-(Q-1), Q-1)  # ファンシーインデックス
    w_s = np.zeros(L)
    for l in range(L):
        den = 0
        for m in range(-(Q-1), Q-1):
            if 0 <= l - m * S & l - m * S < L:
                den += w[l-m*S] ** 2
        w_s[l] = w[l] / den
    return w_s

# 結果の確認
# w = np.arange(100)
# print(window(20, w))