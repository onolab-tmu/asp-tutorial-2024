import numpy as np
import matplotlib.pyplot as plt


def frequency_response(a, b, fs):
    omega = np.linspace(0, 2 * np.pi, fs, endpoint=False)

    num = np.zeros(len(omega), dtype=np.complex128)
    den = np.zeros(len(omega), dtype=np.complex128)

    for k in range(len(b)):
        num = num + b[k] * np.exp(-1j * (omega) * k)

    den = den + 1
    for k in range(1, len(a)):
        den = den + a[k] * np.exp(-1j * (omega) * k)

    H = num / den

    return omega, H
