import numpy as np
import matplotlib.pyplot as plt
import wave

def calculate_snr(signal, noise):
    s_power = np.sum(signal ** 2) / len(signal)
    n_power = np.sum(noise ** 2) / len(noise)
    snr = 10 * np.log10(s_power / n_power)
    return snr