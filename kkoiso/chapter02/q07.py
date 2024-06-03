import numpy as np
import matplotlib.pyplot as plt

def Hamming_Window(N):
    n = np.arange(N)
    return 0.54 - 0.46 * np.cos((2 * np.pi * n )/ (N - 1))