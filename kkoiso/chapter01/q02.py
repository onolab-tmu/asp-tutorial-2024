import numpy as np
import matplotlib.pyplot as plt
#1-2
import wave

a = 1.0
freq= 440 
samp_rate = 16000 
d = 3  

t = np.linspace(0, d, int(samp_rate * d), endpoint=False)


sin_wave = a * np.sin(2 * np.pi * freq * t)
output = 'sin_wave_440Hz.wav'
with wave.open(output, 'w') as wf:
    wf.setnchannels(1)  
    wf.setsampwidth(2)  
    wf.setframerate(samp_rate)
    wf.writeframes((sin_wave * 32767).astype(np.int16).tobytes())

