import numpy as np
import soundfile as sf
from q02 import make_sin_wave
from q07 import add_noise_to_signal

np.random.seed(0)

fs = 16000
sec = 3.0

signal = make_sin_wave(1.0, 440, fs, sec)
noisy_signal, noise = add_noise_to_signal(signal, 6)

sf.write("./skotsugi/chapter01/q08.wav", noisy_signal, fs)
