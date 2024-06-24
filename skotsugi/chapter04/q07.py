import matplotlib.pyplot as plt
from q03 import stft
from q04 import sin, hamming
from q06 import istft

L = 1000
S = 500
sec = 0.1
freq = 440
fs = 16000
x = sin(1, freq, fs, sec)
w = hamming(L)

X = stft(L, S, w, x)
x_istft = istft(S, w, X)

plt.plot(x_istft)
plt.grid()
plt.xlim(0)
plt.savefig('skotsugi/chapter04/q07.png')