import numpy as np
import matplotlib.pyplot as plt
import wave

#1-9
from scipy.io import wavfile
output_noise = 'sin_wave_with_noise_6dB.wav'
rate, data = wavfile.read(output_noise)


downsampled_data = data[::2]


output_downsampled = 'downsampled_8kHz.wav'
wavfile.write(output_downsampled, 8000, downsampled_data.astype(np.int16))
