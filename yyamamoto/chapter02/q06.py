import numpy as np
import matplotlib.pyplot as plt

A = 1       # 振幅
f = 440     # 周波数 Hz
sec = 3     # 信号長 s
fs = 16000  # サンプリング周波数 Hz

t = np.arange(0, sec, 1/fs) # サンプリング点の配列
x = A * np.sin(2*np.pi*f*t) # 正弦波の値


# ここからq06
dft_value = np.fft.fft(x)
A = 20 * np.log10(np.abs(dft_value))
P = np.rad2deg(np.angle(dft_value))

freq = fs * np.arange(len(A)) / len(A)
# グラフの描画
fig = plt.figure()
fig.add_subplot(1,2,1)
plt.plot(freq, A)
plt.title('Amplitude spectrum')

fig.add_subplot(1,2,2)
plt.plot(freq, P)
plt.title('Phase Spectrum')
fig.savefig('q06_graph')


