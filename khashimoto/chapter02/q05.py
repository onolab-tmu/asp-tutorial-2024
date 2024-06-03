# 既存の実装との比較: 8 点の単位インパルス信号の DFT を numpy.fft.fft 関数を用いて計算し，2.の結果と比較せよ．なお，これ以降 DFT を計算する場合は numpy.fft.fft 関数を使用してよい.

import numpy as np

delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])
X = np.fft.fft(delta)
print(X)
# 2. と同じ結果となった