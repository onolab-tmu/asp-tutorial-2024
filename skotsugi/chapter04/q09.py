import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp
from q03 import stft
from q04 import hamming

sec = 1
fs = 16000
t = np.linspace(0, sec, fs+1) 
x = chirp(t, f0=100, f1=16000, t1=sec)

L = 50
S = 25
Xs = []
for i in range(1, 5):
  L = L * 2
  S = S * 2
  w = hamming(L)
  X = stft(L, S, w, x)
  Xs.append(X)

fig, ax = plt.subplots(4, 1, sharey=True, sharex=True)
for i, X in enumerate(Xs):
  A = np.abs(X)

  F = X.shape[0]
  T = X.shape[1]

  cb = ax[i].pcolormesh(A)

plt.tight_layout()

fig.colorbar(cb, ax=ax)

plt.savefig('skotsugi/chapter04/q09.png')