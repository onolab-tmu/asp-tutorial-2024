import numpy as np

def circular_conv(x, h):
  N = len(x)
  z = np.zeros(N, dtype = 'complex_')

  for i in range(N):
    for k in range(N):
      z[i] += x[k] * h[(i - k) % N]

  return z
