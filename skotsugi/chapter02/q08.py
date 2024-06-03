import numpy as np
import matplotlib.pyplot as plt
from q06 import sin
from q07 import hamming

# paramaters
fs = 16000
sec = 3.0
f = 440
N = fs * sec

n = np.arange(0, N) / fs
y = sin(1.0, f, fs, sec) * hamming(N)

# plt.xlim(0, 0.05)
plt.plot(n, y)
plt.savefig('./skotsugi/chapter02/q08.png')
