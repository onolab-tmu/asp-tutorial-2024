# 各種畳み込みの関係

import numpy as np
from q01 import LinearConv
from q02 import CircularConv
from q03 import ZeroPaddingCircularConv

x = np.array([4, 3, 2, 1])
h = np.array([1, 0, -1, 0])
print("線形畳み込み:")
print(LinearConv(x, h))
print("巡回畳み込み:")
print(CircularConv(x, h))
print("零詰めを行った巡回畳み込み:")
print(ZeroPaddingCircularConv(x, h))
