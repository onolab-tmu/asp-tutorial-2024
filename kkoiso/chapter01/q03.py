import numpy as np
import matplotlib.pyplot as plt
import wave
a = 1.0
freq= 440 
samp_rate = 16000 
d = 3  

t = np.linspace(0, d, int(samp_rate * d), endpoint=False)


sin_wave = a * np.sin(2 * np.pi * freq * t)
#1-3
freq2 = 660  
sin_wave2 = a * np.sin(2 * np.pi * freq2 * t)


stereo_wave = np.vstack((sin_wave, sin_wave2)).T


output_stereo = 'stereo_sin_waves.wav'
with wave.open(output_stereo, 'w') as wf:
    wf.setnchannels(2) 
    wf.setsampwidth(2)  
    wf.setframerate(samp_rate)
    wf.writeframes((stereo_wave * 32767).astype(np.int16).tobytes())
