import numpy as np
import matplotlib.pyplot as plt

A = 1.0    # 振幅
f0 = 440   # 周波数[Hz]
sec = 3.0  # 信号の長さ[s]
fs = 16000 # サンプリング周波数[Hz]
PI = np.pi # 円周率

n = np.arange(0, fs*sec) / fs  # 間隔（公差）を指定（start: 0, stop: sec, step: 1/sf）
y = A * np.sin(2 * PI * f0 * n)

plt.plot(n, y)

plt.xlim(0, 1 / f0)
plt.xlabel("time [sec]")
plt.ylabel("Amplitude")

plt.savefig("./skotsugi/chapter01/q1.png")
