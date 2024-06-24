import matplotlib.pyplot as plt
import numpy as np
from q03 import stft
from q04 import sin, hamming

def istft(S: int, X: np.ndarray):
  F, T = X.shape
  N = 2 * (F - 1)
  M = S * (T - 1) + N
  
  hat = np.zeros(M)
  
  z = np.array([ np.fft.irfft(X[0:F,t]) for t in range(T) ])

  if z.shape[1] != N:
    raise "len(z[n]) must be 2(F - 1)"
  
  ws = np.ones(N)

  for t in range(T):
    idx = t * S

    # Overlap add
    hat[idx:idx + N] = hat[idx:idx + N] + ws * z[t]

  return hat


L = 1000
S = 500
sec = 0.1
freq = 440
fs = 16000
x = sin(1, freq, fs, sec)
w = hamming(L)

X = stft(L, S, w, x)
x_istft = istft(S, X)

plt.plot(x_istft)
plt.grid()
plt.xlim(0)
plt.savefig('skotsugi/chapter04/q08.png')