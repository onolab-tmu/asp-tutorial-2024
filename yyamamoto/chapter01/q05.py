import numpy as np
import matplotlib.pyplot as plt

A = 1       # 振幅
f = 440     # 周波数 Hz
sec = 3     # 信号長 s
fs = 16000  # サンプリング周波数 Hz

t = np.arange(0, sec, 1/fs) # サンプリング点の配列

y1 = A * np.sin(2*np.pi*f*t) # 正弦波
y2 = 2 * (np.random.randn(fs*sec)) - 1 # ホワイトノイズ

# グラフの描画
fig = plt.figure()
plt.plot(t, y1, label='sin', zorder=2)
plt.plot(t, y2, label='white noise', zorder=1)
plt.legend()
fig.savefig('q05_graph')

