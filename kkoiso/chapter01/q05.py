import numpy as np
import matplotlib.pyplot as plt
import wave
a = 1.0
freq= 440 
samp_rate = 16000 
d = 3  

t = np.linspace(0, d, int(samp_rate * d), endpoint=False)


sin_wave = a * np.sin(2 * np.pi * freq * t)

white_noise = np.random.normal(0, 1, len(t))
#1-5
mixed_signal = sin_wave + white_noise


plt.plot(t, mixed_signal)  
plt.title("Mixed Signal (Sin Wave + White Noise)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()