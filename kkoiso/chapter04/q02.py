import numpy as np
import matplotlib.pyplot as plt
from q01 import zero_padding


def frame_split(x, L, S):
    padded_x = zero_padding(x, L, S)
    T = (len(padded_x) - L) // S + 1

    frames = np.zeros((T, L))
    for t in range(T):
        frames[t] = padded_x[t * S : t * S + L]

    return frames
