import numpy as np
import matplotlib.pyplot as plt
from q01 import DFT,IDFT

x = np.array([1, 0, 0, 0, 0, 0, 0, 0])
X = DFT(x)


np_X = np.fft.fft(x)
print("Custom DFT:", X)
print("Np FFT:", np_X)