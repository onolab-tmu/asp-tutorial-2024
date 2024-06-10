import numpy as np

def ws(S: int, w): 
  L = len(w)
  Q = L / S

  
  s = [np.sum([ w[l - m*S] ** 2 for m in range(-(Q-1), Q-1) ]) for l in L]

  return np.array(s)