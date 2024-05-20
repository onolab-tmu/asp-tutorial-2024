import numpy as np
import soundfile as sf

def make_sin_wave(A, f, fs, sec):
  n = np.arange(0, fs*sec) / fs
  return A * np.sin(2 * np.pi * f * n)

if __name__ == "__main__":
  fs = 16000 # サンプリング周波数[Hz]

  y = make_sin_wave(1.0, 440, fs, 3.0)

  sf.write("./skotsugi/chapter01/q02.wav", y, fs)
