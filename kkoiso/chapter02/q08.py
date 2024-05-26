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
#ハミング窓を生成し、正弦波にかける
signal_length = len(sin_wave)
hamming_window_signal = sin_wave * Hamming_Window(signal_length)

#プロット
plt.figure(figsize=(10, 4))
plt.plot(hamming_window_signal)
plt.title('Signal with Hamming Window')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()