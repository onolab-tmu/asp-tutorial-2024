import numpy as np

def dft(x):
  N = len(x)
  X = np.zeros(N, dtype = 'complex_')

  for k in range(N):
    for n in range(N):
      X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)
  
  return X

def idft(X): 
  N = len(X)
  x = np.zeros(N, dtype = 'complex_')

  for n in range(N):
    for k in range(N):
      x[k] += X[k] * np.exp(1j * 2 * np.pi * k * n / N) / N
  
  return x

if __name__ == "__main__":
  d = dft([1, 0, 0, 0])
  D = idft(d)
  print(d, D)