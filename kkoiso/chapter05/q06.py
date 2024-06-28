import numpy as np
import matplotlib.pyplot as plt


fs = 16000
T = 1
N = fs * T
t = np.linspace(0, T, N, endpoint=False)
f = 440
a = 1

s = a * np.sin(2 * np.pi * f * t)


np.random.seed(0)
noise = np.random.normal(0, 1, N)
SNR = 10
noise_amplitude = a / (10 ** (SNR / 20))
epsilon = noise_amplitude * noise


x1 = s + epsilon
x2 = np.roll(s, 10) + epsilon
x3 = np.roll(s, 20) + epsilon

x = (x1 + x2 + x3) / 3
plt.figure(figsize=(10, 6))
plt.plot(t[: int(0.01 * fs)], x[: int(0.01 * fs)])
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Multichannel Signals")
plt.legend()
plt.show()
