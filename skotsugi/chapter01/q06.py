import math
import numpy as np
from q02 import make_sin_wave
from q04 import make_white_noise

def square_mean(x):
  # return np.sum(x ** 2) # <- これだとうまくいかなかった
  return np.mean(x ** 2)

def sn_rate(s, x): 
  if (len(s) != len(x)):
    return
  
  s_sum = square_mean(s)
  x_sum = square_mean(x)

  return 10 * math.log10(s_sum / x_sum)

##### DEBUG #####
if __name__ == "__main__":
  np.random.seed(0)

  fs = 16000
  sec = 3.0

  s = make_sin_wave(1.0, 440, fs, 3.0)
  x = make_white_noise(fs*sec)

  print(sn_rate(s, x))
