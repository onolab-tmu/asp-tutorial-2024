import numpy as np
from q01 import dft

delta = [1, 0, 0, 0, 0, 0, 0, 0]

d = dft(delta)
f = np.fft.fft(delta)

diff = d - f
print(diff)
