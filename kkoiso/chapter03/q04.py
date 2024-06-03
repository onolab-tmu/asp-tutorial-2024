import numpy as np
import matplotlib.pyplot as plt
from q01 import linear_conv
from q02 import circular_conv
from q03 import zero_padded_circular_conv

x = [4, 3, 2, 1]
h = [1, 0, -1, 0]
x_padded = np.concatenate([x, np.zeros(4)])

z_linear = linear_conv(x, h)
z_circular = circular_conv(x, h)
z_zero_padded = zero_padded_circular_conv(x, h)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(z_linear)
plt.title("Linear Convolution")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(z_circular)
plt.title("Circular Convolution")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(z_zero_padded)
plt.title("Zero-padded Circular Convolution")
plt.grid(True)

plt.tight_layout()
plt.show()
