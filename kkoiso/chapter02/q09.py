import numpy as np
import matplotlib.pyplot as plt
from q07 import Hamming_Window
#正弦波を生成
a = 1.0
freq= 440 
samp_rate = 16000 
d = 3  

t = np.linspace(0, d, int(samp_rate * d), endpoint=False)


sin_wave = a * np.sin(2 * np.pi * freq * t)

signal_length = len(sin_wave)
#正弦波と同じサイズのハミング窓を生成し、DFT
hamming_window_spectrum = np.fft.fft(Hamming_Window(signal_length))

print(hamming_window_spectrum)