import numpy as np
import matplotlib.pyplot as plt

fs = 16000  # サンプリング周波数 Hz
sec = 3       # 信号長 s

t = np.arange(0, sec, 1/fs) # サンプリング点の配列
y = 2 * (np.random.rand(fs*sec)) - 1

# グラフの描画
fig = plt.figure()
plt.plot(t,y)
fig.savefig('q04_graph')