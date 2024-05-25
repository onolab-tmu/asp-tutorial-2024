import numpy as np
import matplotlib.pyplot as plt
from q01 import dft, idft

delta = [1, 0, 0, 0, 0, 0, 0, 0]
d = dft(delta)
D = idft(d)

print(D)

fig, axs = plt.subplots(2)

plt.ylim(0, 1)

axs[0].stem(np.real(D))
axs[0].set_title('Real Part')
axs[1].stem(np.imag(D))
axs[1].set_title('Imaginary Part')

fig.tight_layout()

plt.savefig('./skotsugi/chapter02/q03.png')
