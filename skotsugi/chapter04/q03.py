import numpy as np
from q02 import divide_frame

def stft(L: int, S: int, w, x):
  # エラー処理
  if L < S:
    raise Exception('Shift size must be smaller than window size.')

  flames = divide_frame(L, S, x)

  ffted = np.fft.rfft(flames*w).T

  return ffted