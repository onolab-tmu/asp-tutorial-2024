import numpy as np
from q01 import zero_padding

def divide_flame(L: int, S: int, x):
  # エラー処理
  if L < S:
    raise Exception('Shift size must be smaller than window size.')
  
  N = len(x)
  x_tilde = zero_padding(L, S, x)

  T = np.arange(int((N - 1) / S))
  return [ x_tilde[t*S:t*S+L] for t in T ]