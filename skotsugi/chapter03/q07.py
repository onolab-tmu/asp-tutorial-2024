import numpy as np

def diff_equation_n(i, a, b, x):
  N = len(a)
  M = len(b)

  if i < 0: 
    return 0

  y_sum = 0
  x_sum = 0
  for k in range(1, N):
    j = i - k
    y_sum += -a[k] * diff_equation_n(j, a, b, x)
    
  for k in range(M):
    j = i - k
    x_sum += (b[k] * x[j])
  return y_sum + x_sum

def diff_equation(a, b, x):
  L = len(x)
  return [diff_equation_n(i, a, b, x) for i in range(L)]


if __name__ == "__main__":
  import matplotlib.pyplot as plt

  N = 10
  x = np.zeros(N)
  x[0] = 1 # impulse

  a = [ 1, -0.3 ]
  b = [ 0.4 ]
  y = diff_equation(a, b, x)

  fig, ax = plt.subplots(2, 1, sharex=True)

  ax[0].grid()
  ax[1].grid()

  ax[0].stem(x)
  ax[1].stem(y)

  plt.savefig('./skotsugi/chapter03/q07.png')
