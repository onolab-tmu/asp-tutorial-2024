import numpy as np

def linear_conv(x, h):
  N = len(x)
  M = 2*N - 1
  z = np.zeros(M, dtype = 'complex_')

  for i in range(M):
    for k in range(N):
      j = i - k
      
      if j < 0 or j > N - 1:
        continue
      else:
        z[i] += x[k] * h[j]

  return z
