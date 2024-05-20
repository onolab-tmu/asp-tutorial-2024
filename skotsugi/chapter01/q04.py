import numpy as np
import matplotlib.pyplot as plt

def make_white_noise(length):
  return np.random.normal(size=int(length))

if __name__ == "__main__":
  np.random.seed(0)
  
  fs = 16000 # サンプリング周波数[Hz]
  sec = 3.0

  y = make_white_noise(fs*sec)
  n = np.arange(0, 3.0, 1/fs)

  plt.plot(n, y)

  plt.xlim(0)
  plt.xlabel("time [sec]")
  plt.ylabel("Amplitude")

  plt.savefig("./skotsugi/chapter01/q4.png")
