from scipy.signal import istft, stft
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
x = (s + np.roll(s, 10) + np.roll(s, 20)) / 3

x1 = s + epsilon
x2 = np.roll(s, 10) + epsilon
x3 = np.roll(s, 20) + epsilon


f, t, X1 = stft(x1, fs, window="hann", nperseg=1024, noverlap=512)
f, t, X2 = stft(x2, fs, window="hann", nperseg=1024, noverlap=512)
f, t, X3 = stft(x3, fs, window="hann", nperseg=1024, noverlap=512)

X = np.stack((X1, X2, X3), axis=0)
F, T = X1.shape


tau = np.array([0, 10 / fs, 20 / fs])
Y = np.zeros((F, T), dtype=complex)
for f in range(F):
    w_f = 1 / 3 * np.exp(-1j * 2 * np.pi * f * tau[:, None] * fs / 2 / F)
    for t in range(T):
        x_ft = X[:, f, t]
        Y[f, t] = np.conj(w_f.T).dot(x_ft)


_, y = istft(Y, fs, window="hann", nperseg=1024, noverlap=512)
t = np.linspace(0, 1, 1 * fs, endpoint=False)


plt.figure(figsize=(10, 6))
plt.plot(t[: int(0.01 * fs)], y[: int(0.01 * fs)])
plt.xlim(0, 0.01)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Enhanced Signal by Delay Sum Beamformer")
plt.show()
