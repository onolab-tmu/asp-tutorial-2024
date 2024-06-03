import numpy as np

def freqz_w(w, a, b):
  N = len(a)
  M = len(b)

  exp_a = np.array([ np.exp(-1j * w * i) for i in range(N)])
  exp_b = np.array([ np.exp(-1j * w * i) for i in range(M)])

  return np.sum(exp_b * b) / (np.sum(exp_a[1:N] * a[1:N]) + 1)

def freqz(w, a, b):
  return [freqz_w(i, a, b) for i in w]
