import numpy as np

def sin(A, f, fs, sec):
  n = np.arange(0, fs*sec) / fs
  return A * np.sin(2 * np.pi * f * n)

def hamming(N: int): 
  n = np.arange(N)
  return 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))

if __name__ == "__main__":
  import matplotlib.pyplot as plt
  from q03 import stft
  
  L = 1000
  S = 500
  sec = 0.1
  freq = 440
  fs = 16000
  x = sin(1, freq, fs, sec)
  w = hamming(L)

  X = stft(L, S, w, x)
  F = X.shape[0]
  T = X.shape[1]

  t = (np.arange(T) + 0.5) * sec / T
  f = np.arange(F) / F * fs / 2

  A = 20*np.log10(np.abs(X))
  ang = np.angle(X)

  fig, ax = plt.subplots(1, 2)

  cb = ax[0].pcolormesh(t, f, A)
  ax[0].set_ylabel('Frequency [Hz]')
  ax[0].set_xlabel('Time [sec]')

  cb = ax[1].pcolormesh(t, f, ang)
  ax[1].set_ylabel('Frequency [Hz]')
  ax[1].set_xlabel('Time [sec]')

  fig.colorbar(cb, orientation="vertical", ax=ax)

  plt.grid()
  plt.tight_layout()
  plt.savefig('skotsugi/chapter04/q04.png')
