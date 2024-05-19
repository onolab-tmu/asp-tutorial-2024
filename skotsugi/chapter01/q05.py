import numpy as np
import matplotlib.pyplot as plt
from q02 import make_sin_wave
from q04 import make_white_noise

np.random.seed(0)

fs = 16000 # サンプリング周波数[Hz]
sec = 3.0

y = make_white_noise(fs*sec) + make_sin_wave(1.0, 440, fs, 3.0)

n = np.arange(0, 3.0, 1/fs)

plt.plot(n, y)

plt.xlim(0)
plt.xlabel("time [sec]")
plt.ylabel("Amplitude")

plt.savefig("./skotsugi/chapter01/q5.png")
