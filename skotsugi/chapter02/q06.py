import numpy as np

def sin(A: float, f: float, fs: float, sec: float):
  n = np.arange(0, fs*sec) / fs
  return A * np.sin(2 * np.pi * f * n)

if __name__ == "__main__":
  import matplotlib.pyplot as plt

  fs = 16000
  sec = 3.0
  N = int(fs*sec)
  
  y = sin(1.0, 440, fs, sec)

  Y = np.fft.fft(y)
  freq = np.fft.fftfreq(N, d=1/fs)

  amp = np.abs(Y)
  phs = np.angle(Y)
  phs[amp < 1e-5] = 0 # これをしないと，絶対値がすごく小さな値の偏角も計算されてしまい，でたらめな位相スペクトルが出てしまう
  
  fig, axs = plt.subplots(1, 2)

  axs[0].stem(freq, amp)
  axs[0].set_xlim([0, max(freq)])
  axs[0].set_title('Amplitude')
  axs[1].stem(freq, phs)
  axs[1].set_xlim([0, max(freq)])
  axs[1].set_title('Phase')

  fig.tight_layout()
  plt.savefig('./skotsugi/chapter02/q06.png')
