# 簡単なフィルタ処理: 9.の信号に対して 5 点移動平均フィルタを適用した結果と元の信号をプロットせよ．

import soundfile as sf
import numpy as np
from matplotlib import pyplot

data, fs = sf.read("q09.wav")    # 読み込み
result = np.convolve(data, np.ones(5), "valid") / 5    # ５点移動平均フィルタを適用

t1 = np.linspace(0, np.size(data) / fs, np.size(data))    # 時間軸
t2 = t1
for i in range(2):
    t2 = np.delete(t2, 0)
    t2 = np.delete(t2, np.size(t2) - 1)

# プロット
pyplot.plot(t1, data)
pyplot.plot(t2, result)
pyplot.savefig('q10.jpg')