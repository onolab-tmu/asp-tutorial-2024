import numpy as np

def hamming(N: int): 
  return [ 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1)) for n in range(int(N)) ]

if __name__ == "__main__":
  import matplotlib.pyplot as plt
  
  w = hamming(16000 * 3.0)
  
  plt.plot(w)
  plt.savefig('./skotsugi/chapter02/q07.png')
