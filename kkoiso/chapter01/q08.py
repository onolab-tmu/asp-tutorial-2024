import numpy as np
import matplotlib.pyplot as plt
import wave


a = 1.0
freq= 440 
samp_rate = 16000 
d = 3  

t = np.linspace(0, d, int(samp_rate * d), endpoint=False)


sin_wave = a * np.sin(2 * np.pi * freq * t)


def add_noise_with_snr(signal, desired_snr_db):
    s_power = np.sum(signal ** 2) / len(signal)
    snr_linear = 10 ** (desired_snr_db / 10)
    n_power = s_power / snr_linear
    noise = np.random.normal(0, np.sqrt(n_power), len(signal))
    return signal + noise

#1-8
desired_snr= 6
noise_signal = add_noise_with_snr(sin_wave, desired_snr)

output_noise = 'sin_wave_with_noise_6dB.wav'
with wave.open(output_noise, 'w') as wf:
    wf.setnchannels(1)  
    wf.setsampwidth(2)  
    wf.setframerate(samp_rate)
    wf.writeframes((noise_signal * 32767).astype(np.int16).tobytes())