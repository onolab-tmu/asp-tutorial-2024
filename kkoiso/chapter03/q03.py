import numpy as np
import matplotlib.pyplot as plt
from q02 import circular_conv


def zero_padded_circular_conv(x, h):
    N = len(x)
    x_padded = np.concatenate([x, np.zeros(N)])
    h_padded = np.concatenate([h, np.zeros(N)])
    z = circular_conv(x_padded, h_padded)
    return z
