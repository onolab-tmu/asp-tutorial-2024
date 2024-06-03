import numpy as np

def circular_zero_conv(x, h):
  N = len(x)
  M = N * 2
  
  x_zero = np.zeros(M, dtype = 'complex_')
  x_zero[:N] = x

  h_zero = np.zeros(M, dtype = 'complex_')
  h_zero[:N] = h

  z = np.zeros(M, dtype = 'complex_')

  for i in range(M):
    for k in range(M):
      j = (i - k) % M
      z[i] += x_zero[k] * h_zero[j]

  return z
