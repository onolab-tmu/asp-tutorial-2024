import numpy as np
import matplotlib.pyplot as plt
import math

def Hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2*np.pi*n/(N-1))
    return w

# ここからq08
N = 48000
H = Hamming(N)
dft_value = np.fft.fft(H)

A = 20 * np.log10(np.abs(dft_value))
P = np.rad2deg(np.angle(dft_value))

fs = 16000
freq = fs * np.arange(len(A)) / len(A)

# グラフの描画
fig = plt.figure()
fig.add_subplot(1,2,1)
plt.plot(freq, A)
plt.title('Amplitude spectrum')
fig.add_subplot(1,2,2)
plt.plot(freq, P)
plt.title('Phase Spectrum')
fig.savefig('q09_graph')
