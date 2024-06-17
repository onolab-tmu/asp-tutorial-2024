import numpy as np

def to_quantity(X: np.ndarray, fs: int, S: int):
  F = X.shape[0] # 1フレームあたりの信号長
  T = X.shape[1] # フレーム数
  L = 2 * (F - 1)

  t = np.arange(T) * S / fs
  f = np.arange(F) * fs / L

  print(t)

  return t, f

if __name__ == "__main__":
  import matplotlib.pyplot as plt
  from q03 import stft
  from q04 import sin, hamming
  
  L = 1000
  S = 500
  sec = 0.1
  freq = 440
  fs = 16000
  x = sin(1, freq, fs, sec)
  w = hamming(L)

  X = stft(L, S, w, x)

  t, f = to_quantity(X, fs, S)

  A = 20 * np.log10(np.abs(X))
  ang = np.angle(X)

  fig, ax = plt.subplots(1, 2)

  cb = ax[0].pcolormesh(t, f, A)
  ax[0].set_ylabel('Frequency [Hz]')
  ax[0].set_xlabel('Time [sec]')

  cb = ax[1].pcolormesh(t, f, ang)
  ax[1].set_ylabel('Frequency [Hz]')
  ax[1].set_xlabel('Time [sec]')

  plt.tight_layout()

  fig.colorbar(cb, ax=ax)

  plt.grid()
  plt.savefig('skotsugi/chapter04/q10.png')
