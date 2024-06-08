import numpy as np
import matplotlib.pyplot as plt
from q02 import frame_split


def stft(x, L, S, w):
    frames = frame_split(x, L, S)
    windowed_frames = frames * w
    stft_matrix = np.fft.rfft(windowed_frames, axis=1)

    return stft_matrix
