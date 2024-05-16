# 信号の混合: 1.で作成した正弦波と 4.で作成したホワイトノイズと正弦波を混合してプロットせよ．

import numpy as np
from matplotlib import pyplot

A = 1    # 振幅
f = 440    # 周波数
fs = 16000    # サンプリング周波数
t = np.linspace(0, 3, 3 * fs)    # 3秒分作成

x = A * np.sin(2 * np.pi * f * t)    # 1.で作成した正弦波
wn = 2 * np.random.rand(3 * fs) - 1    # 4.で作成したホワイトノイズ
mix = x + wn    # 混合音

# プロット
pyplot.plot(t, mix)
pyplot.savefig('q05.jpg')