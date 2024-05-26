#  正弦波のスペクトル: 第 1 章 1.で作成した信号の DFT を計算し，振幅スペクトルと位相スペクトルをプロットせよ．（プロットする際はデシベル表記にするために 20 * log10(np.abs(X)) などのようにしてデシベル表記になおしてから計算すると見やすいです．）

import numpy as np
import matplotlib.pyplot as plt

A = 1    # 振幅
f = 440    # 周波数
fs = 16000    # サンプリング周波数
T = 3
t = np.arange(fs * T) / fs
x = A * np.sin(2 * np.pi * f * t)    # 第１章１. で作成した信号

X = np.fft.fft(x)


# 振幅スペクトルと位相スペクトルをプロット
plt.subplot(2,1,1)
plt.plot(20 * np.log10(abs(X)))
#plt.stem(abs(X))

plt.subplot(2,1,2)
plt.plot(np.angle(X))
plt.show()