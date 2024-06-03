import numpy as np

def conv(X, Y):
  N = len(X) 
  Z = np.zeros(N, dtype = 'complex_')
  k = np.arange(N)

  for i in range(N):
    Z[k] += X[i] * Y[k - i]

  return Z


if __name__ == "__main__":
  import matplotlib.pyplot as plt
  from q06 import sin
  from q07 import hamming

  fs = 16000
  sec = 3
  N = int(fs * sec)

  x = sin(1, 440, fs, sec)
  X = np.fft.fft(x)

  y = hamming(N)
  Y = np.fft.fft(y)

  Z = conv(X, Y)
  z = np.fft.ifft(Z) / N

  print(z)

  n = np.arange(0, N) / fs
  #plt.xlim(0, 0.05)
  plt.plot(n, z.real)
  plt.savefig('./skotsugi/chapter02/q10.png')
