# 窓関数: 次式で定義される 点の Hamming 窓を作成する関数を実装せよ.

import numpy as np

def hamming(N):
    w = np.zeros(N)
    for n in range(N):
        w[n] = 0.54-0.46 * np.cos(2 * np.pi * n / (N-1))
    return w


# ------------- 確認 ----------------
w = hamming(5)
print(w)