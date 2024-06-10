import numpy as np
from q01 import zero_padding

def divide_frame(L: int, S: int, x):
  # エラー処理
  if L < S:
    raise Exception('Shift size must be smaller than window size.')
  
  x_tilde = zero_padding(L, S, x)
  N = len(x_tilde)

  T = np.arange((N - L) // S + 1)
  return np.array([ x_tilde[t*S:t*S+L] for t in T ])

if __name__ == "__main__":
  x = np.ones(5)
  print(x)
  print(zero_padding(4, 3, x))
  print(divide_frame(4, 3, x))