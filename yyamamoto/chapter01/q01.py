import numpy as np
import matplotlib.pyplot as plt

A = 1       # 振幅
f = 440     # 周波数 Hz
sec = 3     # 信号長 s
fs = 16000  # サンプリング周波数 Hz

t = np.arange(0, sec, 1/fs) # サンプリング点の配列

y = A * np.sin(2*np.pi*f*t) # 正弦波の値

# グラフの描画
fig = plt.figure()
plt.plot(t,y)
fig.savefig('q01_graph')