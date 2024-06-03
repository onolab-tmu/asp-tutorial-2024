import numpy as np
import matplotlib.pyplot as plt
from q07 import hamming

fs = 16000
sec = 3
N = fs * sec
wN = 2 ** 8

w = hamming(N)
W = np.fft.fft(w)

amp = 20 * np.log10(np.abs(W))
#amp = np.abs(W)
phs = np.angle(W)
phs[amp < 1e-5] = 0 

freq = np.fft.fftfreq(int(N), d=1/fs)

fig, axs = plt.subplots(1, 2)
axs[0].stem(freq, amp)
axs[0].set_title('Amplitude')
axs[1].stem(freq, phs)
axs[1].set_title('Phase')

fig.tight_layout()

plt.savefig('./skotsugi/chapter02/q09.png')
