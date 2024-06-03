import numpy as np
import matplotlib.pyplot as plt
from q07 import Hamming_Window
from q01 import DFT,IDFT
#正弦波を生成
a = 1.0
freq= 440 
samp_rate = 16000 
d = 3  

t = np.linspace(0, d, int(samp_rate * d), endpoint=False)


sin_wave = a * np.sin(2 * np.pi * freq * t)
#正弦波をDFT
sin_wave_DFT = np.fft.fft(sin_wave)


#正弦波と同じサイズのハミング窓を生成し、DFT
signal_length = len(sin_wave)
hamming_window_spectrum = np.fft.fft(Hamming_Window(signal_length))

#巡回畳み込み
Z=[0] * signal_length
for k in range(signal_length):
    s = 0
    for n in range(signal_length):
        s =s +sin_wave_DFT[n]*hamming_window_spectrum[k-n]
    Z[k] = s
z_idft = np.fft.ifft(Z)
print(z_idft)


#プロット
plt.figure(figsize=(10, 4))
plt.plot(z_idft)
plt.title('Signal with Hamming Window')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()