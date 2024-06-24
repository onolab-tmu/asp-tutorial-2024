import numpy as np
import matplotlib.pyplot as plt


def zero_padding(x, L, S):
    N = len(x)
    padding_size = L - S
    padded_x = np.concatenate(([0] * padding_size, x, [0] * padding_size))
    zero_add = S - (len(padded_x) % S) + (L - S)
    padded_x = np.concatenate((padded_x, [0] * zero_add))

    return padded_x
