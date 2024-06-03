# 窓関数の確認: 第 1 章 1.で作成した信号に対して 6.の窓関数を適用した信号をプロットせよ．

import numpy as np
import matplotlib.pyplot as plt

def hamming(N):
    w = np.zeros(N)
    for n in range(N):
        w[n] = 0.54-0.46 * np.cos(2 * np.pi * n / (N-1))
    return w


A = 1    # 振幅
f = 440    # 周波数
fs = 16000    # サンプリング周波数
T = 3
t = np.arange(fs * T) / fs
x = A * np.sin(2 * np.pi * f * t)    # 第１章１. で作成した信号

w = hamming(fs*T)
x2 = x * w

plt.plot(t, x2)
plt.show()