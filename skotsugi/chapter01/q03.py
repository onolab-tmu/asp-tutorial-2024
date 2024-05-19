import numpy as np
import soundfile as sf
from q02 import make_sin_wave

fs = 16000 # サンプリング周波数[Hz]
sec = 3.0

y = np.zeros((int(fs*sec), 2), dtype=float)  
y[:,0] = make_sin_wave(1.0, 440, fs, sec)
y[:,1] = make_sin_wave(1.0, 660, fs, sec)

sf.write("./skotsugi/chapter01/q03.wav", y, fs)
