import numpy as np
from scipy.signal import stft
from q04 import spatial_correlation_matrix

fs = 16000
sec = 5
L = 512
S = 256

np.random.seed(1)
noise = np.random.normal(0, 1, size=(2, sec * fs))

f, t, X = stft(noise, fs, nperseg=L, noverlap=L - S)

R = spatial_correlation_matrix(X)

print(R[100].real)

# [[3.19811768e-03 7.08151469e-06]
#  [7.08151469e-06 3.29345106e-03]]
