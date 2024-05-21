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

#1-2
import wave


output = 'sin_wave_440Hz.wav'
with wave.open(output, 'w') as wf:
    wf.setnchannels(1)  
    wf.setsampwidth(2)  
    wf.setframerate(samp_rate)
    wf.writeframes((sin_wave * 32767).astype(np.int16).tobytes())


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

#1-4
white_noise = np.random.normal(0, 1, len(t))


plt.plot(t, white_noise) 
plt.title("White Noise")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()


#1-5
mixed_signal = sin_wave + white_noise


plt.plot(t, mixed_signal)  
plt.title("Mixed Signal (Sin Wave + White Noise)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

#1-6
def calculate_snr(signal, noise):
    s_power = np.sum(signal ** 2) / len(signal)
    n_power = np.sum(noise ** 2) / len(noise)
    snr = 10 * np.log10(s_power / n_power)
    return snr

#1-7
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


#1-9
from scipy.io import wavfile

rate, data = wavfile.read(output_noise)


downsampled_data = data[::2]


output_downsampled = 'downsampled_8kHz.wav'
wavfile.write(output_downsampled, 8000, downsampled_data.astype(np.int16))

#1-10
filtered_signal = np.convolve(downsampled_data, np.ones(5)/5, mode='valid')

plt.figure(figsize=(14, 6))
plt.subplot(2, 1, 1)
plt.plot(downsampled_data[:1000])
plt.title("Original Downsampled Signal (8 kHz)")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(filtered_signal[:1000])
plt.title("Filtered Signal (5-point Moving Average)")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
