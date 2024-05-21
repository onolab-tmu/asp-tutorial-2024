import numpy as np
import matplotlib.pyplot as plt
import wave

#1-7
def add_noise_with_snr(signal, desired_snr_db):
    s_power = np.sum(signal ** 2) / len(signal)
    snr_linear = 10 ** (desired_snr_db / 10)
    n_power = s_power / snr_linear
    noise = np.random.normal(0, np.sqrt(n_power), len(signal))
    return signal + noise