import numpy as np
from scipy.signal import stft
import matplotlib.pyplot as plt
from q04 import spatial_correlation_matrix

fs = 16000
T = 5
N = fs * T
np.random.seed(0)
white_noise = np.random.normal(0, 1, (2, N))

f, t, Zxx1 = stft(white_noise[0], fs, window="hann", nperseg=512, noverlap=256)
f, t, Zxx2 = stft(white_noise[1], fs, window="hann", nperseg=512, noverlap=256)
X = np.stack((Zxx1, Zxx2), axis=0)


R = spatial_correlation_matrix(X)


print(R[100].real)
