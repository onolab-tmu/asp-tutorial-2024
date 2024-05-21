import numpy as np
import matplotlib.pyplot as plt

#1-1
a = 1.0
freq= 440 
samp_rate = 16000 
d = 3  

t = np.linspace(0, d, int(samp_rate * d), endpoint=False)


sin_wave = a * np.sin(2 * np.pi * freq * t)


plt.plot(t,sin_wave)
plt.title("Sin Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()