import numpy as np
import matplotlib.pyplot as plt
import math

def Hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2*np.pi*n/(N-1))
    return w

A = 1       # 振幅
f = 440     # 周波数 Hz
sec = 3     # 信号長 s
fs = 16000  # サンプリング周波数 Hz

t = np.arange(0, sec, 1/fs) # サンプリング点の配列
x = A * np.sin(2*np.pi*f*t) # 正弦波の値

# ここからq08
N = len(x)
y = np.zeros(N)
H = Hamming(N)
y = x * H

fig = plt.figure()
plt.plot(t, y)
fig.savefig('q08_graph')

