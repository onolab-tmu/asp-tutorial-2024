import numpy as np
from q05 import synthesis_window

def istft(S: int, w: np.ndarray, X: np.ndarray):
  F, T = X.shape
  N = 2 * (F - 1)
  M = S * (T - 1) + N
  
  hat = np.zeros(M)
  
  z = np.array([ np.fft.irfft(X[:,t]) for t in range(T) ])

  if z.shape[1] != N:
    raise "len(z[n]) must be 2(F - 1)"
  
  ws = synthesis_window(S, w)

  for t in range(T):
    idx = t * S

    # Overlap add
    hat[idx:idx + N] += ws * z[t]

  return hat