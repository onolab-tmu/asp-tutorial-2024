import numpy as np
import matplotlib.pyplot as plt
from q01 import DFT,IDFT

x = np.array([1, 0, 0, 0, 0, 0, 0, 0])
X = DFT(x)
x_idft = IDFT(X)
print(x_idft)
idft_real = [val.real for val in x_idft]#実部を取りだす
idft_imag = [val.imag for val in x_idft]#虚部を取り出す

#実部をプロット
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.stem(idft_real)
plt.title('IDFT(Real Part)')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

#虚部をプロット
plt.subplot(2, 1, 2)
plt.stem(idft_imag)
plt.title('IDFT Result (Imaginary Part)')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()