# 窓関数の特性: 第 1 章 1.で作成した信号と同じ長さの Hamming 窓を作成し，DFT を計算せよ．

import numpy as np
import matplotlib.pyplot as plt

def hamming(N):
    w = np.zeros(N)
    for n in range(N):
        w[n] = 0.54-0.46 * np.cos(2 * np.pi * n / (N-1))
    return w

fs = 16000    # サンプリング周波数
T = 3    # 時間
w = hamming(fs*T)
w = np.fft.fft(w)
print(w)