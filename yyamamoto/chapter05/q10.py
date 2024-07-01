import numpy as np
import matplotlib.pyplot as plt
from q05 import stft
from q04 import correlation_matrix

def spatial_spectrum(z):
    M = z.shape[0]
    L = 1024
    S = 512
    window = np.hanning(L)
    T, F = stft(L, S, window, z[0]).shape
    Z = np.zeros((M, F, T), dtype=complex)
    for m in range(M):
        Z[m] = stft(L, S, w, z).T
    corr_matrix = correlation_matrix(Z)

    
