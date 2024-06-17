import numpy as np

def synthesis_window(S: int, w: np.ndarray): 
  L = w.size
  Q = L // S
  
  s = np.array([
    np.sum([
      w[l - m*S]**2 for m in range(-(Q-1), Q-1) if 0 < l - m*S and L > l - m*S
    ]) for l in range(L) 
  ])

  return w / s