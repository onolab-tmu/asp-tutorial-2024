# 簡単な多チャネル観測シミュレーション

import numpy as np
import matplotlib.pyplot as plt


fs = 16000
sec = 1
A = 1
f = 440

t = np.arange(fs * sec) / fs
s = A * np.sin(2 * np.pi * f * t)  # 正弦波

snr = 10
noise = np.random.randn(fs * sec)
noise /= np.sqrt(np.sum(noise**2))
noise *= np.sqrt(np.sum(s**2))
a = 10 ** (-snr / 20)
noise = a * noise  # ホワイトノイズ

x1 = np.zeros(fs * sec)
x2 = np.zeros(fs * sec)
x3 = np.zeros(fs * sec)
for n in range(fs * sec):
    x1[n] = s[n] + noise[n]
    x2[n] = s[n - 10] + noise[n]
    x3[n] = s[n - 20] + noise[n]


plt.plot(t, x1)
plt.plot(t, x2)
plt.plot(t, x3)
plt.xlim(0, 0.01)
plt.show()
