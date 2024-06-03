import numpy as np

def calc_H(a, b, omega):
    N = a.size
    M = b.size
    k_a = np.arange(1, N)
    k_b = np.arange(M)
    sum_a = np.sum(a[k_a] * np.exp(-1j*omega*k_a))
    sum_b = np.sum(b[k_b] * np.exp(-1j*omega*k_b))
    
    return sum_b / (1 + sum_a)
