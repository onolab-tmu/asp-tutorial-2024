import numpy as np
import matplotlib.pyplot as plt
from q01 import DFT

x = np.array([1, 0, 0, 0, 0, 0, 0, 0])
X = DFT(x)
title = "DFT impulse"

plt.figure(figsize=(10, 4))

#振幅スペクトルのプロット
plt.subplot(2, 1, 1)
plt.plot(np.abs(X))
plt.title(title + ' Amplitude Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.grid(True)
    
#位相スペクトルのプロット
plt.subplot(2, 1, 2)
plt.plot(np.angle(X))
plt.title(title + ' Phase Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Phase')
plt.grid(True)
    
plt.tight_layout()
plt.show()