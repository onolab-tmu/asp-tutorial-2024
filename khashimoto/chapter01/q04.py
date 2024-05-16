# 白色雑音の生成: ホワイトノイズをサンプリング周波数 16000 Hz で 3 秒分作成しプロットせよ．

import numpy as np
from matplotlib import pyplot

fs = 16000    # サンプリング周波数
t = np.linspace(0, 3, 3 * fs)    # 3秒分作成
x = 2 * np.random.rand(3 * fs) - 1

# プロット
pyplot.plot(t, x)
pyplot.savefig('q04.jpg')