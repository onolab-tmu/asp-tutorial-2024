# SN 比: 信号長の等しい 2 個の信号 $s[n], x[n]; (n = 0, \dots, N-1), $ の信号対雑音比 (SN比) を計算する関数を実装せよ．

import numpy as np

def snr(s, x):
    r = 10 * np.log10(np.sum(s ** 2) / np.sum(x ** 2))
    return r
