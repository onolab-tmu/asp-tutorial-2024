# 正弦波の生成: 振幅 1, 周波数 440 Hz の正弦波をサンプリング周波数 16000 Hz で 3 秒分作成しプロットせよ．

import numpy as np
from matplotlib import pyplot

A = 1    # 振幅
f = 440    # 周波数
fs = 16000    # サンプリング周波数
t = np.linspace(0, 3, 3 * fs)    # 3秒分作成
x = A * np.sin(2 * np.pi * f * t)    # 変位

# プロット
pyplot.plot(t, x)
pyplot.savefig('q01.jpg')