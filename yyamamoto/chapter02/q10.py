import numpy as np
import matplotlib.pyplot as plt
import math
import tqdm

A = 1       # 振幅
f = 440     # 周波数 Hz
sec = 0.5     # 信号長 s
fs = 16000  # サンプリング周波数 Hz

t = np.arange(0, sec, 1/fs) # サンプリング点の配列
x = A * np.sin(2*np.pi*f*t) # 正弦波の値

X = np.fft.fft(x)

def conv(x, h):
    N = len(x)
    n = np.arange(N)
    z = np.zeros(N, dtype=complex)
    for k in tqdm.tqdm(range(N)):
        z[k] = np.sum(x[n] * h[k-n])
    return z


def Hamming(N):
    n = np.arange(N)
    w = np.zeros(N, dtype=complex)
    w = 0.54 - 0.46 * np.cos(2*np.pi*n/(N-1))
    return w

N = len(x)
y = np.zeros(N)
H = Hamming(N)
y = x * H

# ここまでq08の内容


N = 48000
H = Hamming(N)
Y = np.fft.fft(H)

Z = np.zeros(N)
Z = conv(X, Y) # np.convolve は巡回畳み込みをしないので使えませんでした...
z = np.fft.ifft(Z)
print(z)
print(y)



fig = plt.figure()
fig.add_subplot(1,2,1)
plt.plot(t, y)
plt.title('q08')
fig.add_subplot(1,2,2)
plt.plot(t, z)
plt.title('q10')
fig.savefig('q10_graph')

