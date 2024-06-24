import numpy as np

def synthesis_window(S: int, w: np.ndarray): 
  L = w.size
  Q = L // S
  
  s = np.array([
    np.sum([
      w[l - m*S]**2 
      for m in range(-(Q-1), Q) 
      if 0 <= l - m*S and L > l - m*S
    ]) for l in range(L) 
  ])

  return w / s


if __name__ == "__main__":
  import matplotlib.pyplot as plt
  
  N = 500
  hamming = np.hamming(N)
  ws = synthesis_window(N, hamming)
  plt.plot(ws)
  plt.savefig("./skotsugi/chapter04/q05.png")